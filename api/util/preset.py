from sqlalchemy import event, text
from models.institution import InstitutionModel
from models.user import UserModel
from models.medical_doctor import MedicalDoctorModel
from models.guard import GuardModel
from models.subscription import SubscriptionModel
from models.service import ServiceModel
from models.assignment import AssignmentModel
from models.zone import ZoneModel
from models.guards_group import GuardsGroupModel
from models.administrator import AdministratorModel
from db import db
import bcrypt


def preset_db():
    try:
        db.session.add(InstitutionModel())
        db.session.add(InstitutionModel())
        db.session.add(ZoneModel("z1"))
        db.session.add(GuardsGroupModel([]))
        passw = 'cris1234'
        hashed = bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())
        md = MedicalDoctorModel(
            1234562,  'Cristhofer Travieso',  hashed, 'md', '09785412', 'c@c.com', 1)
        db.session.add(md)
        passw = '1234cris'
        hashed2 = bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())
        db.session.add(MedicalDoctorModel(4562123,  'Travieso Cristhofer ',
                                          hashed2, 'pedatria', '09748512', 'b@c.com', 1))
        db.session.add(ServiceModel('Puerta de Emergencia', 'PE1'))
        db.session.add(ServiceModel('Puerta de Emergencia II', 'PE2'))
        sub = SubscriptionModel('lista', 1)
        db.session.add(sub)
        db.session.add(SubscriptionModel('lista', 2))
        g1 = GuardModel(1, '2021-12-25', '08:00', '10:15')
        g2 = GuardModel(1, '2021-12-25', '09:00', '11:15')
        g3 = GuardModel(1, '2021-12-26', '10:00', '12:15')
        g4 = GuardModel(2, '2021-12-27', '08:11', '10:00')
        g1.save_to_db()
        g2.save_to_db()
        g3.save_to_db()
        g4.save_to_db()
        db.session.add(GuardsGroupModel([g1, g2, g3]))
        db.session.add(GuardsGroupModel([g4]))
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
        g4.medical_doctor_id = 4562123
        g4.save_to_db()

        md.subscriptions.append(sub)
        md.save_to_db()
        passw = 'jp123'
        hashed3 = bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())
        db.session.add(AdministratorModel(98765431, 'Juan Perez', hashed3, 1, True))
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()