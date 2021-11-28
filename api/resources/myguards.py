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
        if current_user.type == 'administrator':
            return {"message": "You are not authorized to access this resource."}, 401
        return {
            'myguards': [guard.json() for guard in current_user.guards]
        }, 201
