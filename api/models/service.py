from db import db
from sqlalchemy.orm import relationship


class ServiceModel(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    code = db.Column(db.String(10), unique=True)
    color = db.Column(db.String(10))
    institution_id = db.Column(db.Integer, db.ForeignKey(
        'institutions.id'), nullable=False, default=1)
    institution = db.relationship("InstitutionModel")

    def __init__(self, name, code, color, institution_id=1):
        self.name = name
        self.code = code
        self.color = color
        self.institution_id = institution_id

    def json(self):
        return {'name': self.name,
                'code': self.code,
                'color': self.color,
                'id': self.id,
                'institution': self.institution_id
        }

    def get_subscriptions(self):
        return self.subscriptions

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # simple TOP 1 select

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()  # simple TOP 1 select

    def save_to_db(self):  # Upserting data
        db.session.add(self)
        db.session.commit()  # Balla

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
