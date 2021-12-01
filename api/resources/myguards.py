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
from util import access

class MyGuards(Resource):
    @jwt_required()
    def get(self):
        access.medical_doctor(current_user)
        return {
            'myguards': [guard.json() for guard in current_user.guards]
        }, 201
