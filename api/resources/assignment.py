#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from util.notifications import Notificaciones
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
from models.medical_doctor import MedicalDoctorModel
from models.assignment import AssignmentModel
from models.guard import GuardModel
from util import access
from util.is_empty import is_empty

class Assignment(Resource):

    def __init__(self):
        pass

    @jwt_required()
    def post(self, medical_doctor_id, guard_id):
        if current_user.type == 'medical_doctor':
            medical_doctor = current_user
            medical_doctor_id = medical_doctor.get_id()
        else: 
            medical_doctor = MedicalDoctorModel.find_by_id(medical_doctor_id)
        guard = GuardModel.find_by_id(guard_id)
        if medical_doctor:
            if guard:
                if (medical_doctor.json()['institution'] == current_user.json()['institution']) and (guard.json()['institution'] == current_user.json()['institution']):
                    if (guard.json()['lock'] == False):
                        assignment = AssignmentModel(
                            medical_doctor_id, guard_id, current_user.json()['institution'])
                        guard.medical_doctor_id = medical_doctor_id
                        guard.lock = True

                        try:
                            assignment.save_to_db()
                            guard.save_to_db()
                        except BaseException as err:
                            return {"message": f"An error occurred inserting the assignment. {err}"}, 500
                        return assignment.json(), 201
                    return {"message": "It's lock"}, 500
                return {"message": "Incorrect Institution"}, 500
            return {"message": "Guard not exist"}, 500
        return {"message": "Medical Doctor not exist"}, 500

    @jwt_required()
    def delete(self, medical_doctor_id, guard_id):
        if current_user.type == 'medical_doctor':
            medical_doctor = current_user
            medical_doctor_id = medical_doctor.get_id()
        else: 
            medical_doctor = MedicalDoctorModel.find_by_id(medical_doctor_id)
        assignment = AssignmentModel.find_by_ids(medical_doctor_id, guard_id)
        guard = GuardModel.find_by_id(guard_id)
        if assignment and (assignment.json()['institution'] == current_user.json()['institution']):
            assignment.delete_from_db()
            guard.medical_doctor_id = None
            guard.lock = False
            email = medical_doctor.email
            telefono = 'whatsapp:+598'+medical_doctor.phone.lstrip("0")
            message = "Guardia Liberada"
            Notificaciones(email, telefono, medical_doctor_id,
                           guard_id, message)
            return {'message': 'Assignment deleted'}
        return {'message': 'Assignment not found'}, 404

    @jwt_required()
    def get(self, medical_doctor_id=0, guard_id=0):
        access.medical_doctor()

        if medical_doctor_id > 0:
            assignment = AssignmentModel.find_by_medical_doctor_id(
                medical_doctor_id)
            if assignment and (assignment.json()['institution'] == current_user.json()['institution']):
                return assignment.json(), 201
            return {"message": "Medical doctor not found."}, 404

        if guard_id > 0:
            assignment = AssignmentModel.find_by_guard_id(guard_id)
            if assignment and (assignment.json()['institution'] == current_user.json()['institution']):
                return assignment.json(), 201
            return {"message": "Medical doctor not found."}, 404

        return {"message": "Not found."}, 404
