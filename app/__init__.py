from flask import Flask
from flask.sansio.app import App
from config import ProductionConfig, DevelopmentConfig
from app.routes.login import auth_bp
from flask_cors import CORS
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)
    
    CORS(app, supports_credentials=True)
    jwt = JWTManager()

    app.register_blueprint(auth_bp)
    jwt.init_app(app)

    return app

