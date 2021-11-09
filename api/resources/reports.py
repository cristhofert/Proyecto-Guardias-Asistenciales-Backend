#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import jwt_required, current_user
from models.medical_doctor import MedicalDoctorModel
from models.assignment import AssignmentModel
from models.service import ServiceModel


class Reports(Resource):
    def __init__(self):
        pass

    parser = reqparse.RequestParser()

    @jwt_required()
    def get(self):
        # if current_user.type == 'medical_doctor':
        #    return {'message': 'You are not allowed to the reports'}, 401
        """
        {
            medical_doctor_id: 12345,
            hours: 000 #tiempo promdedio en aceptar las guardias
        }
        """
        average_assignment = []
        for medical_doctor in MedicalDoctorModel.query.filter_by(institution_id=current_user.json()['institution']).all():
            guards = []
            for guard in medical_doctor.guards:
                assignment = AssignmentModel.find_by_ids(medical_doctor.get_id(
                ), guard.get_id())
                if assignment:
                    dt = assignment.get_assignment_date() - guard.get_created_at()
                    guards.append(
                        {**guard.json(), 'hours': dt.total_seconds() / 60 / 60})
            average_assignment.append(
                {**medical_doctor.json(), 'count': len(guards), 'guards': guards})

        services = []
        for service in ServiceModel.query.filter_by(institution_id=current_user.json()['institution']).all():
            medical_doctors_id = []
            medical_doctors = []
            for guards in [subscription.guards_json() for subscription in service.get_subscriptions()]:
                for guard in guards:
                    medical_doctors_id.append(guard['medical_doctor_id'])

            for _id in set(medical_doctors_id):
                m = MedicalDoctorModel.find_by_id(_id)
                if m:
                    medical_doctors.append(m.json())

            services.append({**service.json(), 'medical_doctors': medical_doctors})

        return {'average_assignment': average_assignment, 'services': services}, 200
