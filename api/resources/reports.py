#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import jwt_required, current_user
from models.medical_doctor import MedicalDoctorModel
from models.assignment import AssignmentModel
from models.service import ServiceModel
import datetime

class Reports(Resource):
    def __init__(self):
        pass

    parser = reqparse.RequestParser()
    parser.add_argument('month',
        type=int,
        help='This field cannot be left blank')
    parser.add_argument('year',
        type=int,
        help='This field cannot be left blank')

    @jwt_required()
    def get(self):
        data = self.parser.parse_args()
        today = datetime.date.today()
        if data['year'] > today.year:
            return {'message': 'Invalid future year'}, 400
        if data['year'] == today.year and data['month'] > today.month:
            return {'message': 'Invalid future month'}, 400
        average_assignment = []
        for medical_doctor in MedicalDoctorModel.query.filter_by(institution_id=current_user.json()['institution']).all():
            guards = []
            avg = 0
            for guard in medical_doctor.guards:
                assignment = AssignmentModel.find_by_ids(medical_doctor.get_id(
                ), guard.get_id())
                if assignment:
                    if assignment.get_assignment_date().month == data['month'] and assignment.get_assignment_date().year == data['year']:
                        dt = assignment.get_assignment_date() - guard.get_created_at()
                        guards.append(
                            {**guard.json(), 'hours': dt.total_seconds() / 60 / 60})
                        avg += dt.total_seconds() / 60 / 60
            if len(guards) > 0:
                avg = avg / len(guards)
            average_assignment.append(
                {**medical_doctor.json(), 'count': len(guards), 'avg':avg, 'guards': guards})

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

        return {'average_assignment': average_assignment, 'services': services}, 201
