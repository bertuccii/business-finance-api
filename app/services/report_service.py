from app.models import Sale, Expense

def generate_summary_report(user_id):
    total_sales = sum(sale.amount for sale in Sale.query.filter_by(user_id=user_id).all())
    total_expenses = sum(expense.amount for expense in Expense.query.filter_by(user_id=user_id).all())
    profit = total_sales - total_expenses

    return {
        'total_sales': total_sales,
        'total_expenses': total_expenses,
        'profit': profit
    }
