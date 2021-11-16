#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
from models.subscription import SubscriptionModel
#from app.util.logz import create_logger

class Subscription(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('type', type=str, required=True, help="This field cannot be left blank!")
    parse.add_argument('service_id', type=str, required=True, help="This field cannot be left blank!")

    def __init__(self):
        #self.logger = create_logger(__name__)
        pass

    @jwt_required()
    def get(self, id):
        subscription = SubscriptionModel.find_by_id(id)
        #self.logger.info("Subscription get: {}".format(subscription))
        if subscription and (subscription.json()['institution'] == current_user.json()['institution']):
            return subscription.json()
        return {'message': 'Subscription not found'}, 404

    @jwt_required()
    def post(self, id):
        data = Subscription.parse.parse_args()
        subscription = SubscriptionModel.find_by_service_id_type(data['service_id', data['type']])

        if subscription:
            return {'message': "An subscription with id '{}' already exists.".format(id)}, 400

        subscription = SubscriptionModel(**data, institution_id=current_user.json()['institution'])

        try:
            subscription.save_to_db()
        except:
            return {"message": "An error occurred inserting the subscription."}, 500

        return subscription.json(), 201

    @jwt_required()
    def put(self, id):
        data = Subscription.parse.parse_args()
        subscription = SubscriptionModel.find_by_id(id)

        if subscription.json()['institution'] == current_user.json()['institution'] :
            if subscription:
                subscription.type = data['type']
                subscription.service_id = data['service_id']
            else:
                subscription = SubscriptionModel(**data)

            subscription.save_to_db()

            return subscription.json()

        else:
            return {'message': 'access denied'}, 401

    @jwt_required()
    def delete(self, id):
        subscription = SubscriptionModel.find_by_id(id)
        if subscription and (subscription.json()['institution'] == current_user.json()['institution']):
            subscription.delete_from_db()
            return {'message': 'Subscription deleted'}
        return {'message': 'Subscription not found'}, 404

class SubscriptionList(Resource):
    @jwt_required()
    def get(self):
        return {'subscriptions': [subscription.json() for subscription in SubscriptionModel.query.filter_by(institution_id=current_user.json()['institution']).all()]}