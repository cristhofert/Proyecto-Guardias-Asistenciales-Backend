from db import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class AssignmentModel(db.Model):
    __tablename__ = 'assignment'
    
    guard_id = db.Column(db.ForeignKey('guard.id'), primary_key=True)
    guard = db.relationship("GuardModel", back_populates="assignment", uselist=False)#solucionar esta relacion
    medical_doctor_id = db.Column(db.ForeignKey('medical_doctor.id'), primary_key=True)
    medical_doctor = db.relationship('MedicalDoctorModel', back_populates='assignment', uselist=False)
    assignment_date= db.Column(db.DateTime, default=db.func.current_timestamp())
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id'), nullable=False, default=1)
    institution = db.relationship("InstitutionModel")

    def __init__(self, medical_doctor_id, guard_id, institution_id=1):
        self.guard_id = guard_id
        self.medical_doctor_id = medical_doctor_id
        self.institution_id = institution_id

    def json(self):
        return {
            'guard': self.guard.json(),
            'medical_doctor': self.medical_doctor.json(),
            'assignment_date': self.assignment_date,
            'institution': self.institution_id
        }

    @classmethod
    def find_by_guard_id(cls, _id):
        return cls.query.filter_by(guard_id=_id).order_by(Assignmentmodel.assignment_date).first()
        
    @classmethod
    def find_by_medical_doctor_id(cls, _id):
        return cls.query.filter_by(medical_doctor_id=_id).order_by(Assignmentmodel.assignment_date).first()
    
    @classmethod
    def find_by_ids(cls, _medical_doctor_id, _guard_id):
        return cls.query.filter_by(medical_doctor_id=_medical_doctor_id, guard_id=_guard_id).order_by(Assignmentmodel.assignment_date).first()
    