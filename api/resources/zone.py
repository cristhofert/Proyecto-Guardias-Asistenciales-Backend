#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
#from flask_jwt_extended import jwt_required
from models.zone import ZoneModel
#from app.util.logz import create_logger

class Zone(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('id',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )


    def __init__(self):
        pass
        ##self.logger = create_logger()

    #@jwt_required()  # Requires dat token
    def get(self, id):
        zone = ZoneModel.find_by_id(id)
        #self.logger.info(f'returning zone: {zone.json()}')
        if zone:
            return zone.json()
        return {'message': 'Zone not found'}, 404

    #@jwt_required()
    def post(self, id):
        #self.logger.info(f'parsed args: {Zone.parser.parse_args()}')

        if ZoneModel.find_by_id(id):
            return {'message': "An zone with id '{}' already exists.".format(
                id)}, 400
        data = Zone.parser.parse_args()
        zone = ZoneModel(data['id'], data['code'])

        try:
            zone.save_to_db()
        except:
            return {"message": "An error occurred inserting the zone."}, 500
        return zone.json(), 201

    #@jwt_required()
    def delete(self, id):

        zone = ZoneModel.find_by_id(id)
        if zone:
            zone.delete_from_db()

            return {'message': 'zone has been deleted'}

    #@jwt_required()
    def put(self, id):
        # Create or Update
        data = Zone.parser.parse_args()
        zone = ZoneModel.find_by_id(id)

        if zone is None:
            zone = ZoneModel(id, data['name'])
        else:
            if data['name'] is not None: zone.name = data['name']

        zone.save_to_db()

        return zone.json()


class ZoneList(Resource):
    #@jwt_required()
    def get(self):
        return {
            'zones': [zone.json() for zone in ZoneModel.query.all()]}  # More pythonic
        ##return {'zones': list(map(lambda x: x.json(), ZoneModel.query.all()))} #Alternate Lambda way
