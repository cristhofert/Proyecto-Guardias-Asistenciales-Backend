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

    def json(self):
        return {
            'id': audit.id,
            'user_id': audit.user_id,
            'action': audit.action
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class AuditList(Resource):
    def get(self):
        return {'audits': [audit.json() for audit in Audit.query.all()]}