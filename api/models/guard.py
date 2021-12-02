from db import db
from pprint import pprint
from datetime import datetime
from models.assignment import AssignmentModel
from util.query import QueryWithSoftDelete

class GuardModel(db.Model):
    __tablename__ = 'guard'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'))
    zone = db.relationship('ZoneModel')  # ?
    lock = db.Column(db.Boolean(), default=False)
    assignments = db.relationship(
        'AssignmentModel', back_populates='guard', primaryjoin=id == AssignmentModel.guard_id, lazy=True)
    medical_doctor_id = db.Column(
        db.String(80), db.ForeignKey('medical_doctor.id'))
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscriptions.id'))
    subscription = db.relationship(
        'SubscriptionModel', back_populates='guards')
    group_id = db.Column(db.Integer, db.ForeignKey(
        'guards_group.id'), default=1)
    institution_id = db.Column(db.Integer, db.ForeignKey(
        'institutions.id'), nullable=False, default=1)
    institution = db.relationship("InstitutionModel")
    deleted = db.Column(db.Boolean(), default=False)
    
    query_class = QueryWithSoftDelete

    def __init__(self, subscription_id, date, start_time, end_time, zone_id=None, institution_id=1):
        self.subscription_id = subscription_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.institution_id = institution_id
        if zone_id:
            self.zone_id = zone_id

    def json(self):
        return {
            'id': self.id,
            'created_at': str(self.created_at.strftime('%Y-%m-%d %H:%M:%S')),
            'updated_at': str(self.updated_at.strftime('%Y-%m-%d %H:%M:%S')),
            'date': str(self.date.strftime('%Y-%m-%d')),
            'start_time': str(self.start_time.strftime('%H:%M')),
            'end_time': str(self.end_time.strftime('%H:%M')),
            'zone': self.zone.json() if self.zone else None,
            'lock': self.lock,
            'start': (self.date.strftime('%Y-%m-%d') + " " + self.start_time.strftime('%H:%M')),
            'end': (self.date.strftime('%Y-%m-%d') + " " + self.end_time.strftime('%H:%M')),
            'subscription_name': self.subscription.json()['name'] if self.subscription else None,
            'subscription_id': self.subscription_id,
            'medical_doctor_id': self.medical_doctor_id if self.medical_doctor_id else None,
            'institution': self.institution_id
        }

    def is_disponible(self):
        return False if self.medical_doctor_id else True

    def assignment_date(self):
        # traer assisgment con esta guardia y medical docotor id y ver su fecha
        return self.created_at  # fecha de asignacion

    def get_created_at(self):
        return self.created_at

    def get_id(self):
        return self.id

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        self.deleted = True
        db.session.commit()
