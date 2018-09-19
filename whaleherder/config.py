class Config:
    FLASK_APP = 'whaleherder'
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(Config):
    ENV = 'production'
