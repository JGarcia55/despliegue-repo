from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
from controllers import *
from db import db
import os

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOST_DB")}/{os.getenv("SCHEMA_DB")}'
db = db.init_app(app)
api = Api(app)
app.secret_key = os.urandom(24)
print(app.secret_key.hex())
login_manager = LoginManager(app)

api.add_resource(guarderia_controller.GuarderiasController, '/guarderia')

from flask_login import UserMixin

@app.route("/test")
def testeer():
    return "Hello"

# User class
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Load user callback
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Ruta de inicio

@app.route('/')
def index():
    return "Hello world"

@app.route('/home')
@login_required
def home():
    return f'Hello, {current_user.id}!'

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = User(user_id)
        login_user(user)
        return redirect(url_for('testeer'))
    return render_template('login.html')

# Ruta de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
