from db import db
from util.query import QueryWithSoftDelete

class ServiceModel(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    code = db.Column(db.String(10), unique=True)
    institution_id = db.Column(db.Integer, db.ForeignKey(
        'institutions.id'), nullable=False, default=1)
    institution = db.relationship("InstitutionModel")
    deleted = db.Column(db.Boolean(), default=False)

    query_class = QueryWithSoftDelete
    
    def __init__(self, name, code, institution_id=1):
        self.name = name
        self.code = code
        self.institution_id = institution_id

    def json(self):
        return {'name': self.name,
                'code': self.code,
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
        self.deleted = True
        db.session.commit()
