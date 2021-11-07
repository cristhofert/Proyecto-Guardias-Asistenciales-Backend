#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
from models.notification import NotificationModel
#from app.util.logz import create_logger


class Notification(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('medical_doctor_id', type=str,
                       required=True, help="This field cannot be left blank!")
    parse.add_argument('message', type=str, required=True,
                       help="This field cannot be left blank!")
    parse.add_argument('read', type=bool, required=False,
                       help="This field cannot be left blank!")

    def __init__(self):
        #self.logger = create_logger(__name__)
        pass

    @jwt_required()
    def get(self, id):
        notification = NotificationModel.find_by_id(id)
        #self.logger.info("Notification get: {}".format(notification))
        if notification and (notification.json()['institution'] == current_user.json()['institution']):
            return notification.json()
        return {'message': 'Notification not found'}, 404

    @jwt_required()
    def post(self, id):
        data = self.parse.parse_args()
        notification = NotificationModel.find_by_id(data['id'])

        if notification:
            return {'message': "An notification with id '{}' already exists.".format(id)}, 400

        notification = NotificationModel(
            **data, institution_id=current_user.json()['institution'])

        try:
            notification.save_to_db()
        except:
            return {"message": "An error occurred inserting the notification."}, 500

        return notification.json(), 201

    @jwt_required()
    def put(self, id):
        data = self.parse.parse_args()
        notification = NotificationModel.find_by_id(data['id'])

        if notification.json()['institution'] == current_user.json()['institution']:
            if notification:
                notification.medical_doctor_id = data['medical_doctor_id']
                notification.read = data['read']
                notification.message = data['message']
            else:
                notification = NotificationModel(
                    **data, institution_id=current_user.json()['institution'])

            notification.save_to_db()

            return notification.json()
        else:
            return {'message': 'access denied'}, 401

    @jwt_required()
    def delete(self, id):
        notification = NotificationModel.find_by_id(id)
        if notification and (notification.json()['institution'] == current_user.json()['institution']):
            notification.delete_from_db()
            return {'message': 'Notification deleted'}
        return {'message': 'Notification not found'}, 404


class NotificationList(Resource):
    @jwt_required()
    def get(self):
        return {'notifications': [notification.json() for notification in Notification.query.filter_by(institution_id=current_user.json()['institution']).all()]}
