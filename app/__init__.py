from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from app.config import app_config
from database.db import db, initialize_db
from users.db.models import User
from users.routes import initialize_users_routes


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    initialize_db(app)
    api = Api(app)
    jwt = JWTManager(app)
    initialize_users_routes(api)

    return app
