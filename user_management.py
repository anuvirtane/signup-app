from db import db
from sqlalchemy.sql import text

def create_user(username: str, hash_value_pwd: str):
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":hash_value_pwd})
    db.session.commit()
    return True

def get_user(username: str):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    return user

def get_user_id(username: str):
    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user_id = result.fetchone()[0]
    return user_id



