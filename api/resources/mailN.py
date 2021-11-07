#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask import app, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import current_user
from models.user import UserModel
from util.encoder import AlchemyEncoder
import json
from util.logz import create_logger
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
import sendgrid


class MailN(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        #self.logger = create_logger()
        pass

    def post(self):

        data = self.parser.parse_args()
        email = data['email']
        mail = Mail()
        mail.from_email = Email("federicoDn3@gmail.com", "Guardias Medicas")
        #to_email = To(email)
        # Esto en caso de prueba
        mail.to = To("federico.diaz@utec.edu.uy")
        mail.subject = "Bienvenido a Guardias Medicas"
        mail.template_id = TemplateId("d-ab9d3a52dc724b17a143c51ab1d55511")

        try:
            sg = sendgrid.SendGridAPIClient(
                api_key='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')
            response = sg.send(mail)
            # print(mail)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except:
            return {"message": "An error occurred sending mail."}, 500
        return response._status_code
