#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
from models.administrator import AdministratorModel
from util import access
from util.ci import CedulaUruguaya
import bcrypt
#from app.util.logz import create_logger

class Administrator(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=str,
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

    ci = CedulaUruguaya()
    def __init__(self):
        pass
        ##self.logger = create_logger()

    @jwt_required()  # Requires dat token
    def get(self, id):
        access.administor(current_user)

        administrator = AdministratorModel.find_by_id(id)
        #self.logger.info(f'returning administrator: {administrator.json()}')
        if administrator and (administrator.json()['institution'] == current_user.json()['institution']):
            return administrator.json(), 201
        return {'message': 'this not found'}, 404

    @jwt_required()
    def post(self, id):
        access.administor(current_user)
        data = self.parser.parse_args()
        if not self.ci.validate_ci(int(data['id'])):
            return {'message': 'ci not valid'}, 401
        hashed = bcrypt.hashpw(
            data['password'].encode('utf-8'), bcrypt.gensalt())
        if AdministratorModel.find_by_id(data['id']):
            return {'message': "An administrator with id '{}' already exists.".format(
                id)}, 400
        administrator = AdministratorModel(
            data['id'], data['name'], hashed, current_user.json()['institution'])

        try:
            administrator.save_to_db()
        except:
            return {"message": "An error occurred inserting the administrator."}, 500
        return administrator.json(), 201

    @jwt_required()
    def delete(self, id):
        access.administor(current_user)

        administrator = AdministratorModel.find_by_id(id)
        if administrator and (administrator.json()['institution'] == current_user.json()['institution']):

            if administrator.delete_from_db() == 'Cannot delete superadmin':
                return {'message': 'cannot delete superadmin'}, 404

            return {'message': 'administrator has been deleted'}
        return {'message': 'this not found'}, 404

    @jwt_required()
    def put(self, id):
        # Create or Update
        access.administor(current_user)
        data = self.parser.parse_args()
        if not self.ci.validate_ci(int(data['id'])):
            return {'message': 'ci not valid'}, 401
        hashed = bcrypt.hashpw(
            data['password'].encode('utf-8'), bcrypt.gensalt())
        administrator = AdministratorModel.find_by_id(data['id'])

        if administrator.json()['institution'] == current_user.json()['institution']:
            if administrator is None:
                administrator = AdministratorModel(
                    data['id'], data['name'], hashed, current_user.json()['institution'])
            else:
                if data['id'] is not None:
                    administrator.id = data['id']
                if data['name'] is not None:
                    administrator.name = data['name']
                if data['password'] is not None:
                    administrator.password = hashed

            administrator.save_to_db()

            return administrator.json(), 201
        else:
            return {'message': 'access denied'}, 401


class AdministratorList(Resource):
    @jwt_required()
    def get(self):
        access.administor(current_user)
        return {
            'administrators': [administrator.json() for administrator in AdministratorModel.query.filter_by(institution_id=current_user.json()['institution']).all()]}, 201
