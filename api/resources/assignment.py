#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from models.medical_doctor import MedicalDoctorModel
from models.guard import GuardModel

class Assignment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('medical_doctor_id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('guard_id',
        type=False,
        required=True,
        help="This field cannot be left blank!"
    )

    def __init__(self):
        pass

    def post(self, medical_doctor_id, guard_id):

        medical_doctor = MedicalDoctorModel.find_by_id(medical_doctor_id)
        guard = GuardModel.find_by_id(guard_id)
        if medical_doctor and guard:
            medical_doctor.assignment.append(guard)

            try:
                medical_doctor.save_to_db()
                guard.save_to_db()
            except:
                return {"message": "An error occurred inserting the medical_doctor."}, 500
        return medical_doctor.json(), 201

    def delete(self, medical_doctor_id, guard_id):
        medical_doctor = MedicalDoctorModel.find_by_id(medical_doctor_id)
        guard = GuardModel.find_by_id(guard_id)

        if medical_doctor and guard:
            medical_doctor.assignment.remove(guard)

            try:
                medical_doctor.save_to_db()
                guard.save_to_db()
            except:
                return {"message": "An error occurred inserting the medical_doctor."}, 500
        return medical_doctor.json(), 201