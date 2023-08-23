class BaseConfig:
    SECRET_KEY = 'your-secret-key'
    DEBUG = False


class LocalConfig(BaseConfig):
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # Add more configuration settings for development


class ProductionConfig(BaseConfig):
    DEBUG = False
    # Add more configuration settings for production
