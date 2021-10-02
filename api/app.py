#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import mariadbConfig

from resources.administrator import Administrator, AdministratorList
from resources.audit import Audit, AuditList
from resources.guard import Guard, GuardList
from resources.medical_doctor import MedicalDoctor, MedicalDoctorList
from resources.notification import Notification, NotificationList
from resources.service import Service, ServiceList
from resources.subscription import Subscription, SubscriptionList
from resources.zone import Zone, ZoneList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = mariadbConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
CORS(api)# CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})

@app.before_first_request
def create_tables():
    from db import db
    db.init_app(app)
    #db.drop_all()
    db.create_all()

api.add_resource(Administrator, '/administrator/<int:id>')
api.add_resource(AdministratorList, '/administrators')
api.add_resource(Audit, '/audit/<int:id>')
api.add_resource(AuditList, '/audits')   
api.add_resource(Guard, '/guard/<int:id>')
api.add_resource(GuardList, '/guards')
api.add_resource(MedicalDoctor, '/medical_doctor/<int:id>')
api.add_resource(MedicalDoctorList, '/medical_doctors')
api.add_resource(Notification, '/notification/<int:id>')
api.add_resource(NotificationList, '/notifications')
api.add_resource(Service, '/service/<int:id>')
api.add_resource(ServiceList, '/services')
api.add_resource(Subscription, '/subscription/<int:id>')
api.add_resource(SubscriptionList, '/subscriptions')
api.add_resource(Zone, '/zone/<string:name>')
api.add_resource(ZoneList, '/zones')

if __name__ == "__main__":
    app.run(debug=True)