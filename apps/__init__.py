from flask import Flask
import settings
from apps.blueprints.auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    app.register_blueprint(auth_bp)
    return app