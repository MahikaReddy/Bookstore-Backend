import secrets

jwt_secret_key = secrets.token_urlsafe(32)
print(jwt_secret_key)



flask_secret_key = secrets.token_urlsafe(32)
print(flask_secret_key)
