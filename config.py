class Config(object):
    POSTGRES = {
        'user': 'test_user',
        'pw': 'test_password',
        'db': 'test_database',
        'host': 'localhost',
        'port': 5432
    }

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
