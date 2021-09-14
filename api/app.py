#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask import Flask
from flask_restful import Api
from config import mariadbConfig

from resources.service import Service, ServiceList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = mariadbConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request
def create_tables():
    from db import db
    db.init_app(app)
    db.create_all()

api.add_resource(Service, '/service/<string:name>')
api.add_resource(ServiceList, '/services')

if __name__ == "__main__":
    app.run(debug=True)