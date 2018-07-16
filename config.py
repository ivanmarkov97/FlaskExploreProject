class Config(object):
    POSTGRES = {
        'user': 'test_user',
        'pw': 'test_password',
        'db': 'test_database',
        'host': 'localhost',
        'port': 5432
    }

    DEBUG = False
    TESTING = False
    LIVESERVER_PORT = 5000
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_secret_key'
    SECURITY_REGISTERABLE = True
