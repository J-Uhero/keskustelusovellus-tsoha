from db import db
from flask import session
import secrets
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
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["username"]
    del session["admin"]
    del session["csrf_token"]

def register(name, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (name, password, admin, timestamp, active) " \
            "VALUES (:name, :password, FALSE, NOW(), True);"
        db.session.execute(sql, {"name":name, "password":hash_value})
        db.session.commit()
        return login(name, password)
    except Exception:
        return False

def validate(name, password):
    return 20 >= len(name) > 1 and len(password) > 6

def count_users_messages(id):
    sql = "SELECT u.timestamp as created_at, u.id as id, u.active as active, " \
        "u.name as name, u.admin as admin, count(m.id) as count," \
        ":user_id IN (SELECT user_id FROM contacts " \
        "WHERE user_id=:user_id AND contact_id=:id) as contact "\
        "FROM users u " \
        "LEFT JOIN messages m " \
        "ON m.user_id=:id AND m.visible=True " \
        "WHERE u.id=:id " \
        "GROUP BY u.id;"
    count = db.session.execute(sql, {"user_id":session["user_id"],
                                     "id":id}).fetchone()
    return count

def search_user_by_name(name):
    sql = "SELECT id, name FROM users WHERE name LIKE :name ORDER BY name LIMIT 30;"
    return db.session.execute(sql, {"name":name}).fetchall()

def freeze_user(id):
    sql = "UPDATE users SET active=False WHERE id=:id;"
    db.session.execute(sql, {"id":id})
    db.session.commit()

def activate_user(id):
    sql = "UPDATE users SET active=True WHERE id=:id;"
    db.session.execute(sql, {"id":id})
    db.session.commit()

def get_username(id):
    sql = "SELECT id as id, name as username FROM users WHERE id=:id;"
    return db.session.execute(sql, {"id":id}).fetchall()

def give_admin_rights(id):
    sql = "UPDATE users SET admin=True WHERE id=:id;"
    db.session.execute(sql, {"id":id})
    db.session.commit()
