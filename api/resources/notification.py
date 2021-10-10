#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
#from flask_jwt_extended import jwt_required
from models.notification import NotificationModel
#from app.util.logz import create_logger

class Notification(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('medical_doctor_id', type=int, required=True, help="This field cannot be left blank!")
    parse.add_argument('message', type=str, required=True, help="This field cannot be left blank!")
    parse.add_argument('read', type=bool, required=False, help="This field cannot be left blank!")


    def __init__(self):
        #self.logger = create_logger(__name__)
        pass

    def get(self, id):
        notification = NotificationModel.find_by_id(id)
        #self.logger.info("Notification get: {}".format(notification))
        if notification:
            return notification.json()
        return {'message': 'Notification not found'}, 404

    #@jwt_required
    def post(self, id):
        data = self.parse.parse_args()
        notification = NotificationModel.find_by_id(id)

        if notification:
            return {'message': "An notification with id '{}' already exists.".format(id)}, 400

        notification = NotificationModel(**data)

        try:
            notification.save_to_db()
        except:
            return {"message": "An error occurred inserting the notification."}, 500

        return notification.json(), 201

    #@jwt_required
    def put(self, id):
        data = self.parse.parse_args()
        notification = NotificationModel.find_by_id(id)

        if notification:
            notification.type = data['type']
            notification.service_id = data['service_id']
        else:
            notification = NotificationModel(**data)

        notification.save_to_db()

        return notification.json()

    #@jwt_required
    def delete(self, id):
        notification = NotificationModel.find_by_id(id)
        if notification:
            notification.delete_from_db()
            return {'message': 'Notification deleted'}
        return {'message': 'Notification not found'}, 404

class NotificationList(Resource):
    def get(self):
        return {'notifications': [notification.json() for notification in Notification.query.all()]}
