#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
#from flask_jwt_extended import jwt_required
from models.user import UserModel
#from app.util.logz import create_logger

class User(Resource):
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
    def get(self, id):
        user = UserModel.find_by_id(id)
        #self.logger.info(f'returning user: {user.json()}')
        if user:
            return user.json()
        return {'message': 'this not found'}, 404

    #@jwt_required()
    def post(self, id):
        #self.logger.info(f'parsed args: {self.parser.parse_args()}')

        if UserModel.find_by_id(id):
            return {'message': "An user with id '{}' already exists.".format(
                id)}, 400
        data = self.parser.parse_args()
        user = UserModel(data['id'], data['name'], data['password'])

        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the user."}, 500
        return user.json(), 201

    #@jwt_required()
    def delete(self, id):

        user = UserModel.find_by_id(id)
        if user:
            user.delete_from_db()

            return {'message': 'user has been deleted'}

    #@jwt_required()
    def put(self, id):
        # Create or Update
        data = self.parser.parse_args()
        user = UserModel.find_by_id(id)

        if user is None:
            user = UserModel(id, data['name'], data['password'])
        else:
            if data['name'] is not None: user.name = data['name']
            if data['password'] is not None: user.password = data['password']

        user.save_to_db()

        return user.json()

class UserList(Resource):
    #@jwt_required()
    def get(self):
        return {
            'users': [user.json() for user in UserModel.query.all()]}  # More pythonic
        ##return {'users': list(map(lambda x: x.json(), UserModel.query.all()))} #Alternate Lambda way
