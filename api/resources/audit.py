#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
#from flask_jwt_extended import jwt_required
from models.administrator import AdministratorModel
#from app.util.logz import create_logger

class Audit(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('user_id', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('action', type=str, required=True, help="This field cannot be left blank!")

    def __init__(self):
        #self.logger = create_logger(__name__)
        pass

    def get(self, id):
        audit = AuditModel.find_by_id(id)
        #self.logger.info("Audit get: {}".format(audit))
        if audit:
            return audit.json()
        return {'message': 'Audit not found'}, 404

    #@jwt_required
    def post(self, id):
        data = self.parse.parse_args()
        audit = AuditModel.find_by_id(id)

        if audit:
            return {'message': "An audit with id '{}' already exists.".format(id)}, 400

        audit = AuditModel(**data)

        try:
            audit.save_to_db()
        except:
            return {"message": "An error occurred inserting the audit."}, 500

        return audit.json(), 201

    #@jwt_required
    def put(self, id):
        data = self.parse.parse_args()
        audit = AuditModel.find_by_id(id)

        if audit:
            audit.type = data['type']
            audit.service_id = data['service_id']
        else:
            audit = AuditModel(**data)

        audit.save_to_db()

        return audit.json()

    #@jwt_required
    def delete(self, id):
        audit = AuditModel.find_by_id(id)
        if audit:
            audit.delete_from_db()
            return {'message': 'Audit deleted'}
        return {'message': 'Audit not found'}, 404

class AuditList(Resource):
    def get(self):
        return {'audits': [audit.json() for audit in AuditModel.query.all()]}