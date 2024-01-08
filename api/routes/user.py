from flask import request, jsonify, session
from token_config import token_checker, token_generator
from lib.database_connection import get_flask_database_connection

from lib.User_repository import UserRepository
from lib.User import User


def apply_user_routes(app):
    """User Router."""

    @app.route("/users/add", methods=["POST"])
    def user_signup():
        """
        Route: /users/add
        Request: POST
        Signup, adds user to Users table.
        """

        connection = get_flask_database_connection(app)
        user_repo = UserRepository(connection)

        data = request.get_json()
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")

        # Check if user email is unique
        if user_repo.find_by_email(email):
            print("User already exists:")
            response = jsonify({"message": "Credentials error"})
            response.status_code = 401

        else:
            new_user = User(None, username, password, email)
            user_repo.add(new_user)
            response = jsonify({"message": "OK!"})
            response.status_code = 200

        return response
