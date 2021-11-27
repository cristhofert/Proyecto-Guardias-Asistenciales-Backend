#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
from models.medical_doctor import MedicalDoctorModel
from models.subscription import SubscriptionModel
from cerberus import Validator

schema = {
    'id': {'type': 'string'},
    'name': {'type': 'string'},
    'password': {'type': 'string'},
    'speciality': {'type': 'string'},
    'phone': {'type': 'string'},
    'email': {'type': 'string'},
    'zone_id': {'type': 'integer', 'required': False},
    'subscriptions': {'type': 'list', 'required': False}
}
md = Validator(schema)

class Create:
    def create(self, data):
        if MedicalDoctorModel.find_by_id(data['id']):
            return {'message': "An medical_doctor with name '{}' already exists.".format(
                id)}, 400
        medical_doctor = MedicalDoctorModel(data['id'], data['name'], data['password'],
                                            data['speciality'], data['phone'], data['email'], data['zone_id'], current_user.json()['institution'])

        if data['subscriptions'] is not None:
            for subscription in data['subscriptions']:
                subscription = SubscriptionModel.find_by_id(subscription)
                medical_doctor.subscriptions.append(subscription)

        try:
            medical_doctor.save_to_db()
        except:
            return {"message": "An error occurred inserting the medical_doctor."}, 500
        return medical_doctor.json(), 201
        
class MedicalDoctor(Resource):
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
    parser.add_argument('speciality',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('phone',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('zone_id',
                        type=int,
                        required=False,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('subscriptions',
                        type=int,
                        required=False,
                        action='append',
                        help="This field cannot be left blank!"
                        )

    def __init__(self):
        pass
        ##self.logger = create_logger()

    @jwt_required()  # Requires dat token
    def get(self, id):
        medical_doctor = MedicalDoctorModel.find_by_id(id)
        #self.logger.info(f'returning medical_doctor: {medical_doctor.json()}')
        if medical_doctor and (medical_doctor.json()['institution'] == current_user.json()['institution']):
            return medical_doctor.json()
        return {'message': 'this not found'}, 404

    @jwt_required()
    def post(self, id):
        #self.logger.info(f'parsed args: {self.parser.parse_args()}')

        data = self.parser.parse_args()
        c = Create()
        return c.create(data)

    @jwt_required()
    def delete(self, id):
        medical_doctor = MedicalDoctorModel.find_by_id(id)
        if medical_doctor and (medical_doctor.json()['institution'] == current_user.json()['institution']):
            medical_doctor.delete_from_db()

            return {'message': 'medical_doctor has been deleted'}
        return {'message': 'medical_doctor not found'}, 404

    @jwt_required()
    def put(self, id):
        # Create or Update
        data = self.parser.parse_args()
        medical_doctor = MedicalDoctorModel.find_by_id(id)
        if medical_doctor and medical_doctor.json()['institution'] == current_user.json()['institution']:
            if data['name'] is not None:
                medical_doctor.name = data['name']
            if data['password'] is not None:
                medical_doctor.password = data['password']
            if data['speciality'] is not None:
                medical_doctor.speciality = data['speciality']
            if data['phone'] is not None:
                medical_doctor.phone = data['phone']
            if data['email'] is not None:
                medical_doctor.email = data['email']
            if data['zone_id'] is not None:
                medical_doctor.zone_id = data['zone_id']
            if data['subscriptions'] is not None:
                medical_doctor.subscriptions = []
                for subscription in data['subscriptions']:
                    subscription = SubscriptionModel.find_by_id(subscription)
                    medical_doctor.subscriptions.append(subscription)

            medical_doctor.save_to_db()

            return medical_doctor.json()
        else:
            return {'message': 'access denied'}, 401


class MedicalDoctorList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("MDs", 
        type=dict, 
        action="append", 
        default=[],        
        required=False,
        help="This field cannot be left blank!")

    @jwt_required()
    def get(self):
        return {
            'medical_doctors': [medical_doctor.json() for medical_doctor in MedicalDoctorModel.query.filter_by(institution_id=current_user.json()['institution']).all()]}
        # return {'medical_doctors': list(map(lambda x: x.json(), MedicalDoctorModel.query.all()))} #Alternate Lambda way

    @jwt_required()
    def post(self):
        data = self.parser.parse_args()
        MDs = []
        for medical_doctor in data['MDs']:
            if medical_doctor!={} and md.validate(medical_doctor):
                if not medical_doctor.get('zone_id'):
                    medical_doctor['zone_id'] = 1
                c = Create()
                MDs.append(c.create(medical_doctor))
            else:
                MDs.append(md.errors)
        return {'MDs': MDs}
