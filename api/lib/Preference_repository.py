from lib.Preference import Preference


class PreferenceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM preferences")
        preferences = [
            Preference(
                row["id"],
                row["user_id"],
                row["age_slot"],
                row["gender"],
                row["continent"],
                row["season"],
                row["category"],
            )
            for row in rows
        ]
        return preferences

    def find_by_user_id(self, user_id):
        rows = self._connection.execute(
            "SELECT * from PREFERENCES WHERE user_id = %s", [user_id]
        )
        if rows:
            row = rows[0]
            return Preference(
                row["id"],
                row["user_id"],
                row["age_slot"],
                row["gender"],
                row["continent"],
                row["season"],
                row["category"],
            )
        return []


    """
    method interacting with database table 
    if condition update: changing already existing preferences data set
    if condition insert: adding new preferences data set
    """
    def setup_preferences(self, preference_object, condition):
        match condition:
            case "update":
                self._connection.execute(
                    """
                    UPDATE preferences SET age_slot = %s, gender = %s, continent = %s, season = %s, category = %s
                    WHERE user_id = %s;
                    """,
                    [
                        preference_object.age_slot,
                        preference_object.gender,
                        preference_object.continent,
                        preference_object.season,
                        preference_object.category,
                        preference_object.user_id,
                    ],
                )
            case "insert":
                self._connection.execute(
                    """
                    INSERT INTO preferences (user_id, age_slot, gender, continent, season, category)
                    VALUES (%s, %s, %s, %s, %s, %s);
                    """,
                    [
                        preference_object.user_id,
                        preference_object.age_slot,
                        preference_object.gender,
                        preference_object.continent,
                        preference_object.season,
                        preference_object.category,
                    ],
                )
