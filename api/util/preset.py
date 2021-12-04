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
    # Open the .sql file
    sql_file = open('api/util/data.sql', 'r', encoding='utf-8') 

    # Create an empty command string
    sql_command = ''

    # Iterate over all lines in the sql file
    for line in sql_file:
        # Ignore commented lines
        if not line.startswith('--') and line.strip('\n'):
            # Append line to the command string
            sql_command += line.strip('\n')

            # If the command string ends with ';', it is a full statement
            if sql_command.endswith(';'):
                # Try to execute statement and commit it
                try:
                    db.session.execute(text(sql_command))
                    db.session.commit()

                # Assert in case of error
                except:
                    print('Ops')

                # Finally, clear command string
                finally:
                    sql_command = ''
 