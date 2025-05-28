from app.models import Expense
from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ExpenseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Expense
        load_instance = True
        sqla_session = db.session
