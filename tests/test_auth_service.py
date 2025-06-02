from app.services.auth_service import register_user, authenticate_user
from unittest.mock import patch

@patch("app.services.auth_service.User")
def test_register_user_success(MockUser):
    user_data = {"username": "test", "email": "t@example.com", "password": "pass123"}
    db_mock = patch("app.services.auth_service.db").start()
    token = register_user(user_data)
    assert isinstance(token, str)
