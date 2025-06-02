from app.schemas.user_schema import user_schema
from app.models import User

def test_user_schema_dump():
    user = User(id=1, username="john", email="john@example.com", password_hash="xxx")
    result = user_schema.dump(user)
    assert result["username"] == "john"
    assert "password_hash" not in result  # if excluded

def test_user_schema_load():
    data = {"username": "john", "email": "john@example.com", "password": "123456"}
    result = user_schema.load(data)
    assert result["username"] == "john"
