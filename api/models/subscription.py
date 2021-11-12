from db import db
from sqlalchemy.orm import relationship
from pprint import pprint

subscription_medical_doctor_table = db.Table('subscription_medical_doctor_table', db.Model.metadata,
                                             db.Column('subscription_id', db.ForeignKey(
                                                 'subscriptions.id'), primary_key=True),
                                             db.Column('medical_doctor_id', db.ForeignKey(
                                                 'medical_doctor.id'), primary_key=True)
                                             )

class SubscriptionModel(db.Model):
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80))
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    service = db.relationship('ServiceModel', backref='subscriptions')
    medical_doctors = relationship(
        'MedicalDoctorModel', secondary=subscription_medical_doctor_table, back_populates='subscriptions')
    guards = db.relationship('GuardModel', back_populates='subscription')
    institution_id = db.Column(db.Integer, db.ForeignKey(
        'institutions.id'), nullable=False, default=1)
    institution = db.relationship("InstitutionModel")

    def __init__(self, type, service_id, institution_id=1):
        self.type = type
        self.service_id = service_id
        self.institution_id = institution_id

    def json(self):
        return {
            'id': self.id,
            'type': self.type,
            'service_id': self.service_id,
            'service': self.service.json(),
            'name': self.service.json()['name'] + ' - ' + self.type
        }

    def guards_json(self):
        return [guard.json() for guard in self.guards]
    
    def disponible_guards_json(self):
        guards = []
        for guard in self.guards:
            if guard.is_disponible():
                guards.append(guard.json())
        return guards

    @classmethod
    def find_by_channel_id(cls, channel_id):
        return cls.query.filter_by(channel_id=channel_id).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):  # Upserting data
        db.session.add(self)
        db.session.commit()  # Balla

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
