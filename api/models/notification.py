from db import db 

class NotificationModel(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    medical_doctor_id = db.Column(db.Integer, db.ForeignKey('medical_doctor.id'), nullable=False)
    medical_doctor = db.relationship('MedicalDoctorModel', backref='notifications', lazy=True)
    message = db.Column(db.String(128), nullable=False)
    read = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __init__(self, medical_doctor_id, message, read=False):
        self.medical_doctor_id = medical_doctor_id
        self.message = message
        self.read = read

    def json(self):
        return {
            'id': self.id,
            'medical_doctor': self.medical_doctor.json(),
            'message': self.message,
            'read': self.read,
            'timestamp': self.timestamp
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()