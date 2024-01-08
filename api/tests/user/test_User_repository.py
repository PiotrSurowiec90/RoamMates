from lib.User_repository import UserRepository
from lib.Profile_repository import ProfileRepository
from lib.User import User
from lib.Profile import Profile


"""
Test if user by id found
"""


def test_find_user_by_id(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.find_by_id(1) == User(1, "amina", "amina1", "amina@gmail.com")


"""
Test if user by email found
"""


def test_find_user_by_email_none(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.find_by_email("amina@gmail.com") == User(
        1, "amina", "amina1", "amina@gmail.com"
    )


"""
Test if user by email not found
"""


def test_find_user_by_email_none(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.find_by_email("nonexistingemail@gmail.com") == []


"""
Test if user email and password is in database for login attempt
"""


def test_check_login_details(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.check_login_details("amina@gmail.com", "amina1") == True


def test_check_login_details_password_incorrect(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.check_login_details("amina@gmail.com", "amina5") == False


def test_check_login_details_email_incorrect(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.check_login_details("amina@gmail.co.uk", "amina1") == False


def test_check_login_details_password(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.check_login_details("amina@gmail.co.uk", "daniel1") == False


"""
Test if new user and profile added
"""


def test_add_new_user(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    user_repo = UserRepository(db_connection)
    profile_repo = ProfileRepository(db_connection)

    new_user = User(None, "test", "testpassword", "testemail")
    user_repo.add(new_user)

    assert user_repo.all()[-1] == User(5, "test", "testpassword", "testemail")

    assert profile_repo.all()[-1] == Profile(
        5, User(5, "test", None, "testemail"), None, None, None, None, None
    )
