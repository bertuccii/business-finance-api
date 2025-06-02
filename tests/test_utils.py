from app.utils import hash_password, verify_password

def test_hash_password_returns_different_string():
    password = "mysecret123"
    hashed = hash_password(password)

    assert hashed != password
    assert isinstance(hashed, str)
    assert hashed.startswith("pbkdf2:")

def test_verify_password_success():
    password = "mysecret123"
    hashed = hash_password(password)

    assert verify_password(hashed, password) is True

def test_verify_password_failure():
    password = "mysecret123"
    wrong_password = "wrongpass"
    hashed = hash_password(password)

    assert verify_password(hashed, wrong_password) is False
