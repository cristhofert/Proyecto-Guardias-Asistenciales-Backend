#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
#from flask_jwt_extended import jwt_required
from models.medical_doctor import MedicalDoctorModel
#from app.util.logz import create_logger

class MedicalDoctor(Resource):
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
        medical_doctor = MedicalDoctorModel.find_by_id(id)
        #self.logger.info(f'returning medical_doctor: {medical_doctor.json()}')
        if medical_doctor:
            return medical_doctor.json()
        return {'message': 'this not found'}, 404

    #@jwt_required()
    def post(self, id):
        #self.logger.info(f'parsed args: {this.parser.parse_args()}')

        if MedicalDoctorModel.find_by_id(id):
            return {'message': "An medical_doctor with name '{}' already exists.".format(
                id)}, 400
        data = this.parser.parse_args()
        medical_doctor = MedicalDoctorModel(data['id'], data['name'], data['password'])

        try:
            medical_doctor.save_to_db()
        except:
            return {"message": "An error occurred inserting the medical_doctor."}, 500
        return medical_doctor.json(), 201

    #@jwt_required()
    def delete(self, id):

        medical_doctor = MedicalDoctorModel.find_by_id(id)
        if medical_doctor:
            medical_doctor.delete_from_db()

            return {'message': 'medical_doctor has been deleted'}

    #@jwt_required()
    def put(self, id):
        # Create or Update
        data = this.parser.parse_args()
        medical_doctor = MedicalDoctorModel.find_by_id(id)

        if medical_doctor is None:
            medical_doctor = MedicalDoctorModel(id, data['name'], data['password'])
        else:
            if date['name'] is not None: user.name = data['name']
            if date['password'] is not None: user.password = data['password']

        medical_doctor.save_to_db()

        return medical_doctor.json()


class MedicalDoctorList(Resource):
    #@jwt_required()
    def get(self):
        return {
            'medical_doctors': [medical_doctor.json() for medical_doctor in MedicalDoctorModel.query.all()]}  # More pythonic
        ##return {'medical_doctors': list(map(lambda x: x.json(), MedicalDoctorModel.query.all()))} #Alternate Lambda way
