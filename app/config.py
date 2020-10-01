import os


class Config(object):
    """Parent configuration class."""

    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET")
    MONGODB_SETTINGS = {"host": "mongodb://localhost:27017/bankapp"}
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_CSRF_CHECK_FORM = True


class DevelopmentConfig(Config):
    """Configurations for Development."""

    PORT = 8000
    DEBUG = True
    ENV = "development"


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""

    TESTING = True
    MONGODB_SETTINGS = {"host": "mongodb://localhost:27017/testingbankapp"}
    DEBUG = True
    ENV = "testing"


class StagingConfig(Config):
    """Configurations for Staging."""

    DEBUG = True
    ENV = "staging"


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False
    ENV = "production"


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}