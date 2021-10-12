#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
#from flask_jwt_extended import jwt_required
from models.administrator import AdministratorModel
#from app.util.logz import create_logger

class Administrator(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def __init__(self):
        pass
        ##self.logger = create_logger()

    #@jwt_required()  # Requires dat token
    def get(self, name):
        administrator = AdministratorModel.find_by_name(name)
        #self.logger.info(f'returning administrator: {administrator.json()}')
        if administrator:
            return administrator.json()
        return {'message': 'this not found'}, 404

    #@jwt_required()
    def post(self, name):
        #self.logger.info(f'parsed args: {self.parser.parse_args()}')

        if AdministratorModel.find_by_name(name):
            return {'message': "An administrator with name '{}' already exists.".format(
                name)}, 400
        data = self.parser.parse_args()
        administrator = AdministratorModel(data['name'], data['code'])

        try:
            administrator.save_to_db()
        except:
            return {"message": "An error occurred inserting the administrator."}, 500
        return administrator.json(), 201

    #@jwt_required()
    def delete(self, name):

        administrator = AdministratorModel.find_by_name(name)
        if administrator:
            administrator.delete_from_db()

            return {'message': 'administrator has been deleted'}

    #@jwt_required()
    def put(self, name):
        # Create or Update
        data = self.parser.parse_args()
        administrator = AdministratorModel.find_by_name(name)

        if administrator is None:
            administrator = AdministratorModel(name, data['code'])
        else:
            if date['name'] is not None: user.name = data['name']
            if date['password'] is not None: user.password = data['password']
            
        administrator.save_to_db()

        return administrator.json()


class AdministratorList(Resource):
    #@jwt_required()
    def get(self):
        return {
            'administrators': [administrator.json() for administrator in AdministratorModel.query.all()]}  # More pythonic
        ##return {'administrators': list(map(lambda x: x.json(), AdministratorModel.query.all()))} #Alternate Lambda way
