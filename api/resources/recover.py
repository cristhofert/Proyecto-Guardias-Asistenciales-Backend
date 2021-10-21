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


class Recover(Resource):
    def __init__(self):
        self.logger = create_logger()

    # only allow price changes, no name changes allowed
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=int, required=True,
                        help='This field cannot be left blank')

    @jwt_required()
    def post(self):
        if current_user.type == 'medical_doctor':
            return {'message': 'You are not allowed to recover password'}, 401
            
        data = self.parser.parse_args()
        id = data['id']

        user = UserModel.query.filter_by(id=id).one_or_none()
        if not user:
            return {'message': 'Wrong id or password.'}, 401
        # Notice that we are passing in the actual sqlalchemy user object here
        access_token = create_access_token(
            identity=user)
        return jsonify(access_token=access_token)# En un fituro seria enviado el token de acceso al email del usuario
