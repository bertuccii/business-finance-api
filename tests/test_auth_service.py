from app.services.auth_service import register_user, authenticate_user
from unittest.mock import patch

@patch("app.services.auth_service.User")
def test_register_user_success(MockUser):
    db_mock = patch("app.services.auth_service.db").start()
    token = register_user(username= "test", email= "t@example.com", password= "pass123")
    assert isinstance(token, str)

