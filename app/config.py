import os


class Config(object):
    """Parent configuration class."""

    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET")
    MONGO_DATABASE_URI = os.getenv("DATABASE_URL")


class DevelopmentConfig(Config):
    """Configurations for Development."""

    DEBUG = True
    ENV = "development"
    MONGODB_SETTINGS = {"host": "mongodb://localhost:27017/bankapp"}


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