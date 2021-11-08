from db import db
from models.user import UserModel
from models.subscription import subscription_medical_doctor_table
from sqlalchemy.orm import relationship

class MedicalDoctorModel(UserModel):
    __tablename__ = 'medical_doctor'

    id = db.Column(db.String(80), db.ForeignKey('user.id'), primary_key=True)
    speciality = db.Column(db.String(80))
    phone = db.Column(db.String(9))
    email = db.Column(db.String(80))
    residence_zone = db.Column(db.Integer, db.ForeignKey('zone.id'),
                               nullable=True)
    #zones = db.relationship('ZoneModel', back_populates='medical_doctors')
    subscriptions = relationship(
        'SubscriptionModel', secondary=subscription_medical_doctor_table, back_populates='medical_doctors')
    assignments = relationship('AssignmentModel', back_populates='medical_doctor')
    guards = db.relationship('GuardModel', backref='medical_doctor', lazy=True)
    __mapper_args__ = {
        'polymorphic_identity': 'medical_doctor'
    }

    def __init__(self,  id, name, password, speciality, phone, email, institution_id=1):
        super().__init__(id, name, password, 'medical_doctor', institution_id)
        self.speciality = speciality
        self.phone = phone
        self.email = email

    def json(self):
        return {
            'id': self.id, 
            'name': self.name, 
            'speciality': self.speciality, 
            'phone': self.phone, 
            'email': self.email,
            'institution': self.institution_id
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
        db.session.delete(self)
        db.session.commit()
