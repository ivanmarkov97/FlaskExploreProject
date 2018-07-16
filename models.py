from app import db
from flask_login import UserMixin


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(80))

    def __str__(self):
        return self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80))
    password = db.Column(db.String(80))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.id, self.login, self.password, self.role, self.get_id())

    def __repr__(self):
        return 'User (%s, %s, %s, %s, %s)' % (self.id, self.login, self.password, self.role, self.get_id())
