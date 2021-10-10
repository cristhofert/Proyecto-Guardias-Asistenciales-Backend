from db import db
from models.user import UserModel

class AdministratorModel(UserModel):
    __tablename__ = 'administrator'
    
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity':'administrator'
    }
    
    def __init__(self, id, name, password):
        super().__init__(id, name, password, 'administrator')

    def json(self):
        return {'id': self.id, 'name': self.name}
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()