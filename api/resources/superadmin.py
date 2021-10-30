#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
from models.administrator import AdministratorModel


class SuperAdmin(Resource):
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

    def post(self, id):
        #self.logger.info(f'parsed args: {self.parser.parse_args()}')
        data = self.parser.parse_args()
        if AdministratorModel.find_by_id(data['id']):
            return {'message': "An administrator with id '{}' already exists.".format(
                id)}, 400

        administrator = AdministratorModel(
            data['id'], data['name'], data['password'], 1)
        try:
            administrator.save_to_db()
        except:
            return {"message": "An error occurred inserting the administrator."}, 500
        return administrator.json(), 201
