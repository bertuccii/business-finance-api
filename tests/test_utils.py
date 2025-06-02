from app.utils import hash_password, verify_password

def test_hash_password_returns_different_string():
    password = "mysecret123"
    hashed = hash_password(password)

    assert isinstance(hashed, str)
    assert hashed != password  # Ensure the password is hashed

def test_verify_password_success():
    password = "mysecret123"
    hashed = hash_password(password)

    assert verify_password(password, hashed) is True

def test_verify_password_failure():
    password = "mysecret123"
    hashed = hash_password(password)

    assert verify_password("wrongpassword", hashed) is False
