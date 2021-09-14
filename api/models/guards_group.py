from db import db
from sqlalchemy.orm import relationship

class GuardsGroupModel(db.Model):
    __tablename__ = 'guards_group'

    id = db.Column(db.Integer, primary_key=True)
    guards = relationship("guards", backref="guards_group")

    def __init__(self, id, guards):
        self.id = id
        self.guards = guards

    def json(self):
        return {'id': self.id, 'guards': self.guards}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()