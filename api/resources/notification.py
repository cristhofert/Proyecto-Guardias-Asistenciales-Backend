#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse, inputs, fields
from flask_jwt_extended import jwt_required, current_user
from models.notification import NotificationModel
#from app.util.logz import create_logger
import calendar
from datetime import datetime
from pprint import pprint


class Notification(Resource):
    @jwt_required()
    def get(self):
        if current_user.type == 'medical_doctor':
            notifications = NotificationModel.find_by_user_id(current_user.id)
            return [notification.json() for notification in notifications], 201
        return {"message": "You are not authorized to access this resource."}, 401