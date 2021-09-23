#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
#from flask_jwt_extended import jwt_required
from models.administrator import AdministratorModel
#from app.util.logz import create_logger

class Notification(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('medical_doctor_id', type=int, required=True, help="This field cannot be left blank!")
    parse.add_argument('message', type=str, required=True, help="This field cannot be left blank!")
    parse.add_argument('read', type=bool, required=False, help="This field cannot be left blank!")

    def __init__(self):
        #self.logger = create_logger(__name__)
        pass

    def json(self):
        return {
            'id': self.id,
            'medical_doctor_id': self.medical_doctor_id,
            'message': self.message,
            'read': self.read
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_medical_doctor_id(cls, medical_doctor_id):
        return cls.query.filter_by(medical_doctor_id=medical_doctor_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
class NotificationList(Resource):
    def get(self):
        return {'notifications': [notification.json() for notification in Notification.query.all()]}
