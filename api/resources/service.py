#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
from models.service import ServiceModel
from models.subscription import SubscriptionModel
from util import access
from util.is_empty import is_empty

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

    def __init__(self):
        pass
        ##self.logger = create_logger()

    @jwt_required()  # Requires dat token
    def get(self, id):
        access.administor(current_user)
        service = ServiceModel.find_by_id(id)
        #self.logger.info(f'returning service: {service.json()}')
        if service and (service.json()['institution'] == current_user.json()['institution']):
            return service.json(), 201
        return {'message': 'Service not found'}, 404

    @jwt_required()
    def post(self, id):
        access.administor(current_user)
        #self.logger.info(f'parsed args: {Service.parser.parse_args()}')
        data = Service.parser.parse_args()
        if is_empty(data):
            return {'menssage': 'The field is required'}, 401
        if ServiceModel.find_by_name(data['name']):
            return {'message': "An service with name '{}' already exists.".format(
                data['name'])}, 400
        service = ServiceModel(data['name'], data['code'], current_user.json()['institution'])
        try:
            service.save_to_db()
        except:
            return {"message": "An error occurred inserting the service."}, 500

        print(f'Service  {service.id}. {type(service.id)}')
        subscription_list = SubscriptionModel("lista", service.id, current_user.json()['institution'])
        subscription_dispersion = SubscriptionModel("dispersi??n", service.id, current_user.json()['institution'])

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

    @jwt_required()
    def delete(self, id):
        access.administor(current_user)
        service = ServiceModel.find_by_id(id)
        if service and (service.json()['institution'] == current_user.json()['institution']):
            service.delete_from_db()

            return {'message': 'service has been deleted'}
        return {'message': 'service not found'}, 404

    @jwt_required()
    def put(self, id):
        access.administor(current_user)
        # Create or Update
        data = Service.parser.parse_args()
        if is_empty(data):
            return {'menssage': 'The field is required'}, 401
        service = ServiceModel.find_by_id(id)

        if service.json()['institution'] == current_user.json()['institution'] :
            if service is None:
                service = ServiceModel(data['name'], data['code'])	
            else:
                if data['name'] is not None: service.name = data['name']
                if data['code'] is not None: service.code = data['code']

            try:
                service.save_to_db()
            except BaseException as err:
                return {"message": f"An error occurred inserting the service. ERROR: {err}"}, 500

            return service.json(), 201
        else:
            return {'message': 'access denied'}, 401

class ServiceList(Resource):
    @jwt_required()
    def get(self):
        access.administor(current_user)
        return {
            'services': [service.json() for service in ServiceModel.query.filter_by(institution_id=current_user.json()['institution']).all()]} , 201