#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user, decode_token
from models.user import UserModel
#from app.util.logz import create_logger

class Password(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('old_password',
        type=str,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('new_password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    #self.args = parser.parse_args(strict=True)

    def __init__(self):
        pass
        ##self.logger = create_logger()

    @jwt_required()
    def put(self, token):
        data = Password.parser.parse_args()
        if not data['old_password']:
            return {'message': 'Old password is required'}, 400

        if current_user.check_password(data['old_password']):
            current_user.password = data['new_password']
            try:
                current_user.save_to_db()
            except:
                return {"message": "An error occurred inserting the user."}, 500
            return {"message": "User password updated successfully."}, 201
        else:
            return {"message": "Old password is incorrect."}, 400

    def post(self, token):
        data = Password.parser.parse_args()
        jwt_data = decode_token(token)
        identity = jwt_data["sub"]
        user = UserModel.query.filter_by(id=identity).one_or_none()
        user.password = data['new_password']
        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the user."}, 500
        return {"message": "User password updated successfully."}, 201
