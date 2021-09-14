from db import db
from user import UserModel
from service import association_table
from sqlalchemy.orm import relationship

class MedicalDoctorModel(UserModel):
    __tablename__ = 'medical_doctor'

    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    speciality = db.Column(db.String(80))
    service = relationship(
        "ServiceModel",
        secondary=association_table,
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