from fastapi.testclient import TestClient

def test_create_user_success(client: TestClient):
    response = client.post(
        "/auth/users",
        json={"email": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_create_user_duplicate_email(client: TestClient):
    # First, create a user
    client.post(
        "/auth/users",
        json={"email": "test2@example.com", "password": "password123"},
    )
    # Now, try to create another with the same email
    response = client.post(
        "/auth/users",
        json={"email": "test2@example.com", "password": "password123"},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_create_user_invalid_password(client: TestClient):
    response = client.post(
        "/auth/users",
        json={"email": "test3@example.com", "password": "short"},
    )
    assert response.status_code == 422
