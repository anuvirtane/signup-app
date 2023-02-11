from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv, urandom

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SECRET KEY"] = getenv("SECRET_KEY")
app.config.update(SECRET_KEY = urandom(24))
app.config['SESSION_TYPE'] = 'filesystem'
db = SQLAlchemy(app)