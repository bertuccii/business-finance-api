import pytest
from app import create_app, db
from app.models import User, Sale, Expense

@pytest.fixture(scope="module")
def app():
    app = create_app('config.TestingConfig')  # Use a config with a test DB
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope="function")
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def clean_db():
    """Clean database after each test function automatically."""
    yield
    db.session.rollback()
    db.session.query(Sale).delete()
    db.session.query(Expense).delete()
    db.session.query(User).delete()
    db.session.commit()
