from app.services.report_service import generate_summary_report

from app import create_app

def test_generate_report():
    app = create_app()
    with app.app_context():
        summary = generate_summary_report(user_id=1)
        assert "total_sales" in summary
        assert "total_expenses" in summary
        assert "profit" in summary
