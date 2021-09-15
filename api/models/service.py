from db import db
from sqlalchemy.orm import relationship

service_medical_doctor_table = db.Table('association', db.Model.metadata,
    db.Column('service_id', db.ForeignKey('service.id'), primary_key=True),
    db.Column('medical_doctor_id', db.ForeignKey('medical_doctor.id'), primary_key=True)
)

class ServiceModel(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    code = db.Column(db.String(10), unique=True)
    color = db.Column(db.String(10), unique=True)
    guards = relationship("GuardModel", back_populates="service")
    #M.D. list
    list = relationship(
        "MedicalDoctorModel",
        secondary=service_medical_doctor_table,
        back_populates="list")

    def __init__(self, name, code, color):
        self.name = name
        self.code = code
        self.color = color

    def json(self):
        return {'name': self.name, 'code': self.code, 'color': self.color}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # simple TOP 1 select

    def save_to_db(self):  # Upserting data
        db.session.add(self)
        db.session.commit()  # Balla

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
