from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Sale, Expense
from flasgger import swag_from
import os
from app.services import report_service
DOCS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'docs'))

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/summary', methods=['GET'])
@swag_from(os.path.join(DOCS_PATH, 'reports', 'summary.yml'))
@jwt_required()
def get_summary_report():
    user_id = get_jwt_identity()

    report = report_service.generate_summary_report(user_id=user_id)

    

    return jsonify({'report': report}), 200
