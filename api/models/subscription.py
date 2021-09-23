from db import db
from sqlalchemy.orm import relationship

class SubscriptionModel(db.Model):
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80))
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    service = relationship('ServiceModel')

    def __init__(self, type, service_id):
        self.type = type
        self.service_id = service_id

    def json(self):
        return {
            'id': self.id,
            'type': self.type,
            'service_id': self.service_id
        }

    @classmethod
    def find_by_channel_id(cls, channel_id):
        return cls.query.filter_by(channel_id=channel_id).first()