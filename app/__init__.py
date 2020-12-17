from flask import Flask
from config import BaseConfig


def create_app(config_class=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
