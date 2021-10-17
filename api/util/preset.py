from sqlalchemy import event
from models.institution import InstitutionModel
from models.user import UserModel

def preset():
    
    #auto insert user
    def insert_data_i(target, connection, **kw):
        connection.execute(target.insert(), {'id': 1})

    event.listen(InstitutionModel.__table__, 'after_create', insert_data_i)

    def insert_data(target, connection, **kw):
        connection.execute(target.insert(), {'id': 1234562, 'name': 'Cristhofer Travieso', 'password': 'cris1234', 'type': 'administrator', 'institution_id': 1}, {'id': 98765443, 'name': 'Travieso Cristhofer', 'password': '1234cris', 'type': 'medical_doctor', 'institution_id': 1})

    event.listen(UserModel.__table__, 'after_create', insert_data)
    