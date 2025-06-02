from app.services.report_service import generate_summary_report
from app.models import Sale, Expense
from app import db

def test_generate_report(app):
    with app.app_context():
        db.session.add(Sale(amount=100, user_id=1))
        db.session.add(Expense(amount=40, user_id=1))
        db.session.commit()

        summary = generate_summary_report(user_id=1)
        assert summary["total_sales"] == 100
        assert summary["total_expenses"] == 40
        assert summary["profit"] == 60
