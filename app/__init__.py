from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
swagger = Swagger()

def create_app(config_class='config.DevelopmentConfig'):
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)  # Para permitir requisições de outros domínios
    swagger.init_app(app)

    # Importar e registrar Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.sales_routes import sales_bp
    from app.routes.expenses_routes import expenses_bp
    from app.routes.reports_routes import reports_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(sales_bp, url_prefix='/sales')
    app.register_blueprint(expenses_bp, url_prefix='/expenses')
    app.register_blueprint(reports_bp, url_prefix='/reports')

    return app
