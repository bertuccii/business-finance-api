from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Sale, Expense
from flasgger import swag_from

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/summary', methods=['GET'])
@swag_from('docs/reports/summary.yml')
@jwt_required()
def get_summary_report():
    current_user = get_jwt_identity()

    total_sales = sum(sale.amount for sale in Sale.query.filter_by(user_id=current_user).all())
    total_expenses = sum(expense.amount for expense in Expense.query.filter_by(user_id=current_user).all())
    profit = total_sales - total_expenses

    report = {
        'total_sales': total_sales,
        'total_expenses': total_expenses,
        'profit': profit
    }

    return jsonify({'report': report}), 200
