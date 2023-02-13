from db import db
from sqlalchemy.sql import text

def create_lift(course_id: int, driver_id: int, to_course: any, from_where: str, from_course: any, to_where: str):
    sql = text("INSERT INTO lift_offers (course_id, driver_id, to_course, from_where, from_course, to_where) VALUES (:course_id, :driver_id, :to_course, :from_where, :from_course, :to_where)")
    db.session.execute(sql, {"course_id":course_id, "driver_id":driver_id, "to_course":to_course, "from_where":from_where, "from_course":from_course, "to_where":to_where})
    db.session.commit()
    return True

