#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
from models.zone import ZoneModel
from util import access
from util.is_empty import is_empty

class Zone(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank!",
    )
    parser.add_argument('geotag',
        type=str,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('longitude',
        type=str,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('latitude',
        type=str,
        required=False,
        help="This field cannot be left blank!"
    )
    
    #self.args = parser.parse_args(strict=True)

    def __init__(self):
        pass
        ##self.logger = create_logger()

    @jwt_required() 
    def get(self, id):
        access.administor(current_user)
        zone = ZoneModel.find_by_id(id)

        if zone and (zone.json()['institution'] == current_user.json()['institution']):
            return zone.json(), 201
        return {'message': 'Zone not found'}, 404

    @jwt_required()
    def post(self, id):
        access.administor(current_user)
        data = Zone.parser.parse_args()
        if is_empty(data):
            return {'menssage': 'The field is required'}, 401
        if ZoneModel.find_by_name(data['name']):
            return {'message': "An zone with name '{}' already exists.".format(
                data['name'])}, 400
        zone = ZoneModel(**data, institution_id=current_user.json()['institution'])

        try:
            zone.save_to_db()
        except:
            return {"message": "An error occurred inserting the zone."}, 500
        return zone.json(), 201

    @jwt_required()
    def delete(self, id):
        access.administor(current_user)
        zone = ZoneModel.find_by_id(id)
        if zone and (zone.json()['institution'] == current_user.json()['institution']):
            zone.delete_from_db()
            return {'message': 'zone has been deleted'}, 201
        else:
            return {'message': 'zone not found'}, 404

    @jwt_required()
    def put(self, id):
        access.administor(current_user)
        # Create or Update
        data = Zone.parser.parse_args()
        if is_empty(data):
            return {'menssage': 'The field is required'}, 401
        zone = ZoneModel.find_by_id(id)

        if zone and zone.json()['institution'] == current_user.json()['institution'] :
            if data['name'] is not None: zone.name = data['name']
            if data['geotag'] is not None: zone.geotag = data['geotag']
            if data['longitude'] is not None: zone.longitude = data['longitude']
            if data['latitude'] is not None: zone.latitude = data['latitude']

            zone.save_to_db()

            return zone.json(), 201
        else:
            return {'message': 'zone not found'}, 401


class ZoneList(Resource):
    @jwt_required()
    def get(self):
        access.administor(current_user)
        return {
            'zones': [zone.json() for zone in ZoneModel.query.filter_by(institution_id=current_user.json()['institution']).all()]}, 201