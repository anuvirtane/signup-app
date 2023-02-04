from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from os import getenv



app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()    
    if not user:
        return render_template("invalid.html")
    else:
        #return render_template("valid.html")
        # hash_value = user.password
        # if check_password_hash(hash_value, password):
        session["username"] = username
        return redirect("/")
        # else:
        #     return render_template("invalid.html")

@app.route("/courses",methods=["GET"])
def courses():
    sql = "SELECT id, day_minus_two, day_minus_one, day_zero, day_ten, day_eleven FROM courses ORDER BY id DESC"
    result = db.session.execute(sql)
    courses = result.fetchall()
    return render_template("courses.html", courses=courses)

@app.route("/course/<int:id>")
def course(id):
    sql = "SELECT id FROM courses WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    choices = result.fetchone()[0]
    return render_template("course.html", id=id)



@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
