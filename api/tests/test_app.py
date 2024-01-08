import json
from playwright.sync_api import Page, expect
from token_config import token_generator
import unittest


"""
Check if server returns "OK" response 
when request to /users/add correct
"""


def test_user_signup_success(web_client, test_web_address):
    response = web_client.post(
        f"http://{test_web_address}/users/add",
        json={
            "email": "test@example.com",
            "password": "test_password",
            "username": "test_username",
        },
    )

    assert response.status_code == 200
    assert response.get_json().get("message") == "OK!"


"""
Check if server returns 401 response 
when request to /users/add incorrect - duplicate email
"""


def test_user_signup_fail(web_client, test_web_address):
    response = web_client.post(
        f"http://{test_web_address}/users/add",
        json={
            "email": "amina@gmail.com",
            "password": "test_password",
            "username": "test_username",
        },
    )

    assert response.status_code == 401
    assert response.get_json().get("message") == "Credentials error"


"""
Check if server returns "OK" response 
when request to /users/authentication correct
"""


def test_user_login(web_client, test_web_address):
    response = web_client.post(
        f"http://{test_web_address}/users/authentication",
        json={"email": "amina@gmail.com", "password": "amina1"}
        # data={"email": "amina@gmail.com", "password": "amina1"},
    )

    assert response.status_code == 200
    assert response.get_json().get("message") == "OK!"


"""
Check if server returns "Invalid credentials" response 
when request to /users/authentication incorrect
"""


def test_user_login_fail(web_client, test_web_address):
    response = web_client.post(
        f"http://{test_web_address}/users/authentication",
        json={"email": "amina@gmail.com", "password": "wrong_password"},
    )

    assert response.status_code == 401
    assert response.get_json().get("message") == "Invalid credentials"


"""
Check if server returns "OK" response 
when request to /profiles/data correct
"""


def test_user_data(web_client, test_web_address):
    token_mock = token_generator(1)
    session_data = {"user_id": 1}

    # Session context manager to mock session data
    with web_client.session_transaction() as sess:
        sess.update(session_data)

    response = web_client.get(
        f"http://{test_web_address}/profiles/data",
        headers={"Authorization": f"Bearer {token_mock}"},
    )
    print("RESPONSE HEADERS:", response.headers)
    print("RESPONSE CONTENT:", response.get_data(as_text=True))
    assert response.status_code == 200
    assert response.get_json().get("message") == "OK!"
    assert response.get_json().get("users")[0] == {
        "age": "28",
        "bio": "Test bio Amina",
        "gender": "Female",
        "name": "Amina",
        "picture": "https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg",
        "user": {
            "email": "amina@gmail.com",
            "id": 1,
            "password": None,
            "username": "amina",
        },
        "user_id": 1,
    }


"""
Check if server returns "Invalid credentials" response 
when request to /profiles/data incorrect
"""


def test_user_data_fail(web_client, test_web_address):
    token_mock = token_generator(2)
    session_data = {"user_id": 1}

    # Session context manager to mock session data
    with web_client.session_transaction() as sess:
        sess.update(session_data)

    response = web_client.get(
        f"http://{test_web_address}/profiles/data",
        headers={"Authorization": f"Bearer {token_mock}"},
    )

    assert response.status_code == 401
    assert response.get_json().get("message") == "Invalid credentials"


"""
Check if server returns "OK" response 
when request to /requests/null
"""


def test_requests_null(web_client, test_web_address):
    token_mock = token_generator(2)
    session_data = {"user_id": 2}

    # Session context manager to mock session data
    with web_client.session_transaction() as sess:
        sess.update(session_data)

    response = web_client.get(
        f"http://{test_web_address}/requests/null",
        headers={"Authorization": f"Bearer {token_mock}"},
    )

    assert response.status_code == 200
    assert response.get_json().get("message") == "OK!"
    assert response.get_json().get("users")[0] == {
        "age": "28",
        "bio": "Test bio Amina",
        "gender": "Female",
        "name": "Amina",
        "picture": "https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg",
        "user": {
            "email": "amina@gmail.com",
            "id": 1,
            "password": None,
            "username": "amina",
        },
        "user_id": 1,
    }


"""
Check if server returns "Invalid credentials" response 
when request to /requests/null
"""


def test_requests_null_fail(web_client, test_web_address):
    token_mock = token_generator(2)
    session_data = {"user_id": 1}

    # Session context manager to mock session data
    with web_client.session_transaction() as sess:
        sess.update(session_data)

    response = web_client.get(
        f"http://{test_web_address}/requests/null",
        headers={"Authorization": f"Bearer {token_mock}"},
    )

    assert response.status_code == 401
    assert response.get_json().get("message") == "Invalid credentials"


"""
Check if server returns "OK" response 
when request to /requests/true
"""


"""
Check if server returns "Invalid credentials" response 
when request to /requests/true
"""


