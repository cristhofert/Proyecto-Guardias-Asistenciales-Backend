from db import db
from pprint import pprint
from util.query import QueryWithSoftDelete

subscription_medical_doctor_table = db.Table('subscription_medical_doctor_table', db.Model.metadata,
                                             db.Column('subscription_id', db.ForeignKey(
                                                 'subscriptions.id'), primary_key=True),
                                             db.Column('medical_doctor_id', db.ForeignKey(
                                                 'medical_doctor.id'), primary_key=True)
                                             )

class SubscriptionModel(db.Model):
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(11), db.CheckConstraint('type in ("dispersión", "lista")'))	
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    service = db.relationship('ServiceModel', backref='subscriptions')
    medical_doctors =db.relationship(
        'MedicalDoctorModel', secondary=subscription_medical_doctor_table, back_populates='subscriptions')
    guards = db.relationship('GuardModel', back_populates='subscription')
    institution_id = db.Column(db.Integer, db.ForeignKey(
        'institutions.id'), nullable=False, default=1)
    institution = db.relationship("InstitutionModel")
    deleted = db.Column(db.Boolean(), default=False)

    query_class = QueryWithSoftDelete
    
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
            'name': self.service.json()['name'] + ' - ' + self.type,
            'institution': self.institution_id
        }

    def guards_json(self):
        return [guard.json() for guard in self.guards]
    
    def disponible_guards_json(self):
        guards = []
        for guard in self.guards:
            if guard.is_disponible():
                guards.append(guard.json())
        return guards

    def medical_doctors_get(self):
        return [md for md in self.medical_doctors]

    @classmethod
    def find_by_service_id_type(cls, _service_id, _type):
        return cls.query.filter_by(service_id=_service_id, type=_type).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):  # Upserting data
        db.session.add(self)
        db.session.commit()  # Balla

    def delete_from_db(self):
        self.deleted = True
        db.session.commit()
