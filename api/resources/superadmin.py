from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
from models.administrator import AdministratorModel
from models.institution import InstitutionModel
import bcrypt
import random
from models.user import UserModel
from util.encoder import AlchemyEncoder
from util.is_empty import is_empty
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
import sendgrid

class SuperAdmin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def __init__(self):
        pass
        ##self.logger = create_logger()

    def post(self, id):
        #self.logger.info(f'parsed args: {self.parser.parse_args()}')
        data = self.parser.parse_args()
        if is_empty(data):
            return {'menssage': 'The field is required'}, 401
        if AdministratorModel.find_by_id(data['id']):
            return {'message': "An administrator with id '{}' already exists.".format(
                data['id'])}, 400
        try:
            Ins = InstitutionModel()
            Ins.save_to_db()
            passw = str(random.randrange(000000000, 999999999, 9))
            hashed = bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())
            administrator = AdministratorModel(
                data['id'], data['name'], hashed, Ins.id, superadmin=True)
            administrator.save_to_db()

        except BaseException as err:
            return {"message": "An error occurred inserting the administrator."}, 500

        email = data['id']
        mail = Mail()
        mail.from_email = Email("federicoDn3@gmail.com", "Guardias Medicas")
        mail.to = To(email)
        mail.subject = "Bienvenido a Guardias Medicas"
        mail.template_id = TemplateId("")#Usar Template Id de Sendgrid
        mail.dynamic_template_data = {"User": data['id'], "Pass": passw}
        try:
            sg = sendgrid.SendGridAPIClient(
                api_key='')#Usar Api key de Sendgrid
            response = sg.send(mail) 
            print(response)
            pass
        except:
            return {"message": "An error occurred sending mail."}, 500

        return {'message': "Super Administrator created successfully."}, 201