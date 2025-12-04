from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.schemas.user import UserCreate

def test_get_access_token(client: TestClient, db: Session) -> None:
    email = "test@example.com"
    password = "password"
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(db, obj_in=user_in)

    login_data = {
        "username": email,
        "password": password,
    }
    r = client.post(f"/api/v1/login/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]
