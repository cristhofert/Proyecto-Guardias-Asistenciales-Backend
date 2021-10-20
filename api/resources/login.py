#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import current_user
from models.user import UserModel
from util.encoder import AlchemyEncoder
import json
from util.logz import create_logger


class Login(Resource):
    def __init__(self):
        self.logger = create_logger()

    # only allow price changes, no name changes allowed
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True,
                        help='This field cannot be left blank')

    def post(self):
        data = self.parser.parse_args()
        id = data['id']
        password = data['password']

        user = UserModel.query.filter_by(id=id).one_or_none()
        if not user or not user.check_password(password):
            return {'message': 'Wrong id or password.'}, 401
        # Notice that we are passing in the actual sqlalchemy user object here
        access_token = create_access_token(
            identity=user)
        return jsonify(access_token=access_token)

    @jwt_required()  # Requires dat token
    def get(self):
        print("GET login")
        # We can now access our sqlalchemy User object via `current_user`.
        return jsonify(
            id=current_user.id, 
            name=current_user.name,
            institution_id=current_user.institution_id,
            type=current_user.type
            )
