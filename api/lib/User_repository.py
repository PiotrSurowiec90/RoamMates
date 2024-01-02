from lib.User import User


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from USERS")
        users = [
            User(row["id"], row["username"], row["password"], row["email"])
            for row in rows
        ]
        return users

# TODO: not needed, signup will be handled through profiles as they include User object now
    def add(self, user_object):
        self._connection.execute(
            "INSERT INTO users (username, password, email) VALUES (%s, %s, %s);",
            [user_object.username, user_object.password, user_object.email],
        )

    def find_by_id(self, user_id):
        rows = self._connection.execute("SELECT * from USERS WHERE id = %s", [user_id])
        row = rows[0]
        return User(row["id"], row["username"], row["password"], row["email"])

    def find_by_email(self, user_id):
        rows = self._connection.execute(
            "SELECT * from USERS WHERE email = %s", [user_id]
        )

        if rows:
            row = rows[0]
            return User(row["id"], row["username"], row["password"], row["email"])
        return []

    def check_login_details(self, email: str, password_attempt: str):
        query = "SELECT * FROM users WHERE email = %s AND password = %s"

        params = [email, password_attempt]
        rows = self._connection.execute(query, params)
        if rows == []:
            return False
        return True
