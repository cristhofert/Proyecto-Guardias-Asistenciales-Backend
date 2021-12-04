from db import db
from models.user import UserModel
from util.query import QueryWithSoftDelete

class AdministratorModel(UserModel):
    __tablename__ = 'administrator'

    id = db.Column(db.String(80), db.ForeignKey('user.id'), primary_key=True)
    superadmin = db.Column(db.Boolean, default=False)

    query_class = QueryWithSoftDelete
    __mapper_args__ = {
        'polymorphic_identity': 'administrator'
    }

    def __init__(self, id, name, password, institution_id=1, superadmin=False):
        super().__init__(id, name, password, 'administrator', institution_id)
        self.superadmin = superadmin

    def json(self):
        return {'id': self.id,
                'name': self.name,
                'institution': self.institution_id,
                'type': self.type,
                'password': self.password,
                'superadmin': self.superadmin
                }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        if self.superadmin:
            return 'Cannot delete superadmin'
        self.deleted = True
        db.session.commit()
        return 'Administrator has been deleted'
