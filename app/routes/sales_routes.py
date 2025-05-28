from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Sale
from flasgger import swag_from

sales_bp = Blueprint('sales', __name__)

@sales_bp.route('/', methods=['POST'])
@swag_from('docs/sales/create.yml')
@jwt_required()
def create_sale():
    data = request.get_json()
    if not data or not data.get('amount'):
        return jsonify({'msg': 'Amount is required'}), 400

    current_user = int(get_jwt_identity())

    new_sale = Sale(
        amount=data['amount'],
        description=data.get('description', ''),
        user_id=current_user
    )

    db.session.add(new_sale)
    db.session.commit()

    return jsonify({'msg': 'Sale created successfully', 'sale_id': new_sale.id}), 201

@sales_bp.route('/', methods=['GET'])
@swag_from('docs/sales/list.yml')
@jwt_required()
def get_sales():
    current_user = int(get_jwt_identity())
    sales = Sale.query.filter_by(user_id=current_user).all()

    sales_list = [
        {
            'id': sale.id,
            'amount': sale.amount,
            'description': sale.description,
            'date': sale.date.isoformat()
        }
        for sale in sales
    ]

    return jsonify({'sales': sales_list}), 200

@sales_bp.route('/<int:sale_id>', methods=['PUT'])
@swag_from('docs/sales/update.yml')
@jwt_required()
def update_sale(sale_id):
    data = request.get_json()
    current_user = int(get_jwt_identity())

    sale = Sale.query.filter_by(id=sale_id, user_id=current_user).first()
    if not sale:
        return jsonify({'msg': 'Sale not found'}), 404

    sale.amount = data.get('amount', sale.amount)
    sale.description = data.get('description', sale.description)

    db.session.commit()

    return jsonify({'msg': 'Sale updated successfully'}), 200

@sales_bp.route('/<int:sale_id>', methods=['DELETE'])
@swag_from('docs/sales/delete.yml')
@jwt_required()
def delete_sale(sale_id):
    current_user = int(get_jwt_identity())

    sale = Sale.query.filter_by(id=sale_id, user_id=current_user).first()
    if not sale:
        return jsonify({'msg': 'Sale not found'}), 404

    db.session.delete(sale)
    db.session.commit()

    return jsonify({'msg': 'Sale deleted successfully'}), 200
