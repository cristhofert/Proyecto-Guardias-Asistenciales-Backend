#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse, inputs, fields
from flask_jwt_extended import jwt_required, current_user
from models.guard import GuardModel
from models.guards_group import GuardsGroupModel
#from app.util.logz import create_logger
import calendar
from datetime import datetime

class Guard(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('subscription_id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('zone_id',
        type=int,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('date',
        type=inputs.date,#input date
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('start_time',
        type=str,#Time
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('end_time',
        type=str,#Time
        required=True,
        help="This field cannot be left blank!"
    )

    def __init__(self):
        pass
        ##self.logger = create_logger()

    @jwt_required()  # Requires dat token
    def get(self, id):
        guard = GuardModel.find_by_id(id)
        #self.logger.info(f'returning guard: {guard.json()}')
        if guard and (guard.json()['institution'] == current_user.json()['institution']):
            return guard.json()
        return {'message': 'this not found'}, 404

    @jwt_required()
    def post(self, id):
        #self.logger.info(f'parsed args: {self.parser.parse_args()}')
        data = self.parser.parse_args()

        #self.logger.info(f'parsed args: {data}')
        guard = GuardModel(data['subscription_id'], data['date'], data['start_time'], data['end_time'], data['zone_id'], current_user.json()['institution'])

        try:
            guard.save_to_db()
        except:
            return {"message": "An error occurred inserting the guard."}, 500
        return guard.json(), 201

    @jwt_required()
    def delete(self, id):

        guard = GuardModel.find_by_id(id)
        if guard and (guard.json()['institution'] == current_user.json()['institution']):
            guard.delete_from_db()

            return {'message': 'guard has been deleted'}

    @jwt_required()
    def put(self, id):
        # Create or Update
        data = self.parser.parse_args()
        guard = GuardModel.find_by_id(data['id'])

        if guard.json()['institution'] == current_user.json()['institution']:
            if guard is None:
                return {'message': 'guard not exist'}, 500
            else:
                if data['subscription_id'] is not None: guard.subscription_id = data['subscription_id']
                if data['zone_id'] is not None: guard.zone_id = data['zone_id']
                if data['date'] is not None: guard.date = data['date']
                if data['start_time'] is not None: guard.start_time = data['start_time']
                if data['end_time'] is not None: guard.end_time = data['end_time']

            guard.save_to_db()

            return guard.json()
        else:
            return {'message': 'access denied'}, 401

class GuardList(Resource):
    @jwt_required()
    def get(self):
        return {
            'guards': [guard.json() for guard in GuardModel.query.filter_by(institution_id=current_user.json()['institution']).all()]}  # More pythonic

    @jwt_required()
    def post(self):
        guards = []
        today = date.today()
        for tuple in calendar.Calendar().monthdays2calendar(today.year, today.month):
            for week in tuple:
                day, weekday = week
                if(day != 0):
                    for wday in data['repeat']:
                        if wday == calendar.day_name[weekday]:
                            date_guard = date(today.year, today.month, day)
                            if date_guard > today:
                                guards.append(GuardModel(data['subscription_id'], date_guard, data['start_time'], date['end_time'], data['zone_id'], current_user.json()['institution']))
                                #puede que falte guardar cada guardia

        group = GuardsGroupModel(0, guards, current_user.json()['institution'])

        try:
            group.save_to_db()
        except:
            return {"message": "An error occurred inserting the guard."}, 500
        return guard.json(), 201