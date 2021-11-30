#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
from models.user import UserModel
#from app.util.logz import create_logger

class User(Resource):
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
    parser.add_argument('institution_id',
        type=int,
        required=False,
        help="This field cannot be left blank!"
    )

    def __init__(self):
        pass
        ##self.logger = create_logger()

    @jwt_required()  # Requires dat token
    def get(self, id):
        user = UserModel.find_by_id(id)
        #self.logger.info(f'returning user: {user.json()}')
        if user and (user.json()['institution'] == current_user.json()['institution']):
            return user.json(), 201
        return {'message': 'this not found'}, 404

    @jwt_required()
    def delete(self, id):
        user = UserModel.find_by_id(id)
        if user and (user.json()['institution'] == current_user.json()['institution']):
            user.delete_from_db()
            return {'message': 'user has been deleted'}
        return {'message': 'this not found'}, 404

    @jwt_required()
    def put(self, id):
        # Create or Update
        data = self.parser.parse_args()
        user = UserModel.find_by_id(id)

        if user.json()['institution'] == current_user.json()['institution'] :
            if user is None:
                user = UserModel(id, data['name'], data['password'], data['institution_id'])
            else:
                if data['name'] is not None: user.name = data['name']
                if data['password'] is not None: user.password = data['password']

            user.save_to_db()

            return user.json(), 201
        else:
            return {'message': 'access denied'}, 401

class UserList(Resource):
    @jwt_required()
    def get(self):
        return {
            'users': [user.json() for user in UserModel.query.filter_by(institution_id=current_user.json()['institution']).all()]}, 201