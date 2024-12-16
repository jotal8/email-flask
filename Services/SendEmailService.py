from flask import Flask
import os
from dotenv import load_dotenv
from flask_mail import Mail,Message

mailApp = Flask(__name__)

mail= Mail(mailApp)

mailApp.config['MAIL_SERVER'] = 'smtp.gmail.com'
mailApp.config['MAIL_PORT'] = 587
mailApp.config['MAIL_USERNAME'] = 'jotal8@gmail.com'
mailApp.config['MAIL_PASSWORD'] = 'huct pejy ohiv cjzw'
mailApp.config['MAIL_USE_TLS'] = True

load_dotenv()

class SendEmailService:
  
    def __init__(self):
      self.password = os.getenv('EMAIL_PASSWORD')

    def send(self):
        email_sender = 'jotal8@gmail.com'
        email_receiver = 'julian.otalvaro@cerok.com'
        subject = 'Bienvenido al sistema de empleados!'
        body = """  
            Se ha creado una cuenta nueva en el sistema de empleados, tu password de ingreso es: XXXXXX 
        """

        msg = Message(subject, sender=email_sender, recipients=[email_receiver])
        msg.body = body
  
        try:
          with mail.connect() as connection:
            connection.send(msg)
            return 'Correo enviado correctamente'
        except Exception as e:
          return f'Error al enviar el correo: {str(e)}'