from app.services.auth_service import register_user

def test_register_user_success(app):
    with app.app_context():
        response, status_code = register_user('newuser', 'new@example.com', 'securepass')
        assert status_code == 201
        assert response['msg'] == 'User registered successfully'
