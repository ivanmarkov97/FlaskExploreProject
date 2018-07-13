from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)
db.init_app(app)
from models import *


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/add-user', methods=['GET'])
def add_default_user():
    user = User(login='userEmail@yandex.ru', password='userPassword')
    db.session.add(user)
    db.session.commit()
    return str(user)


@app.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append(user)
    return str(user_list)


@app.route('/<name>', methods=['GET'])
def hello_name(name):
    context = {
        "name": name,
        "description": "kek"
    }
    return render_template('profile.html', context=context)


if __name__ == '__main__':
    app.run()
