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
    sql = "SELECT day_minus_two, day_minus_one, day_zero, day_ten, day_eleven FROM courses WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    course = result.fetchone()
    return render_template("course.html", id=id, course=course)

@app.route("/signup/", methods=["POST"])
def signup():
    course_id = request.form["id"]
    username = session["username"]
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user_id = result.fetchone()[0]
    #tässä vertaile päivämääriä, ja laita saapumispvm ja lähtöpvm tietokantaan
    if "participation" in request.form:

        participation_days = request.form.getlist("participation")
        arrival_day = participation_days[0]
        departure_day = participation_days[-1]

        sql = "INSERT INTO participations (course_id, user_id, arrival_day, departure_day) VALUES (:course_id, :user_id, :arrival_day, :departure_day)"
        db.session.execute(sql, {"course_id":course_id, "user_id":user_id, "arrival_day":arrival_day, "departure_day": departure_day })
        db.session.commit()
    return redirect("/participation/" + str(user_id))

@app.route("/participation/<int:user_id>")
def participation(user_id):
    sql = "SELECT id, course_id, arrival_day, departure_day FROM participations WHERE user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    participation_data = result.fetchall()
    #tässä kohtaa hae kurssien pvm:t, jotta ne voisi näyttää participation.html:ssä
    # for data in participation data:
    # data[0] = participation_id
    # data[1] = course_id
    return render_template("participation.html", participation_data=participation_data)





@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
