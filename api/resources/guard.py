#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse, inputs, fields
from flask_jwt_extended import jwt_required, current_user
from util.notifications import Notificaciones
from util import access
from models.medical_doctor import MedicalDoctorModel
from models.subscription import SubscriptionModel
from models.guard import GuardModel
from models.guards_group import GuardsGroupModel
#from app.util.logz import create_logger
import calendar
from datetime import date

class Guard(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('subscription_id',
                        type=inputs.positive,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('zone_id',
                        type=inputs.positive,
                        required=False,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('date',
                        type=inputs.date,  # input date
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('start_time',
                        type=str,  # Time
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('end_time',
                        type=str,  # Time
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('quantity',
                        type=inputs.positive,
                        required=False,
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
            return guard.json(), 201
        return {'message': 'this not found'}, 404

    @jwt_required()
    def post(self, id):
        access.administor(current_user)
        #self.logger.info(f'parsed args: {self.parser.parse_args()}')
        data = self.parser.parse_args()

        #self.logger.info(f'parsed args: {data}')
        quantity = data['quantity'] if data['quantity'] and data['quantity'] > 0 and data['quantity'] < 50 else 1
        guards = []
        for i in range(quantity):
            guards.append(GuardModel(data['subscription_id'], data['date'], data['start_time'],
                          data['end_time'], data['zone_id'], current_user.json()['institution']))

        group = GuardsGroupModel(guards, current_user.json()['institution'])

        sm = SubscriptionModel.find_by_id(data['subscription_id'])
        ml = sm.medical_doctors_get()
        message = "Guardia Liberada"
        try:
            for g in guards:
                g.save_to_db()
                for m in ml:
                    print(m)
                    Notificaciones(m.email, 'whatsapp:+598' +
                                   m.phone.lstrip("0"), m.id, g.id, message)
            group.save_to_db()
        except BaseException as err:
            print(err)
            return {"message": "An error occurred inserting the guard.", "error": f'{err}'}, 500
        return group.json(), 201

    @jwt_required()
    def delete(self, id):
        access.administor(current_user)
        guard = GuardModel.find_by_id(id)
        if guard and (guard.json()['institution'] == current_user.json()['institution']):
            guard.delete_from_db()

            return {'message': 'guard has been deleted'}, 201
        return {'message': 'guard not found'}, 404

    @jwt_required()
    def put(self, id):
        access.administor(current_user)
        # Create or Update
        data = self.parser.parse_args()
        guard = GuardModel.find_by_id(id)

        if guard is None:
            return {'message': 'guard not exist'}, 500
        if guard.json()['institution'] == current_user.json()['institution']:
            if data['subscription_id'] is not None:
                guard.subscription_id = data['subscription_id']
            if data['zone_id'] is not None:
                guard.zone_id = data['zone_id']
            if data['date'] is not None:
                guard.date = data['date']
            if data['start_time'] is not None:
                guard.start_time = data['start_time']
            if data['end_time'] is not None:
                guard.end_time = data['end_time']

            guard.save_to_db()

            return guard.json(), 201
        else:
            return {'message': 'access denied'}, 401


class GuardList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('subscription_id',
                        type=inputs.positive,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('zone_id',
                        type=inputs.positive,
                        required=False,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('repeat',
                        type=str,
                        action='append',
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('start_time',
                        type=str,  # Time
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('end_time',
                        type=str,  # Time
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('quantity',
                        type=int,
                        required=False,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('date',
                        type=inputs.date,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()
    def get(self):
        if current_user.type == 'administrator':
            return {
                'guards': [guard.json() for guard in GuardModel.query.filter_by(institution_id=current_user.json()['institution']).all()]}, 201
        elif current_user.type == 'medical_doctor':
            guards = []
            for subscription in current_user.subscriptions:
                for guard in subscription.disponible_guards_json():
                    guards.append(guard)
            return {
                'guards': guards
            }, 201
        else:
            return {'message': 'access denied, you need be a medical_doctor or an administator'}, 401

    @jwt_required()
    def post(self):#mes actual
        access.administor(current_user)
        guards = []
        data = self.parser.parse_args()
        print(data['repeat'])
        today = date.today()
        start_date = data['date'].date()
        if start_date < today:
            return {'message': 'date must be today or future'}, 400
        for tuple in calendar.Calendar().monthdays2calendar(start_date.year, start_date.month):
            for week in tuple:
                day, weekday = week
                if(day > 0):
                    print(day, calendar.day_name[weekday])
                    for wday in data['repeat']:
                        if wday == calendar.day_name[weekday]:
                            print("Day: ", wday)
                            print("CDay: ", calendar.day_name[weekday])
                            date_guard = date(start_date.year, start_date.month, day)
                            print(date_guard, " ", today)
                            if date_guard > today:
                                quantity = data['quantity'] if data['quantity'] else 1
                                for i in range(quantity):
                                    guards.append(GuardModel(data['subscription_id'], date_guard, data['start_time'],
                                                             data['end_time'], data['zone_id'], current_user.json()['institution']))

        if guards == []:
            return {"message": f"No hay dias disponible en este mes {start_date.month} del {start_date.year}"}, 400
        group = GuardsGroupModel(guards, current_user.json()['institution'])
        sm = SubscriptionModel.find_by_id(data['subscription_id'])
        ml = sm.medical_doctors_get()
        message = "Guardia Liberada"
        try:
            for g in guards:
                g.save_to_db()
                for m in ml:
                    print(m)
                    Notificaciones(m.email, 'whatsapp:+598' +
                                   m.phone.lstrip("0"), m.id, g.id, message)
            group.save_to_db()
        except:
            return {"message": "An error occurred inserting the guard."}, 500
        return group.json(), 201
