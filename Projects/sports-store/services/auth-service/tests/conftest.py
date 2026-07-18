import os
from datetime import datetime, timedelta, timezone

os.environ["JWT_SECRET"] = "test-secret"

import jwt
import pytest
from fastapi.testclient import TestClient

from main import app


class AsyncCursor:
    """Minimal async iterator for mocking Motor cursors."""

    def __init__(self, items):
        self.items = list(items)

    def __aiter__(self):
        self._iter = iter(self.items)
        return self

    async def __anext__(self):
        try:
            return next(self._iter)
        except StopIteration:
            raise StopAsyncIteration


def make_token(user_id="507f1f77bcf86cd799439011", email="user@test.com",
               role="customer", expires_minutes=60):
    payload = {
        "sub": user_id,
        "email": email,
        "role": role,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=expires_minutes),
    }
    return jwt.encode(payload, "test-secret", algorithm="HS256")


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def auth_headers():
    return {"Authorization": f"Bearer {make_token()}"}


@pytest.fixture
def admin_headers():
    return {"Authorization": f"Bearer {make_token(role='admin')}"}
