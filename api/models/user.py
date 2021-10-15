#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from db import db
from werkzeug.security import hmac

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)# Cedula de Identidad de Uruguay
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    type = db.Column(db.String(80))
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id'), nullable=False)
    institution = db.relationship("InstitutionModel")

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type,
        'with_polymorphic': '*'
    }

    def __init__(self, id, name, password, type, institution_id):
        self.id = id
        self.name = name
        self.password = password
        self.type = type
        self.institution_id = institution_id

    def json(self):
        return {
            'id': self.id, 
            'name': self.name,
            'institution': self.institution_id
        }   

    def check_password(self, password):
        return hmac.compare_digest(self.password, password)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()