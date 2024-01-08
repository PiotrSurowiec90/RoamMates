from lib.Request import Request
from lib.Profile import Profile
from lib.User import User


class RequestRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from REQUESTS")
        requests = [
            Request(row["id"], row["status"], row["request_from"], row["request_to"])
            for row in rows
        ]
        return requests

    # Function returns a list of all requests with status null
    def all_null(self):
        rows = self._connection.execute("SELECT * from REQUESTS WHERE status IS NULL")
        requests = [
            Request(row["id"], row["status"], row["request_from"], row["request_to"])
            for row in rows
        ]
        return requests

    # Function returns a list of all requests with status true
    def all_true(self):
        rows = self._connection.execute("SELECT * from REQUESTS WHERE status = true")
        requests = [
            Request(row["id"], row["status"], row["request_from"], row["request_to"])
            for row in rows
        ]
        return requests

    def get_requesting_users_for_user(self, requested_user_id, status_condition):
        """
        Repository method to get list of users with pending or approved request
        to seleced user.

        Args:
            requested_user_id: Id of user request has been sent to.
            status_condition: status of request (true if match), (null if pending).
        """

        query = f"""
        SELECT 
        requests.status AS r_status,
        requests.request_from AS r_request_from,
        requests.request_to AS r_request_to,
        users.id AS u_id,
        users.username AS u_username,
        users.email As u_email,
        profiles.picture AS p_picture,
        profiles.name AS p_name,
        profiles.age AS p_age,
        profiles.gender AS p_gender,
        profiles.bio AS p_bio
        FROM requests
        JOIN users ON requests.request_from = users.id
        JOIN profiles ON users.id = profiles.user_id
        WHERE requests.request_to = %s AND requests.status {status_condition};
        """

        rows = self._connection.execute(query, [requested_user_id])
        user_data = [
            Profile(
                row["u_id"],
                User(row["u_id"], row["u_username"], None, row["u_email"]),
                row["p_picture"],
                row["p_name"],
                row["p_age"],
                row["p_gender"],
                row["p_bio"],
            )
            for row in rows
        ]
        return user_data

    # Function returning a status of request between session user and accesed profile user
    # For custom reject/accept/contact details/send request button
    # “” -> “send request”
    # None -> “accept or reject”
    # True -> “match”
    # False -> “rejected”

    def get_request_status(self, session_user_id, profile_user_id):
        rows = self._connection.execute(
            "SELECT * from REQUESTS WHERE request_from = %s and request_to = %s",
            [session_user_id, profile_user_id],
        )
        if rows == []:
            return ""
        else:
            return rows[0]["status"]


# SELECT * FROM requests
# JOIN users ON requests.request_from=users.id
# JOIN profiles ON users.id=profiles.user_id
# WHERE requests.request_to=1;
