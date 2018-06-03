import os


class Config(object):
    """Parent configurationclass."""
    
    DEBUG = True

    CSRF_ENABLED = True

    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")

class DevelopmentConfig(Config):
    """ configurations for Development"""
    DEBUG = True

class TestingConfig(Config):
    """configurations for testing """
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """Configurations for staging"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for production"""
    DEBUG = False
    TESTING = False

app_config = {

    "development": DevelopmentConfig,
    "testing" : TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}


