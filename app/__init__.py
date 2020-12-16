from flask import Flask
from config import BaseConfig
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_class=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
