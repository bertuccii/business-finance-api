from app.services.auth_service import register_user
from unittest.mock import patch, MagicMock

@patch("app.services.auth_service.User")
def test_register_user_success(mock_user_class):
    # Configura o mock para simular "usuário não encontrado"
    mock_query = MagicMock()
    mock_query.filter.return_value.first.return_value = None
    mock_user_class.query = mock_query

    # Simula o commit do db
    mock_user_instance = MagicMock()
    mock_user_class.return_value = mock_user_instance

    response, status_code = register_user('newuser1', 'new1@example.com', 'securepass1')
    assert status_code == 201
    assert isinstance(response, dict)
    assert response['msg'] == 'User registered successfully'