def test_requests_true_fail(web_client, test_web_address):
    token_mock = token_generator(2)
    session_data = {"user_id": 1}

    # Session context manager to mock session data
    with web_client.session_transaction() as sess:
        sess.update(session_data)

    response = web_client.get(
        f"http://{test_web_address}/requests/true",
        headers={"Authorization": f"Bearer {token_mock}"},
    )

    assert response.status_code == 401
    assert response.get_json().get("message") == "Invalid credentials"


"""
Check if server returns "OK" response 
when request to /profiles/user_id
"""


def test_profiles_data(web_client, test_web_address):
    token_mock = token_generator(1)
    session_data = {"user_id": 1}

    # Session context manager to mock session data
    with web_client.session_transaction() as sess:
        sess.update(session_data)

    response = web_client.get(
        f"http://{test_web_address}/profiles/1",
        headers={"Authorization": f"Bearer {token_mock}"},
    )

    assert response.status_code == 200
    assert response.get_json().get("message") == "OK!"
    assert response.get_json().get("profile") == {
        "email": "amina@gmail.com",
        "id": 1,
        "password": "amina1",
        "username": "amina",
    }
    assert response.get_json().get("preferences") == {
        "age_slot": "[18, 24]",
        "category": "resort",
        "continent": "North America",
        "gender": "other",
        "id": 1,
        "season": "winter",
        "user_id": 1,
    }
    assert response.get_json().get("user_request_status") == ""


"""
Check if server returns "Invalid credentials" response 
when request to /profiles/user_id
"""


def test_profiles_data_fail(web_client, test_web_address):
    token_mock = token_generator(2)
    session_data = {"user_id": 1}

    # Session context manager to mock session data
    with web_client.session_transaction() as sess:
        sess.update(session_data)

    response = web_client.get(
        f"http://{test_web_address}/profiles/1",
        headers={"Authorization": f"Bearer {token_mock}"},
    )

    assert response.status_code == 401
    assert response.get_json().get("message") == "Invalid credentials"


"""
Check if server returns OK response when 
requests to /preferences/new
when user is new
"""


def test_preferences_setup_new_user(web_client, test_web_address):
    token_mock = token_generator(3)
    session_data = {"user_id": 3}

    # Session context manager to mock session data
    with web_client.session_transaction() as sess:
        sess.update(session_data)

    response = web_client.post(
        f"http://{test_web_address}/preferences/new",
        json={
            "age_slot": "[30, 100]",
            "gender": "other",
            "continent": "Asia",
            "season": "summer",
            "category": "beach",
        },
        headers={"Authorization": f"Bearer {token_mock}"},
    )

    assert response.status_code == 200
    assert response.get_json().get("message") == "OK!"


"""
Check if server returns OK response when 
requests to /preferences/new
when user already exists
"""


def test_preferences_setup_existing_user(web_client, test_web_address):
    token_mock = token_generator(1)
    session_data = {"user_id": 1}

    # Session context manager to mock session data
    with web_client.session_transaction() as sess:
        sess.update(session_data)

    response = web_client.post(
        f"http://{test_web_address}/preferences/new",
        json={
            "age_slot": "[30, 100]",
            "gender": "other",
            "continent": "Asia",
            "season": "summer",
            "category": "beach",
        },
        headers={"Authorization": f"Bearer {token_mock}"},
    )

    assert response.status_code == 200
    assert response.get_json().get("message") == "OK!"


"""
Check if server returns 401 response when 
requests to /preferences/new
when user is new
"""


def test_preferences_setup_new_user_fail(web_client, test_web_address):
    token_mock = token_generator(2)
    session_data = {"user_id": 3}

    # Session context manager to mock session data
    with web_client.session_transaction() as sess:
        sess.update(session_data)

    response = web_client.post(
        f"http://{test_web_address}/preferences/new",
        json={
            "age_slot": "[30, 100]",
            "gender": "other",
            "continent": "Asia",
            "season": "summer",
            "category": "beach",
        },
        headers={"Authorization": f"Bearer {token_mock}"},
    )

    assert response.status_code == 401
    assert response.get_json().get("message") == "Invalid credentials"


"""
Check if server returns 401 response when 
requests to /preferences/new
when user already exists
"""


def test_preferences_setup_existing_user_fail(web_client, test_web_address):
    token_mock = token_generator(2)
    session_data = {"user_id": 1}

    # Session context manager to mock session data
    with web_client.session_transaction() as sess:
        sess.update(session_data)

    response = web_client.post(
        f"http://{test_web_address}/preferences/new",
        json={
            "age_slot": "[30, 100]",
            "gender": "other",
            "continent": "Asia",
            "season": "summer",
            "category": "beach",
        },
        headers={"Authorization": f"Bearer {token_mock}"},
    )

    assert response.status_code == 401
    assert response.get_json().get("message") == "Invalid credentials"
