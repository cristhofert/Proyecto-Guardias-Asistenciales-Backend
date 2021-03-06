#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import mariadbConfig
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt, set_access_cookies
import json
from datetime import timedelta, datetime, timezone
from resources.administrator import Administrator, AdministratorList
from resources.guard import Guard, GuardList
from resources.medical_doctor import MedicalDoctor, MedicalDoctorList
from resources.service import Service, ServiceList
from resources.subscription import Subscription, SubscriptionList
from resources.zone import Zone, ZoneList
from resources.assignment import Assignment
from resources.login import Login
from resources.password import Password
from resources.subscribe import Subscribe
from resources.mailN import MailN
from resources.superadmin import SuperAdmin
from resources.myguards import MyGuards
from resources.reports import Reports
from resources.guards_group import GuardsGroup, GuardsGroupList
from resources.notification import Notification
from models.user import UserModel
from models.institution import InstitutionModel
from util.preset import preset_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = mariadbConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "secret#jwt#g1"
jwt = JWTManager(app)
#CORS(app)# CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
api = Api(app)

@app.before_first_request
def create_tables():
    from db import db
    db.init_app(app)
    db.drop_all()
    db.create_all()
    preset_db()
# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring. Change the timedeltas to match the needs of your application.
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

# Register a callback function that loades a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UserModel.query.filter_by(id=identity).one_or_none()

api.add_resource(Administrator, '/administrator/<int:id>')
api.add_resource(AdministratorList, '/administrators') 
api.add_resource(Guard, '/guard/<int:id>')
api.add_resource(GuardList, '/guards')
api.add_resource(MedicalDoctor, '/medical_doctor/<string:id>')
api.add_resource(MedicalDoctorList, '/medical_doctors')
api.add_resource(Service, '/service/<int:id>')
api.add_resource(ServiceList, '/services')
api.add_resource(Subscription, '/subscription/<int:id>')
api.add_resource(SubscriptionList, '/subscriptions')
api.add_resource(Zone, '/zone/<int:id>')
api.add_resource(ZoneList, '/zones')
api.add_resource(Assignment, '/assignment/<int:medical_doctor_id>/<int:guard_id>')
api.add_resource(Login, '/login')
api.add_resource(Password, '/password/<string:token>')
api.add_resource(Subscribe, '/subscribe/<int:medical_doctor_id>/<int:subscription_id>')
api.add_resource(MailN, '/MailN')
api.add_resource(SuperAdmin, '/superadmin/<int:id>')
api.add_resource(MyGuards, '/myguards/')
api.add_resource(Reports, '/reports')
api.add_resource(GuardsGroup, '/group/<int:id>')
api.add_resource(GuardsGroupList, '/groups')
api.add_resource(Notification, '/notifications')

if __name__ == "__main__":
    app.run(debug=True)