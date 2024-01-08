import jwt
from datetime import datetime, timedelta
from flask import jsonify


# Function generating unique token containing user_id
def token_generator(user_id):
    token = jwt.encode({"user_id": user_id}, "secret", algorithm="HS256")

    return token


# Function checking a validity of a token
# We copare decoded token user_id to user_id stored in session
# Returns True if valid, False if invalid
def token_checker(token, user_id_from_session):
    try:
        decoded_token = jwt.decode(token, "secret", algorithms=["HS256"])
        return decoded_token["user_id"] == user_id_from_session
    except Exception as e:
        raise ValueError(f"Token not valid: {e}")


print(token_generator(2))
