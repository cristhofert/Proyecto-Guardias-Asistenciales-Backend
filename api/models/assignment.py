from db import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from util.query import QueryWithSoftDelete

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
    deleted = db.Column(db.Boolean(), default=False)

    query_class = QueryWithSoftDelete
    
    db.UniqueConstraint('guard_id', 'medical_doctor_id',
                     name='guard_medical_doctor_unique')

    def __init__(self, medical_doctor_id, guard_id, institution_id=1):
        self.guard_id = guard_id
        self.medical_doctor_id = medical_doctor_id
        self.institution_id = institution_id

    def json(self):
        return {
            'id': self.id,
            'guard': self.guard.json(),
            'medical_doctor': self.medical_doctor.json(),
            'assignment_date': str(self.assignment_date.strftime('%Y-%m-%d')),
            'institution': self.institution_id
        }

    def get_assignment_date(self):
        return self.assignment_date

    @classmethod
    def find_by_guard_id(cls, _id):
        return cls.query.filter_by(guard_id=_id).order_by(self.assignment_date).first()

    @classmethod
    def find_by_medical_doctor_id(cls, _id):
        return cls.query.filter_by(medical_doctor_id=_id).order_by('assignment_date').all()

    @classmethod
    def find_by_ids(cls, _medical_doctor_id, _guard_id):
        return cls.query.filter_by(medical_doctor_id=_medical_doctor_id, guard_id=_guard_id).order_by(AssignmentModel.assignment_date).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        self.deleted = True
        db.session.commit()
