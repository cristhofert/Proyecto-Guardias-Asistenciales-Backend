from db import db

class AuditModel(db.Model):
    __tablename__ = 'audit'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('UserModel')
    action = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime)

    def __init__(self, user_id, action, timestamp):
        self.user_id = user_id
        self.action = action
        self.timestamp = timestamp

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'action': self.action,
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