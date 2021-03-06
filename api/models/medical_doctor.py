from db import db
from models.user import UserModel
from models.subscription import subscription_medical_doctor_table
from util.query import QueryWithSoftDelete

class MedicalDoctorModel(UserModel):
    __tablename__ = 'medical_doctor'

    id = db.Column(db.String(80), db.ForeignKey('user.id'), primary_key=True)
    speciality = db.Column(db.String(80))
    phone = db.Column(db.String(9), db.CheckConstraint('phone LIKE \'%09%\''))
    email = db.Column(db.String(80))
    subscriptions =db.relationship(
        'SubscriptionModel', secondary=subscription_medical_doctor_table, back_populates='medical_doctors')
    assignments =db.relationship('AssignmentModel', back_populates='medical_doctor')
    guards = db.relationship('GuardModel', backref='medical_doctor', lazy=True)
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'))
    zone = db.relationship('ZoneModel', backref='medical_doctors')

    query_class = QueryWithSoftDelete
    
    __mapper_args__ = {
        'polymorphic_identity': 'medical_doctor'
    }

    def __init__(self,  id, name, password, speciality, phone, email, zone_id, institution_id=1):
        super().__init__(id, name, password, 'medical_doctor', institution_id)
        self.speciality = speciality
        self.phone = phone
        self.email = email
        self.zone_id = zone_id

    def json(self):
        return {
            'id': self.id, 
            'name': self.name, 
            'password': self.password,
            'speciality': self.speciality, 
            'phone': self.phone, 
            'email': self.email,
            'institution': self.institution_id,
            'zone': self.zone.json() if self.zone else None,
            'subscriptions': [subscription.json()['id'] for subscription in self.subscriptions]
            }

    def get_id(self):
        return self.id

    def assignments_json(self):
        return [assignment.json() for assignment in self.assignments]
        
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        self.deleted = True
        db.session.commit()
