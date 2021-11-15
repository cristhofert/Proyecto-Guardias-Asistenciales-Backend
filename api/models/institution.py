from db import db
from util.query import QueryWithSoftDelete

class InstitutionModel(db.Model):
    __tablename__ = 'institutions'

    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.Boolean(), default=False)

    query_class = QueryWithSoftDelete   
    
    def __init__(self):
        pass

    def json(self):
        return {
            'id': self.id
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        self.deleted = True
        db.session.commit()