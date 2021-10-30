from db import db
from sqlalchemy.orm import relationship

class GuardsGroupModel(db.Model):
    __tablename__ = 'guards_group'

    id = db.Column(db.Integer, primary_key=True)
    guards = relationship("GuardModel", backref="guards_group")
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id'), nullable=False, default=1)
    institution = db.relationship("InstitutionModel")
    quantity = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, id, guards, institution_id=1, quantity=1):
        self.id = id
        self.guards = guards
        self.institution_id = institution_id
        self.quantity = quantity

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