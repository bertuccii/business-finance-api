from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Expense
from flasgger import swag_from
import os
DOCS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'docs'))

expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route('/', methods=['POST'])
@swag_from(os.path.join(DOCS_PATH, 'expenses', 'create.yml'))
@jwt_required()
def create_expense():
    data = request.get_json()
    if not data or not data.get('amount'):
        return jsonify({'msg': 'Amount is required'}), 400

    current_user = get_jwt_identity()

    new_expense = Expense(
        amount=data['amount'],
        category=data.get('category', ''),
        user_id=current_user
    )

    db.session.add(new_expense)
    db.session.commit()

    return jsonify({'msg': 'Expense created successfully', 'expense_id': new_expense.id}), 201

@expenses_bp.route('/', methods=['GET'])
@swag_from(os.path.join(DOCS_PATH, 'expenses', 'list.yml'))
@jwt_required()
def get_expenses():
    current_user = get_jwt_identity()
    expenses = Expense.query.filter_by(user_id=current_user).all()

    expenses_list = [
        {
            'id': expense.id,
            'amount': expense.amount,
            'category': expense.category,
            'date': expense.date.isoformat()
        }
        for expense in expenses
    ]

    return jsonify({'expenses': expenses_list}), 200

@expenses_bp.route('/<int:expense_id>', methods=['PUT'])
@swag_from(os.path.join(DOCS_PATH, 'expenses', 'update.yml'))
@jwt_required()
def update_expense(expense_id):
    data = request.get_json()
    current_user = get_jwt_identity()

    expense = Expense.query.filter_by(id=expense_id, user_id=current_user).first()
    if not expense:
        return jsonify({'msg': 'Expense not found'}), 404

    expense.amount = data.get('amount', expense.amount)
    expense.category = data.get('category', expense.category)

    db.session.commit()

    return jsonify({'msg': 'Expense updated successfully'}), 200

@expenses_bp.route('/<int:expense_id>', methods=['DELETE'])
@swag_from(os.path.join(DOCS_PATH, 'expenses', 'delete.yml'))
@jwt_required()
def delete_expense(expense_id):
    current_user = get_jwt_identity()

    expense = Expense.query.filter_by(id=expense_id, user_id=current_user).first()
    if not expense:
        return jsonify({'msg': 'Expense not found'}), 404

    db.session.delete(expense)
    db.session.commit()

    return jsonify({'msg': 'Expense deleted successfully'}), 200
