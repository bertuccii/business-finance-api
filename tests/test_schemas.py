import pytest
from app.schemas.sale_schema import SaleSchema
from app.schemas.expense_schema import ExpenseSchema
from app.schemas.user_schema import UserSchema
from app.models import Sale, Expense, User

sale_schema = SaleSchema()
expense_schema = ExpenseSchema()
user_schema = UserSchema()

# --- Sale Schema ---

def test_sale_serialization():
    sale = Sale(id=1, amount=100.0, description="Test sale", user_id=1)
    result = sale_schema.dump(sale)

    assert result["id"] == 1
    assert result["amount"] == 100.0
    assert result["description"] == "Test sale"
    assert result["user_id"] == 1

def test_sale_deserialization():
    input_data = {
        "amount": 200.0,
        "description": "New sale",
        "user_id": 2
    }

    result = sale_schema.load(input_data)
    assert result.amount == 200.0
    assert result.description == "New sale"
    assert result.user_id == 2

# --- Expense Schema ---

def test_expense_serialization():
    expense = Expense(id=1, amount=50.0, category="Food", user_id=1)
    result = expense_schema.dump(expense)

    assert result["id"] == 1
    assert result["amount"] == 50.0
    assert result["category"] == "Food"
    assert result["user_id"] == 1

def test_expense_deserialization():
    input_data = {
        "amount": 75.0,
        "category": "Transport",
        "user_id": 2
    }

    result = expense_schema.load(input_data)
    assert result.amount == 75.0
    assert result.category == "Transport"
    assert result.user_id == 2

# --- User Schema ---

def test_user_serialization():
    user = User(id=1, username="felipe", email="felipe@example.com")
    result = user_schema.dump(user)

    assert result["id"] == 1
    assert result["username"] == "felipe"
    assert result["email"] == "felipe@example.com"
    assert "password_hash" not in result  # ensure it's excluded

def test_user_deserialization():
    input_data = {
        "username": "ana",
        "email": "ana@example.com",
        "password": "secret123",  # even if unused, test safe handling
        "user_id": 3
    }

    result = user_schema.load(input_data)
    assert result.username == "ana"
    assert result.email == "ana@example.com"
