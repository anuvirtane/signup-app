from db import db
from sqlalchemy.sql import text

def create_lift(course_id: int, driver_id: int, to_course: str, from_where: str, from_course: str, to_where: str):
    sql = text("INSERT INTO lift_offers (course_id, driver_id, to_course, from_where, from_course, to_where) VALUES (:course_id, :driver_id, :to_course, :from_where, :from_course, :to_where)")
    db.session.execute(sql, {"course_id":course_id, "driver_id":driver_id, "to_course":str(to_course), "from_where":str(from_where), "from_course":str(from_course), "to_where":str(to_where)})
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        return False
    return True

