
from app import app
from db import db
from flask import redirect, render_template, request, session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
import course_management
import participation_management
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
    user_id = user_management.get_user_id(username)
    if "participation" in request.form:
        participation_days = request.form.getlist("participation")
        arrival_day = participation_days[0]
        departure_day = participation_days[-1]
        participation_management.add_participation(course_id, user_id, arrival_day, departure_day)
    return redirect("/participation/" + str(user_id))

@app.route("/participation/<int:user_id>")
def participation(user_id):
    participation_data = participation_management.get_participations(user_id)
    participations = []
    for data in participation_data:
        course_id = data[0]
        arrival = data[2]
        departure = data[3]
        start_and_end = course_management.get_course_dates(course_id)
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
            user_management.create_user(username, hash_value_pwd)
        except Exception as e:
            return render_template("invalid.html", message="Something went wrong: "+ str(e) )
        session["username"] = username
        user_id = user_management.get_user_id(username)
        session["user_id"] = user_id
        return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")