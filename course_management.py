from db import db
from sqlalchemy.sql import text

def get_courses():
    sql = text("SELECT id, day_minus_two, day_minus_one, day_zero, day_ten, day_eleven FROM courses ORDER BY id DESC")
    result = db.session.execute(sql)
    courses = result.fetchall()
    return courses

def get_course_by_id(id: int):
    sql = text("SELECT day_minus_two, day_minus_one, day_zero, day_ten, day_eleven FROM courses WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    course = result.fetchone()
    return course

def get_course_dates(course_id):
    sql = text("SELECT day_zero, day_eleven FROM courses WHERE id=:course_id")
    result = db.session.execute(sql, {"course_id":course_id})
    start_and_end = result.fetchone()
    return start_and_end