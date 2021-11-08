from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
import sendgrid
from models.notification import NotificationModel

def Notificaciones(email, telefono, id, gid, message):

    notification = NotificationModel(id, gid, message, institution_id=1)

    notification.save_to_db()

    # print(email)
    mail = Mail()
    mail.from_email = Email("federicoDn3@gmail.com", "Guardias Medicas")
    #to_email = To(email)
    # Esto en caso de prueba
    mail.to = To(email)
    mail.subject = "Nuevas Guardias Publicadas"
    mail.template_id = TemplateId("d-983dd4b5e34a4b4ba99130f61ca97feb")

    sg = sendgrid.SendGridAPIClient(
        api_key='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')
    sg.send(mail)

    account_sid = 'ACf75fba9132de9b7c1ff453096fdac4a3'
    auth_token = 'a3bb005cfade74f07bb36438edb5fa51'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hay nuevas guardias disponibles, revisa tu cuenta para mas informacion.',
        to=telefono
    )
    print(message.sid)
