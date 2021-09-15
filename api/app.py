#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask import Flask
from flask_restful import Api
from config import mariadbConfig

from resources.user import User, UserList
from resources.administrator import Administrator, AdministratorList
from resources.guard import Guard, GuardList
from resources.medical_doctor import MedicalDoctor, MedicalDoctorList
from resources.service import Service, ServiceList
from resources.zone import Zone, ZoneList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = mariadbConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request
def create_tables():
    from db import db
    db.init_app(app)
    db.create_all()

api.add_resource(User, '/user/<int:id>')
api.add_resource(UserList, '/users')
api.add_resource(Administrator, '/administrator/<int:id>')
api.add_resource(AdministratorList, '/administrators')
api.add_resource(Guard, '/guard/<int:id>')
api.add_resource(GuardList, '/guards')
api.add_resource(MedicalDoctor, '/medicaldoctor/<int:id>')
api.add_resource(MedicalDoctorList, '/medicaldoctors')
api.add_resource(Service, '/service/<string:name>')
api.add_resource(ServiceList, '/services')
api.add_resource(Zone, '/zone/<int:id>')
api.add_resource(ZoneList, '/zones')

if __name__ == "__main__":
    app.run(debug=True)