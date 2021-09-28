from db import db
from sqlalchemy.orm import relationship

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
    medical_doctor = relationship('MedicalDoctorModel')
    medical_doctor_id = db.Column(db.Integer, db.ForeignKey('medical_doctor.id'))
    #subscription = db.relationship('SubscriptionModel', lazy='dynamic')
    #subscription_id = db.Column(db.Integer, db.ForeignKey('subscriptions.id'))
    
    def __init__(self, service, date, start_time, end_time, zone=None):
        self.service = service
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        if zone:
            self.zone = zone
            
    def json(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'assigned_at': self.assigned_at,
            'service_id': self.service_id
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
        