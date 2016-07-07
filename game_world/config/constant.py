class DbConfig(object):
    '''
    constants about Databases
    '''

    USER = 'root'
    PASSWORD = 'lf721521'
    # HOST = 'ec2-54-200-98-228.us-west-2.compute.amazonaws.com:3306'
    HOST = '54.200.98.228:3306'
    DB = 'server'

    @classmethod
    def get_db_uri(cls):
        db_uri = 'mysql://%s:%s@%s/%s' % (
            DbConfig.USER,
            DbConfig.PASSWORD,
            DbConfig.HOST,
            DbConfig.DB
        )

        return db_uri
