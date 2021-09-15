from db import db
from sqlalchemy.orm import relationship

class GuardModel(db.Model):
    __tablename__ = 'guard'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    assigned_at = db.Column(db.DateTime)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    service = relationship("ServiceModel", back_populates="guards")
    zone = relationship('ZoneModel')#?
    medical_doctor = relationship('MedicalDoctorModel')
    
    def __init__(self, id, service, zone=None):
        self.id = id
        self.service = service
        if zone:
            self.zone = zone
            
    def json(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'assigned_at': self.assigned_at,
            'service_id': self.service_id
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        