from app.models import Sale
from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class SaleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Sale
        load_instance = True
        sqla_session = db.session
