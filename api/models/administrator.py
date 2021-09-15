from db import db
from models.user import UserModel

class AdministratorModel(UserModel):
    __tablename__ = 'administrator'
    
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __init__(self, id, password):
        super().__init__(id, name, password)

    def json(self):
        return {'id': self.id, 'password': self.password}
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()