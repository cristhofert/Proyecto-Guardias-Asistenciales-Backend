from db import db

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)# Cedula de Identidad de Uruguay
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    type = db.Column(db.String(80))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    def __init__(self, id, name, password, type):
        self.id = id
        self.name = name
        self.password = password
        self.type = type

    def json(self):
        return {'id': self.id, 'name': self.name, 'password': self.password}   

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()