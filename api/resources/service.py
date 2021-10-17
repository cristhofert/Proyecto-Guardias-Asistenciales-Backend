#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask import jsonify
from flask_restful import Resource, reqparse
#from flask_jwt_extended import jwt_required
from models.service import ServiceModel
from models.subscription import SubscriptionModel
#from app.util.logz import create_logger

class Service(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('code',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('color',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def __init__(self):
        pass
        ##self.logger = create_logger()

    #@jwt_required()  # Requires dat token
    def get(self, id):
        service = ServiceModel.find_by_id(id)
        #self.logger.info(f'returning service: {service.json()}')
        if service:
            return service.json()
        return {'message': 'Service not found'}, 404

    #@jwt_required()
    def post(self, id):
        #self.logger.info(f'parsed args: {Service.parser.parse_args()}')
        data = Service.parser.parse_args()

        if ServiceModel.find_by_name(data['name']):
            return {'message': "An service with name '{}' already exists.".format(
                data['name'])}, 400
        service = ServiceModel(data['name'], data['code'], data['color'])
        try:
            service.save_to_db()
        except:
            return {"message": "An error occurred inserting the service."}, 500

        print(f'Service  {service.id}. {type(service.id)}')
        subscription_list = SubscriptionModel("lista", service.id)
        subscription_dispersion = SubscriptionModel("dispersión", service.id)

        try:
            subscription_list.save_to_db()
            subscription_dispersion.save_to_db()
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise
        return {
            "service": service.json(),
            "subscription_list": subscription_list.json(),
            "subscription_dispersion": subscription_dispersion.json()
            }, 201

    #@jwt_required()
    def delete(self, id):

        service = ServiceModel.find_by_id(id)
        if service:
            service.delete_from_db()

            return {'message': 'service has been deleted'}

    #@jwt_required()
    def put(self, name):
        # Create or Update
        data = Service.parser.parse_args()
        service = ServiceModel.find_by_name(name)

        if service is None:
            service = ServiceModel(**data)	
        else:
            if data['code'] is not None: service.code = data['code']
            if data['color'] is not None: service.color = data['color']
            if data['name'] is not None: service.name = data['name']

        service.save_to_db()

        return service.json()


class ServiceList(Resource):
    #@jwt_required()
    def get(self):
        return {
            'services': [service.json() for service in ServiceModel.query.all()]}  # More pythonic
        ##return {'services': list(map(lambda x: x.json(), ServiceModel.query.all()))} #Alternate Lambda way
