from db import db
from models.user import UserModel
from models.subscription import subscription_medical_doctor_table
from models.guard import assignment_table
from sqlalchemy.orm import relationship

class MedicalDoctorModel(UserModel):
    __tablename__ = 'medical_doctor'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    speciality = db.Column(db.String(80))
    phone = db.Column(db.String(9))
    email = db.Column(db.String(80))
    residence_zone = db.Column(db.Integer, db.ForeignKey('zone.id'),
        nullable=True)
    #zones = db.relationship('ZoneModel', back_populates='medical_doctors')	
    subscription = relationship('subscription', secondary=subscription_medical_doctor_table, backref='medical_doctor')
    assignment = relationship('assignment', secondary=assignment_table, backref='medical_doctor')

    def __init__(self, id, password, speciality, phone, email):
        super().__init__(id, password)
        self.speciality = speciality
        self.phone = phone
        self.email = email

    def json(self):
        return {'id': self.id, 'speciality': self.speciality, 'phone': self.phone, 'email': self.email}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()