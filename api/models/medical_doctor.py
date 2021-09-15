from db import db
from models.user import UserModel
from models.service import service_medical_doctor_table
from sqlalchemy.orm import relationship

class MedicalDoctorModel(UserModel):
    __tablename__ = 'medical_doctor'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    speciality = db.Column(db.String(80))
    service = relationship(
        "ServiceModel",
        secondary=service_medical_doctor_table,
        back_populates="service")

    def __init__(self, id, password, speciality):
        super().__init__(id, password)
        self.speciality = speciality

    def json(self):
        return {'id': self.id, 'speciality': self.speciality}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()