from db import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint


class AssignmentModel(db.Model):
    __tablename__ = 'assignment'

    id = db.Column(db.Integer, primary_key=True)
    guard_id = db.Column(db.Integer, db.ForeignKey('guard.id'))
    guard = db.relationship(
        "GuardModel", back_populates="assignments", lazy=True)
    medical_doctor_id = db.Column(db.ForeignKey('medical_doctor.id'))
    medical_doctor = db.relationship(
        'MedicalDoctorModel', back_populates='assignments')
    assignment_date = db.Column(
        db.DateTime, default=db.func.current_timestamp())
    institution_id = db.Column(db.Integer, db.ForeignKey(
        'institutions.id'), nullable=False, default=1)
    institution = db.relationship("InstitutionModel")
    UniqueConstraint('guard_id', 'medical_doctor_id',
                     name='guard_medical_doctor_unique')

    def __init__(self, medical_doctor_id, guard_id, institution_id=1):
        self.guard_id = guard_id
        self.medical_doctor_id = medical_doctor_id
        self.institution_id = institution_id

    def json(self):
        return {
            'id': str(self.medical_doctor_id) + '-' + str(self.guard_id),
            'guard': self.guard.json(),
            'medical_doctor': self.medical_doctor.json(),
            'assignment_date': str(self.assignment_date.strftime('%Y-%m-%d'))
        }

    @classmethod
    # retorna informacion de una asignacion de guardia(que medico tiene esa guardia)
    def find_by_guard_id(cls, _id):
        return cls.query.filter_by(guard_id=_id).order_by(self.assignment_date).first()

    @classmethod
    def find_by_medical_doctor_id(cls, _id):
        return cls.query.filter_by(medical_doctor_id=_id).order_by('assignment_date').all()

    @classmethod
    def find_by_ids(cls, _medical_doctor_id, _guard_id):
        return cls.query.filter_by(medical_doctor_id=_medical_doctor_id, guard_id=_guard_id).order_by(Assignmentmodel.assignment_date).first()
