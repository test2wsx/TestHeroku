#config.py

import os


class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    pass

app_config = {
    'development': DevelopmentConfig,
    #'production': ProductionConfig
}
