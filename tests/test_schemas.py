import pytest
from app.schemas.sale_schema import SaleSchema
from app.schemas.expense_schema import ExpenseSchema
from app.schemas.user_schema import UserSchema
from app.models import Sale, Expense, User

sale_schema = SaleSchema()
expense_schema = ExpenseSchema()
user_schema = UserSchema()

# --- Sale Schema ---

def test_sale_serialization(app):
    with app.app_context():
        sale = Sale(id=1, amount=100.0, description="Test sale")
        result = sale_schema.dump(sale)

        assert result["amount"] == 100.0
        assert result["description"] == "Test sale"

def test_sale_deserialization(app):
    with app.app_context():
        input_data = {
            "amount": 200.0,
            "description": "New sale"
        }

        result = sale_schema.load(input_data)
        assert result.amount == 200.0
        assert result.description == "New sale"

# --- Expense Schema ---

def test_expense_serialization(app):
    with app.app_context():
        expense = Expense(id=1, amount=50.0, category="Food")
        result = expense_schema.dump(expense)

        assert result["amount"] == 50.0
        assert result["category"] == "Food"

def test_expense_deserialization(app):
    with app.app_context():
        input_data = {
            "amount": 75.0,
            "category": "Transport"
        }

        result = expense_schema.load(input_data)
        assert result.amount == 75.0
        assert result.category == "Transport"

# --- User Schema ---

def test_user_serialization(app):
    with app.app_context():
        user = User(id=1, username="felipe", email="felipe@example.com")
        result = user_schema.dump(user)

        assert result["username"] == "felipe"
        assert result["email"] == "felipe@example.com"

def test_user_deserialization(app):
    with app.app_context():
        input_data = {
            "username": "ana",
            "email": "ana@example.com"
        }

        result = user_schema.load(input_data)
        assert result.username == "ana"
        assert result.email == "ana@example.com"
