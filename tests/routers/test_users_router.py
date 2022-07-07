from fastapi import FastAPI
from fastapi.testclient import TestClient

import pytest_asyncio
from tidskrift.db import get_db
from tidskrift.db.queries import userquery
from tidskrift.model.api.user import NewUser, User
from tidskrift.routers import users


@pytest_asyncio.fixture
async def usersclient() -> TestClient:
    api = FastAPI()
    api.include_router(users.router)
    yield TestClient(api)


async def test_users_router_create_new_user_ok(usersclient: TestClient):
    nu = NewUser(
        username="test-username",
        password="test-password",
        first_name="test-fn",
        last_name="test-ln",
        email="test-email",
    )

    response = usersclient.post("/users/", json=nu.dict())

    user = User(**response.json())

    assert response.status_code == 201
    assert user.username == nu.username
    assert user.first_name == nu.first_name

    # usersclient.delete("/users/test-username")
