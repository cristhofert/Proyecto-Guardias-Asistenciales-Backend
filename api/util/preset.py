from sqlalchemy import event
from models.institution import InstitutionModel
from models.user import UserModel
from models.medical_doctor import MedicalDoctorModel
from models.guard import GuardModel
from models.subscription import SubscriptionModel
from models.service import ServiceModel
from models.assignment import AssignmentModel
from db import db

def preset_db():
    db.session.add(InstitutionModel())
    db.session.add(InstitutionModel())
    db.session.add(MedicalDoctorModel(1234562,  'Cristhofer Travieso',  'cris1234', 'md', '09785412', 'c@c.com', 1))
    db.session.add(MedicalDoctorModel(4562123,  'Travieso Cristhofer ',  '1234cris', 'pedatria', '09748512', 'b@c.com', 2))
    db.session.add(ServiceModel('Puerta de Emergencia', 'PE1', ''))
    db.session.add(SubscriptionModel('lista', 1))
    db.session.add(GuardModel(1, '2021-1-1', '08:00', '10:15'))
    db.session.add(GuardModel(1, '2021-2-2', '09:00', '11:15'))
    db.session.add(AssignmentModel(1234562, 1, 1))
    db.session.add(AssignmentModel(1234562, 2, 1))
    db.session.add(AssignmentModel(4562123, 1, 1))
    db.session.commit()
