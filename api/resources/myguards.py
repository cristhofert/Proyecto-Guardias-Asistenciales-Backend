#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse, inputs, fields
from flask_jwt_extended import jwt_required, current_user
from models.guard import GuardModel
from models.guards_group import GuardsGroupModel
from models.assignment import AssignmentModel
#from app.util.logz import create_logger
import calendar
from datetime import datetime
from pprint import pprint

class MyGuards(Resource):
    @jwt_required()
    def get(self):
        return {
            'myguards': [x.json() for x in AssignmentModel.find_by_medical_doctor_id(current_user.id)]
            }