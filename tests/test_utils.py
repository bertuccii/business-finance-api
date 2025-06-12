from app.utils import hash_password, verify_password

def test_hash_password_returns_different_string(app):
    with app.app_context():
        password = "mysecret123"
        hashed = hash_password(password)

        assert isinstance(hashed, str)
        assert hashed != password
        assert ":" in hashed  

def test_verify_password_success(app):
    with app.app_context():
        password = "mysecret123"
        hashed = hash_password(password)

        assert verify_password(hashed, password) is True

def test_verify_password_failure(app):
    with app.app_context():
        password = "mysecret123"
        wrong_password = "wrongpass"
        hashed = hash_password(password)

        assert verify_password(hashed, wrong_password) is False
