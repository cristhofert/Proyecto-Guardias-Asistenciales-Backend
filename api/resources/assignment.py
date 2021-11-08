#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from util.notifications import Notificaciones
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
from models.medical_doctor import MedicalDoctorModel
from models.assignment import AssignmentModel
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

    @jwt_required()
    def post(self, medical_doctor_id, guard_id):
        medical_doctor = MedicalDoctorModel.find_by_id(medical_doctor_id)
        guard = GuardModel.find_by_id(guard_id)
        if medical_doctor and guard and (medical_doctor.json()['institution'] == current_user.json()['institution']) and (guard.json()['institution'] == current_user.json()['institution']):
            assignment = AssignmentModel(
                medical_doctor_id, guard_id, current_user.json()['institution'])
            guard.medical_doctor_id = medical_doctor_id

            try:
                assignment.save_to_db()
                guard.save_to_db()
            except:
                return {"message": "An error occurred inserting the assignment."}, 500
        return assignment.json(), 201

    @jwt_required()
    def delete(self, medical_doctor_id, guard_id):
        assignment = AssignmentModel.find_by_ids(medical_doctor_id, guard_id)
        guard = GuardModel.find_by_id(guard_id)
        if assignment and (assignment.json()['institution'] == current_user.json()['institution']):
            assignment.delete_from_db()
            guard.medical_doctor_id = None
            md = MedicalDoctorModel.find_by_id(medical_doctor_id)
            email = md.email
            telefono = 'whatsapp:+598'+md.phone
            message = "Guardia Liberada"
            print(email)
            print(telefono)
            Notificaciones(email, telefono, medical_doctor_id,
                           guard_id, message)
            return {'message': 'Assignment deleted'}
        return {'message': 'Assignment not found'}, 404

    @jwt_required()
    def get(self, medical_doctor_id=0, guard_id=0):
        if current_user.type == 'medical_doctor':
            return {"message": "You are not authorized to access this resource."}, 401

        if medical_doctor_id > 0:
            assignment = AssignmentModel.find_by_medical_doctor_id(
                medical_doctor_id)
            if assignment and (assignment.json()['institution'] == current_user.json()['institution']):
                return assignment.json(), 200
            return {"message": "Medical doctor not found."}, 404

        if guard_id > 0:
            assignment = AssignmentModel.find_by_guard_id(guard_id)
            if assignment and (assignment.json()['institution'] == current_user.json()['institution']):
                return assignment.json(), 200
            return {"message": "Medical doctor not found."}, 404

        return {"message": "Not found."}, 404
