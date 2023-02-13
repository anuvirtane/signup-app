from db import db
from sqlalchemy.sql import text

def add_participation(course_id: int, user_id: int, arrival_day: any, departure_day: any):
    sql = text("INSERT INTO participations (course_id, user_id, arrival_day, departure_day) VALUES (:course_id, :user_id, :arrival_day, :departure_day)")
    db.session.execute(sql, {"course_id":course_id, "user_id":user_id, "arrival_day":arrival_day, "departure_day": departure_day })
    db.session.commit()
    return True

def get_participation(id: int):
    sql = text("SELECT course_id, user_id, arrival_day, departure_day FROM participations WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    participation = result.fetchone()
    return participation

def get_participations(user_id: int):
    sql = text("SELECT id, course_id, arrival_day, departure_day FROM participations WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    participation_data = result.fetchall()
    return participation_data

def participation_exists(user_id, course_id):
    sql = text("SELECT id, arrival_day, departure_day FROM participations WHERE user_id=:user_id AND course_id=:course_id")
    result = db.session.execute(sql, {"user_id":user_id, "course_id":course_id})
    participation_data = result.fetchone()
    return participation_data