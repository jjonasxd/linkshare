from flask import Flask
from flask.sansio.app import App
from config import ProductionConfig
from app.routes.login import BP_login
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config.from_object(ProductionConfig)

    app.register_blueprint(BP_login)

    return app

