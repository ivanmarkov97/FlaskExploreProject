from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, LoginManager, login_user, logout_user
from config import Config
from posts.views import posts
from models import *

app = Flask(__name__)
app.config.from_object(Config())
app.register_blueprint(posts)
db = SQLAlchemy(app)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    print(user.login)
    print(user.is_active)
    print(user)
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(login=username, password=password).first()
        if user is not None:
            login_user(user)
            return redirect('/')
    return render_template('auth_form.html')


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route('/', methods=['GET'])
@login_required
def hello_world():
    return render_template('index.html')


@app.route('/add-user', methods=['GET'])
def add_default_user():
    role = Role.query.filter_by(name='Common').first()
    print(str(role))
    user = User(login='userEmail@yandex.ru',
                password='userPassword',
                role=role)
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
