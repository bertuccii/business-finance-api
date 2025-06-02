from app.services.report_service import generate_summary_report

def test_generate_report():
    summary = generate_report(user_id=1)
    assert "total_sales" in summary
    assert "total_expenses" in summary
    assert "profit" in summary
