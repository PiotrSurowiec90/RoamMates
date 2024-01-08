from flask import request, jsonify, session
import psycopg
from token_config import token_checker, token_generator

from lib.database_connection import get_flask_database_connection
from lib.Request_repository import RequestRepository


def apply_request_routes(app):
    """Requests Router."""

    @app.route("/requests/<status>", methods=["GET"])
    def requests_user_list(status):
        """Gets list of users with pending requests or matches
        for currently loged user.

        - If status equals null retrieves list of pending requests.
        - If statys equals true retrives list of matches.
        - Otherwise returns 404.

        Returns:
            _type_: Json (message and list of users.)
        """

        status = str(status)
        connection = get_flask_database_connection(app)
        token = request.headers["Authorization"][7:]
        user_id = session.get("user_id")

        if not token_checker(token, user_id):
            response = jsonify({"message": "Invalid credentials"})
            response.status_code = 401
        else:
            request_repo = RequestRepository(connection)
            try:
                users = request_repo.get_requesting_users_for_user(
                    user_id, f"IS {status.upper()}"
                )
                token = token_generator(user_id)
                response = jsonify({"message": "OK!", "token": token, "users": users})
                response.status_code = 200
            except psycopg.errors.SyntaxError:
                response = jsonify({"message": "URL NOT FOUND!"})
                response.status_code = 404

        return response
