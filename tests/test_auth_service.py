from app.services.auth_service import register_user, authenticate_user
from unittest.mock import patch

@patch("app.services.auth_service.User")
def test_register_user_success(mock_user):
    response, status_code = register_user('newuser', 'new@example.com', 'securepass')
    assert status_code == 201
    assert isinstance(response, dict)
    assert response['msg'] == 'User registered successfully'

