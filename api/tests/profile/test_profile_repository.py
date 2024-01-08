from lib.Profile_repository import ProfileRepository
from lib.Profile import Profile
from lib.User import User

"""
Test if all profiles retrieved
"""


def test_get_all_users(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = ProfileRepository(db_connection)
    assert repository.all() == [
        Profile(
            1,
            User(1, "amina", None, "amina@gmail.com"),
            "https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg",
            "Amina",
            "28",
            "Female",
            "Test bio Amina",
        ),
        Profile(
            2,
            User(2, "daniel", None, "daniel@gmail.com"),
            "https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg",
            "Daniel",
            "24",
            "Male",
            "Test bio Daniel",
        ),
        Profile(
            3,
            User(3, "piotr", None, "piotr@gmail.com"),
            "https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg",
            "Piotr",
            "33",
            "Male",
            "Test bio Piotr",
        ),
        Profile(
            4,
            User(4, "david", None, "david1@gmail.com"),
            "https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg",
            "David",
            "24",
            "Male",
            "Test bio David",
        ),
    ]


def test_get_profile_by_user_id(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = ProfileRepository(db_connection)
    assert repository.find_by_user_id(2) == Profile(
        2,
        User(2, "daniel", None, "daniel@gmail.com"),
        "https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg",
        "Daniel",
        "24",
        "Male",
        "Test bio Daniel",
    )
