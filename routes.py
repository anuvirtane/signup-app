
from app import app
from db import db
from flask import redirect, render_template, request, session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
import course_management
import user_management


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = user_management.get_user(username)
    if not user:
        return render_template("invalid.html", message="Invalid user name")
    else:    
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = username
            session["user_id"] = user.id
            return redirect("/")
        else:
            return render_template("invalid.html", message="Invalid password")

@app.route("/courses",methods=["GET"])
def courses():
    courses = course_management.get_courses()
    return render_template("courses.html", courses=courses)

@app.route("/course/<int:id>")
def course(id):
    course = course_management.get_course_by_id(id)
    return render_template("course.html", id=id, course=course)

@app.route("/signup/", methods=["POST"])
def signup():
    """If user chooses dates, put them in participations table"""
    course_id = request.form["id"]
    username = session["username"]
    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user_id = result.fetchone()[0]
    if "participation" in request.form:
        participation_days = request.form.getlist("participation")
        arrival_day = participation_days[0]
        departure_day = participation_days[-1]
        sql = text("INSERT INTO participations (course_id, user_id, arrival_day, departure_day) VALUES (:course_id, :user_id, :arrival_day, :departure_day)")
        db.session.execute(sql, {"course_id":course_id, "user_id":user_id, "arrival_day":arrival_day, "departure_day": departure_day })
        db.session.commit()
    return redirect("/participation/" + str(user_id))

@app.route("/participation/<int:user_id>")
def participation(user_id):
    sql = text("SELECT id, course_id, arrival_day, departure_day FROM participations WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    participation_data = result.fetchall()
    participations = []
    for data in participation_data:
        course_id = data[0]
        arrival = data[2]
        departure = data[3]
        sql = text("SELECT day_zero, day_eleven FROM courses WHERE id=:course_id")
        result = db.session.execute(sql, {"course_id":course_id})
        start_and_end = result.fetchone()
        course_start = start_and_end[0]
        course_end = start_and_end[1]
        participation = (course_start, course_end, arrival, departure)
        participations.append(participation)
    return render_template("participation.html", participations=participations)

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 3 or len(username) > 20:
            return render_template("invalid.html", message="Username should contain 3-20 characters")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("invalid.html", message="Two different passwords were typed")
        if len(password1) < 5:
            return render_template("invalid.html", message="Password should contain 5 or more characters")
        hash_value_pwd = generate_password_hash(password1)
        try:
            sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
            db.session.execute(sql, {"username":username, "password":hash_value_pwd})
            db.session.commit()
        except Exception as e:
            return render_template("invalid.html", message="Something went wrong: "+ str(e) )
        session["username"] = username
        return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")