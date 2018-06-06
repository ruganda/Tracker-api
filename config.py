import os


class Config:
    SECRET_KEY = os.urandom(24) or 'donttouch'
    JWT_SECRET_KEY = 'donttouch'
    FLASK_APP="run.py"
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    JWT_SECRET_KEY = 'donttouch' 

class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
