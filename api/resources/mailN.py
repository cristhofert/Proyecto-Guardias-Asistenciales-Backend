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
        # print(email)
        try:
            sg = sendgrid.SendGridAPIClient(
                api_key='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')
            from_email = Email("federicoDn3@gmail.com")
            to_email = To(email)
            # to_email = To("@") Esto en caso de prueba
            subject = "Bienvenido a GuardiasMedicas"
            content = Content("text/plain", "Bienvenido")
            mail = Mail(from_email, to_email, subject, content)
            """print(mail)
            response = sg.send(mail)
            print(response.status_code)
            print(response.body)
            print(response.headers) """

        except:
            return {"message": "An error occurred sending mail."}, 500
        return 201
