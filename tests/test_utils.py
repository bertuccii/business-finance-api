from app.utils import hash_password, verify_password

def test_password_hashing_and_verification():
    password = "mypassword"
    hashed = hash_password(password)
    assert verify_password(password, hashed)
