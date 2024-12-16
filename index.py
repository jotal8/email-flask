import os
from flask import Flask, Response, request, jsonify
from Services.AuthorizationService import AuthorizationService
from Services.SendEmailService import SendEmailService
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)

@app.route("/sendEmail", methods=['POST'])
def run():
  data = {
      "success": False,
      "message": ""
  }

  statusCode = 401
  authorizationHeader = request.headers.get('Authorization')

  if(authorizationHeader):
    SECRET_KEY = os.getenv('SECRET_KEY')
    authorization_service = AuthorizationService(SECRET_KEY)
    token = authorizationHeader.replace('Bearer ', '')
    verify = authorization_service.verifyToken(token)

    if(verify["valid"]):
      send_email_service = SendEmailService()
      params = request.json
      data["message"] = send_email_service.send(params.get('correo'),params.get('password'))
      statusCode = 200
      data["success"] = True
    else:
      data["message"] = 'EL token es invalido!'

  else:
    data["message"] = 'EL servicio requiere autorizacion'

  response = Response(json.dumps(data), mimetype='application/json')
  response.status_code = statusCode
  return response