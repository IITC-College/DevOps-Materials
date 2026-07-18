from unittest.mock import AsyncMock, MagicMock, patch

import jwt
from pymongo.errors import DuplicateKeyError

from security import hash_password
from tests.conftest import make_token

USER_ID = "507f1f77bcf86cd799439011"

REGISTER_PAYLOAD = {
    "email": "daniel@example.com",
    "password": "Str0ngPass!",
    "full_name": "Daniel Cohen",
}

STORED_USER = {
    "_id": USER_ID,
    "email": "daniel@example.com",
    "password_hash": hash_password("Str0ngPass!"),
    "full_name": "Daniel Cohen",
    "role": "customer",
}


def test_register_returns_201_and_public_user(client):
    with patch("routes.auth.users_collection") as mock_col:
        mock_col.insert_one = AsyncMock(return_value=MagicMock(inserted_id=USER_ID))
        response = client.post("/api/auth/register", json=REGISTER_PAYLOAD)

    assert response.status_code == 201
    body = response.json()
    assert body == {
        "id": USER_ID,
        "email": "daniel@example.com",
        "full_name": "Daniel Cohen",
        "role": "customer",
    }
    inserted = mock_col.insert_one.call_args.args[0]
    assert "password" not in inserted
    assert inserted["password_hash"] != REGISTER_PAYLOAD["password"]
    assert inserted["role"] == "customer"


def test_register_duplicate_email_409(client):
    with patch("routes.auth.users_collection") as mock_col:
        mock_col.insert_one = AsyncMock(side_effect=DuplicateKeyError("dup"))
        response = client.post("/api/auth/register", json=REGISTER_PAYLOAD)

    assert response.status_code == 409


def test_register_short_password_422(client):
    payload = dict(REGISTER_PAYLOAD, password="short")
    response = client.post("/api/auth/register", json=payload)
    assert response.status_code == 422


def test_login_returns_decodable_token(client):
    with patch("routes.auth.users_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=STORED_USER.copy())
        response = client.post(
            "/api/auth/login",
            json={"email": "daniel@example.com", "password": "Str0ngPass!"},
        )

    assert response.status_code == 200
    body = response.json()
    assert body["token_type"] == "bearer"
    assert body["user"]["email"] == "daniel@example.com"
    claims = jwt.decode(body["access_token"], "test-secret", algorithms=["HS256"])
    assert claims["sub"] == USER_ID
    assert claims["role"] == "customer"


def test_login_wrong_password_401(client):
    with patch("routes.auth.users_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=STORED_USER.copy())
        response = client.post(
            "/api/auth/login",
            json={"email": "daniel@example.com", "password": "WrongPass1"},
        )

    assert response.status_code == 401


def test_login_unknown_email_401(client):
    with patch("routes.auth.users_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=None)
        response = client.post(
            "/api/auth/login",
            json={"email": "nobody@example.com", "password": "Str0ngPass!"},
        )

    assert response.status_code == 401


def test_me_returns_current_user(client, auth_headers):
    from bson import ObjectId

    stored = dict(STORED_USER, _id=ObjectId(USER_ID))
    with patch("routes.auth.users_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=stored)
        response = client.get("/api/auth/me", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["id"] == USER_ID


def test_me_without_token_401(client):
    response = client.get("/api/auth/me")
    assert response.status_code == 401


def test_me_expired_token_401(client):
    token = make_token(expires_minutes=-5)
    response = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Token expired"
