from db import db
from util.query import QueryWithSoftDelete


class GuardsGroupModel(db.Model):
    __tablename__ = 'guards_group'

    id = db.Column(db.Integer, primary_key=True)
    guards = db.relationship("GuardModel", backref="group", lazy=True)
    institution_id = db.Column(db.Integer, db.ForeignKey(
        'institutions.id'), nullable=False, default=1)
    institution = db.relationship("InstitutionModel")
    quantity = db.Column(db.Integer, nullable=False, default=1)
    deleted = db.Column(db.Boolean(), default=False)

    query_class = QueryWithSoftDelete

    def __init__(self, guards, institution_id=1, quantity=1):
        self.guards = guards
        self.institution_id = institution_id
        self.quantity = quantity

    def json(self):
        return {
            **(self.guards[0].json() if self.guards else {}),
            'id': self.id,
            'institution': self.institution_id,
            'quantity': self.quantity,
            'assinged': len(self.guards)
        }

    def guards_json(self):
        guards = []
        for guard in self.guards:
            if not guard.deleted:
                guards.append(guard.json())
        return {
            'guards': guards
        }

    def get_id(self):
        return self.id

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        self.deleted = True
        db.session.commit()
