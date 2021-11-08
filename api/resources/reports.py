#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import jwt_required, current_user
from models.medical_doctor import MedicalDoctorModel
from models.assignment import AssignmentModel


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
        report = {'average assignment': []}
        for medical_doctor in MedicalDoctorModel.query.filter_by(institution_id=current_user.json()['institution']).all():
            guards = []
            for guard in medical_doctor.guards:
                dt = AssignmentModel.find_by_ids(medical_doctor.get_id(
                ), guard.get_id()).get_assignment_date() - guard.get_created_at()
                guards.append(
                    {**guard.json(), 'hours': dt.total_seconds() / 60 / 60})
            report['a'].append({**medical_doctor.json(), 'guards': guards})

        return report, 200
