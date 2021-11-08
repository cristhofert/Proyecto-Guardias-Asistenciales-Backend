from sqlalchemy import event
from models.institution import InstitutionModel
from models.user import UserModel
from models.medical_doctor import MedicalDoctorModel
from models.guard import GuardModel
from models.subscription import SubscriptionModel
from models.service import ServiceModel
from models.assignment import AssignmentModel
from models.zone import ZoneModel
from models.guards_group import GuardsGroupModel
from db import db


def preset_db():
    db.session.add(InstitutionModel())
    db.session.add(InstitutionModel())
    db.session.add(ZoneModel("z1"))
    db.session.add(GuardsGroupModel([]))
    md = MedicalDoctorModel(
        1234562,  'Cristhofer Travieso',  'cris1234', 'md', '09785412', 'c@c.com', 1)
    db.session.add(md)
    db.session.add(MedicalDoctorModel(4562123,  'Travieso Cristhofer ',
                   '1234cris', 'pedatria', '09748512', 'b@c.com', 1))
    db.session.add(ServiceModel('Puerta de Emergencia', 'PE1', ''))
    sub = SubscriptionModel('lista', 1)
    db.session.add(sub)
    g1 = GuardModel(1, '2021-1-1', '08:00', '10:15')
    g2 = GuardModel(1, '2021-2-2', '09:00', '11:15')
    g3 = GuardModel(1, '2021-3-3', '10:00', '12:15')
    g1.save_to_db()
    g2.save_to_db()
    g3.save_to_db()
    db.session.add(AssignmentModel(4562123, 1, 1))
    db.session.commit()
    g1.medical_doctor_id = 4562123
    g1.save_to_db()
    db.session.add(AssignmentModel(1234562, 1, 1))
    db.session.commit()
    g1.medical_doctor_id = 1234562
    g1.save_to_db() 
    db.session.add(AssignmentModel(1234562, 2, 1))
    db.session.commit()
    g2.medical_doctor_id = 1234562
    g2.save_to_db()
    db.session.commit()

    md.subscriptions.append(sub)
    md.save_to_db()
