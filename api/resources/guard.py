#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse, inputs
#from flask_jwt_extended import jwt_required
from models.guard import GuardModel
#from app.util.logz import create_logger
import calendar
from datetime import datetime

class Guard(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('service_id',
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
        type=inputs.time,#Time
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('end_time',
        type=inputs.time,#Time
        required=True,
        help="This field cannot be left blank!"
    )

    def __init__(self):
        pass
        ##self.logger = create_logger()

    #@jwt_required()  # Requires dat token
    def get(self, id):
        guard = GuardModel.find_by_id(id)
        #self.logger.info(f'returning guard: {guard.json()}')
        if guard:
            return guard.json()
        return {'message': 'this not found'}, 404

    #@jwt_required()
    def post(self, id):
        #self.logger.info(f'parsed args: {this.parser.parse_args()}')

        if GuardModel.find_by_id(id):
            return {'message': "An guard with id '{}' already exists.".format(
                id)}, 400
        data = this.parser.parse_args()
        self.logger.info(f'parsed args: {data}')
        guard = GuardModel(data['service'], data['date'], data['start_time'], date['end_time'], data['zone'])

        try:
            guard.save_to_db()
        except:
            return {"message": "An error occurred inserting the guard."}, 500
        return guard.json(), 201

    #@jwt_required()
    def delete(self, id):

        guard = GuardModel.find_by_id(id)
        if guard:
            guard.delete_from_db()

            return {'message': 'guard has been deleted'}

    #@jwt_required()
    def put(self, id):
        # Create or Update
        data = this.parser.parse_args()
        guard = GuardModel.find_by_id(id)

        if guard is None:
            return {'message': 'guard not exist'}, 500
        else:
            if data['service'] is not None: guard.service = data['service']
            if data['zone'] is not None: guard.zone = data['zone']

        guard.save_to_db()

        return guard.json()

class GuardList(Resource):
    #@jwt_required()
    def get(self):
        return {
            'guards': [guard.json() for guard in GuardModel.query.all()]}  # More pythonic

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
                                guards.append(GuardModel(data['service'], date_guard, data['start_time'], date['end_time'], data['zone']))
                                #pued e que falte guardar cada guardia

        group = GuardsGroupModel(0, guards)

        try:
            group.save_to_db()
        except:
            return {"message": "An error occurred inserting the guard."}, 500
        return guard.json(), 201