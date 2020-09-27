from flask import Flask
from flask_restful import Resource, Api

from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    api = Api(app)

    return app
