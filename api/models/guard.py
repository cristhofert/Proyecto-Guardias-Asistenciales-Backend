from db import db
from sqlalchemy.orm import relationship
from pprint import pprint
from datetime import datetime

assignment_table = db.Table('assignment', db.Model.metadata,
    db.Column('guard_id', db.ForeignKey('guard.id'), primary_key=True),
    db.Column('medical_doctor_id', db.ForeignKey('medical_doctor.id'), primary_key=True),
    db.Column('assignment_date', db.DateTime, default=db.func.current_timestamp())
)

class GuardModel(db.Model):
    __tablename__ = 'guard'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'))
    zone = relationship('ZoneModel')#?
    medical_doctor = relationship('MedicalDoctorModel', secondary=assignment_table, back_populates='assignment')
    medical_doctor_id = db.Column(db.Integer, db.ForeignKey('medical_doctor.id'))
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscriptions.id'))
    subscription = db.relationship('SubscriptionModel')
    
    def __init__(self, subscription_id, date, start_time, end_time, zone_id=None):
        self.subscription_id = subscription_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
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
            'start': (self.date.strftime('%Y-%m-%d') + " " + self.start_time.strftime('%H:%M')),
            'end': (self.date.strftime('%Y-%m-%d') + " " + self.end_time.strftime('%H:%M')),
            'subscription': self.subscription.json()
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        