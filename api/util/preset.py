from sqlalchemy import event
from models.institution import InstitutionModel
from models.user import UserModel
from models.medical_doctor import MedicalDoctorModel
from db import db

def preset():
    # auto insert user
    def insert_data_i(target, connection, **kw):
        connection.execute(target.insert(), {'id': 1})

    event.listen(InstitutionModel.__table__, 'after_create', insert_data_i)

    def insert_data(target, connection, **kw):
        connection.execute(target.insert(),
                           {'id': 1234562, 'name': 'Cristhofer Travieso', 'password': 'cris1234',
                               'type': 'administrator', 'institution_id': 1},
                           {'id': 98765443, 'name': 'Travieso Cristhofer', 'password': '1234cris',
                            'type': 'medical_doctor', 'institution_id': 1})

    event.listen(UserModel.__table__, 'after_create', insert_data)

def preset_db():
    db.session.add(InstitutionModel())
    db.session.add(InstitutionModel())
    db.session.add(MedicalDoctorModel(1234562,  'Cristhofer Travieso',  'cris1234', 'md', '09785412', 'c@c.com', 1))
    db.session.add(MedicalDoctorModel(4562123,  'Travieso Cristhofer ',  '1234cris', 'pedatria', '09748512', 'b@c.com', 2))
    db.session.commit()
