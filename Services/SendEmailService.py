from flask import Flask
import os
from dotenv import load_dotenv
from flask_mail import Mail,Message

mailApp = Flask(__name__)

load_dotenv()

mail= Mail(mailApp)

mailApp.config['MAIL_SERVER'] = os.getenv('SERVER')
mailApp.config['MAIL_PORT'] = os.getenv('PORT')
mailApp.config['MAIL_USERNAME'] = os.getenv('CORREO')
mailApp.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
mailApp.config['MAIL_USE_TLS'] = True

class SendEmailService:
  
    def __init__(self):
      self.password = os.getenv('EMAIL_PASSWORD')

    def send(self, correo, password):
        email_sender = os.getenv('CORREO')
        email_receiver = correo
        subject = 'Bienvenido al sistema de empleados!'
        body = f"""  
              Se ha creado una cuenta nueva en el sistema de empleados, tu password de ingreso es: {password} 
          """

        msg = Message(subject, sender=email_sender, recipients=[email_receiver])
        msg.body = body
  
        try:
          with mail.connect() as connection:
            connection.send(msg)
            return 'Correo enviado correctamente'
        except Exception as e:
          return f'Error al enviar el correo: {str(e)}'