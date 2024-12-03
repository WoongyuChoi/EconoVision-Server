from flask import Flask
from flask_caching import Cache
from config import Config
from handler.logger import get_logger
from handler.exception_handler import register_exception_handlers

cache = Cache()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cache.init_app(app)
    app.logger = get_logger(__name__)

    register_exception_handlers(app)

    with app.app_context():
        from .server import register_routes

        register_routes(app)

    return app
