from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.CHAR(80))
    password = db.Column(db.CHAR(80))

    def __str__(self):
        return 'login: %s, password: %s' % (self.login, self.password)

    def __repr__(self):
        return 'User (%s, %s)' % (self.login, self.password)