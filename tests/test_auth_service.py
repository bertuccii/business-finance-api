import uuid

def test_register_user_success(app):
    from app.services.auth_service import register_user

    with app.app_context():
        unique_id = str(uuid.uuid4())[:8]
        username = f"user_{unique_id}"
        email = f"{unique_id}@example.com"
        response, status_code = register_user(username, email, 'securepass')
        assert status_code == 201
        assert response['msg'] == 'User created successfully'
