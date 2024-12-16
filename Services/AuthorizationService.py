import jwt

class AuthorizationService:
  def __init__(self, SECRET_KEY, algorithm="HS256", expiration_hours=1):
    self.secret_key = SECRET_KEY
    self.algorithm = algorithm
    self.expiration_hours = expiration_hours

  def verifyToken(self, token):
    try:
      decoded = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
      return {"valid": True, "data": decoded}
    except jwt.ExpiredSignatureError:
      return {"valid": False, "error": "El token ha expirado!"}
    except jwt.InvalidTokenError:
      return {"valid": False, "error": "El token es invalido!"}