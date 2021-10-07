from db import db
from sqlalchemy.orm import relationship

class ServiceModel(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    code = db.Column(db.String(10), unique=True)
    color = db.Column(db.String(10), unique=True)

    def __init__(self, name, code, color):
        self.name = name
        self.code = code
        self.color = color

    def json(self):
        return {'name': self.name, 'code': self.code, 'color': self.color, 'id': self.id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # simple TOP 1 select

    def save_to_db(self):  # Upserting data
        db.session.add(self)
        db.session.commit()  # Balla

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
