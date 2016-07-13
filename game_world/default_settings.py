class Config(object):
    '''
    base configuration class
    '''
    USER = 'root'
    PASSWORD = 'lf721521'
    # HOST = 'ec2-54-200-98-228.us-west-2.compute.amazonaws.com:3306'
    HOST = '54.200.98.228:3306'
    DB = 'server'
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % (
        USER,
        PASSWORD,
        HOST,
        DB
    )

    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
