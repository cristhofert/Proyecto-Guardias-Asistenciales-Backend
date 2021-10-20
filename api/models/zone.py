from db import db

class ZoneModel(db.Model):
    __tablename__ = 'zone'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    geotag = db.Column(db.String(80))
    longitude = db.Column(db.String(80))
    latitude = db.Column(db.String(80))
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id'), nullable=False, default=1)
    institution = db.relationship("InstitutionModel")

    def __init__(self, name, geotag=0, longitude=0, latitude=0, institution_id=1):
        self.name = name
        self.geotag = geotag
        self.longitude = longitude
        self.latitude = latitude
        self.institution_id = institution_id

    def json(self):
        return {'id': self.id,
        'name': self.name,
        'geotag': self.geotag,
        'longitude': self.longitude,
        'latitude': self.latitude
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()