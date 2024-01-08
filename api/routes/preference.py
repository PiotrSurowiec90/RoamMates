from flask import request, jsonify, session
from token_config import token_checker, token_generator

from lib.database_connection import get_flask_database_connection
from lib.Preference_repository import PreferenceRepository
from lib.Preference import Preference


def apply_preference_routes(app):
    """Profile Router."""

    @app.route("/preferences/new", methods=["POST"])
    def setup_preferences_data():
        """
        Posts preferences data
        Route: /preferences/new
        Request: POST
        """

        connection = get_flask_database_connection(app)
        # get data
        data = request.get_json()

        token = request.headers["Authorization"][7:]
        user_id = session.get("user_id")

        if not token_checker(token, user_id):
            response = jsonify({"message": "Invalid credentials"})
            response.status_code = 401
            return response

        # get old preferences by user_id
        preferences_repo = PreferenceRepository(connection)
        preferences = preferences_repo.find_by_user_id(user_id)
        # compare both data and skip None values
        if preferences:
            for key in ["age_slot", "gender", "continent", "season", "category"]:
                new_value = data.get(key)
                if new_value is not None:
                    setattr(preferences, key, data[key])
            preferences_repo.setup_preferences(preferences, "update")

        else:
            # create new preferences object
            new_preferences = Preference(
                None,
                user_id,
                data.get("age_slot"),
                data.get("gender"),
                data.get("continent"),
                data.get("season"),
                data.get("category"),
            )
            preferences_repo.setup_preferences(new_preferences, "insert")

        token = token_generator(user_id)
        response = jsonify({"message": "OK!", "token": token})
        response.status_code = 200

        return response
