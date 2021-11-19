from db import db
from util.query import QueryWithSoftDelete

class NotificationModel(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    medical_doctor_id = db.Column(db.String(80), db.ForeignKey(
        'medical_doctor.id'), nullable=False)
    medical_doctor = db.relationship(
        'MedicalDoctorModel', backref='notifications', lazy=True)
    guard_id = db.Column(db.Integer, db.ForeignKey('guard.id'), nullable=False)
    guard = db.relationship('GuardModel', backref='notifications', lazy=True)
    message = db.Column(db.String(128), nullable=False)
    read = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, nullable=False,
                          default=db.func.current_timestamp())
    institution_id = db.Column(db.Integer, db.ForeignKey(
        'institutions.id'), nullable=False, default=1)
    institution = db.relationship("InstitutionModel")
    deleted = db.Column(db.Boolean(), default=False)

    query_class = QueryWithSoftDelete

    def __init__(self, medical_doctor_id, guard_id, message, read=False, institution_id=1):
        self.medical_doctor_id = medical_doctor_id
        self.guard_id = guard_id
        self.message = message
        self.read = read
        self.institution_id = institution_id

    def json(self):
        return {
            'id': self.id,
            'medical_doctor': self.medical_doctor.json(),
            'guard': self.guard.json() if self.guard_id else None,
            'message': self.message,
            'read': self.read,
            'timestamp': str(self.timestamp.strftime('%Y-%m-%d %H:%M:%S')),
            'institution': self.institution_id
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(medical_doctor_id=user_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        self.deleted = True
        db.session.commit()
