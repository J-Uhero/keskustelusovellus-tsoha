from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(name, password):
    sql = "SELECT id, name, password, admin FROM users WHERE name=:name;"
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["username"] = user[1]
            session["admin"] = user[3]
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["username"]
    del session["admin"]

def register(name, password):
    hash_value = generate_password_hash(password)
    sql = "SELECT id FROM users WHERE name=:name;"
    #user = db.session.execute(sql, {"name":name}).fetchone()
    if validate(name, password):
        try:
            sql = "INSERT INTO users (name, password, admin, timestamp, visible) VALUES \
                (:name, :password, FALSE, NOW()), TRUE;"
            db.session.execute(sql, {"name":name, "password":hash_value})
            db.session.commit()
            return login(name, password)
        except:
            return False
    return False

def validate(name, password):
    return len(name) > 1 and len(password) > 4

def count_users_messages():
    sql = "SELECT u.timestamp as created_at, \
                  u.admin as admin, \
                  count(m.id) \
           FROM users u LEFT JOIN messages m \
           ON m.user_id=:user_id AND u.id=:user_id \
           GROUP BY u.id;"
    count = db.session.execute(sql, {"user_id":session["user_id"]}).fetchone()
    return count
