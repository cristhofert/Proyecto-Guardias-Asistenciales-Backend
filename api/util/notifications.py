from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
import sendgrid
from models.notification import NotificationModel
import threading

def Notificaciones(email, telefono, id, gid, message):

    notification = NotificationModel(id, gid, message, institution_id=1)

    notification.save_to_db()

    threading.Thread(target=notificar, args=(email, telefono, message)).start()

def notificar(email, telefono, message):
    try:
        # print(email)
        mail = Mail()
        mail.from_email = Email("", "Guardias Medicas")#Usar email seleccionado para sendgrid
        mail.to = To(email)
        mail.subject = "Nuevas Guardias Publicadas"
        mail.template_id = TemplateId("") #Usar Template Id de twilio 

        sg = sendgrid.SendGridAPIClient(
            api_key='')#Usar la api key de sendgrid
        sg.send(mail)

        account_sid = ''#Usar la sid key de sendgrid
        auth_token = ''#Usar la token de sendgrid
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='',#Usar tel asignado por twilio 
            body='Hay nuevas guardias disponibles, revisa tu cuenta para mas informacion.',
            to=telefono
        )
        print(message.sid)
    except Exception as e:
        print(e)
