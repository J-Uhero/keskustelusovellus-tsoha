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
    if validate(name, password):
        try:
            print("validate")
            sql = "INSERT INTO users (name, password, admin, timestamp, visible) \
                VALUES (:name, :password, FALSE, NOW(), TRUE);"
            db.session.execute(sql, {"name":name, "password":hash_value})
            db.session.commit()
            return login(name, password)
        except Exception:
            print("exception")
            return False
    print("not validate")
    return False

def validate(name, password):
    return len(name) > 1 and len(password) > 4

def count_users_messages(id):
    sql = "SELECT u.timestamp as created_at, \
                  u.id as id, \
                  u.name as name, \
                  u.admin as admin, \
                  count(m.id) as count, \
                  :user_id IN (SELECT user_id \
                               FROM contacts \
                               WHERE user_id=:user_id \
                               AND contact_id=:id) \
                               as contact \
           FROM users u \
           LEFT JOIN messages m \
           ON m.user_id=:id AND m.visible=True \
           WHERE u.id=:id \
           GROUP BY u.id;"
    count = db.session.execute(sql, {"user_id":session["user_id"], "id":id}).fetchone()
    return count

def get_contacts():
    sql = "SELECT c.contact_id as contact_id, u.name as username\
           FROM contacts c, users u \
           WHERE c.user_id=:user_id AND u.id=c.contact_id \
           ORDER BY username;"
    return db.session.execute(sql, {"user_id":session["user_id"]}).fetchall()

def create_contact(id):
    try:
        sql = "INSERT INTO contacts (user_id, contact_id, timestamp) \
               VALUES (:user_id, :contact_id, NOW());"
        db.session.execute(sql, {"user_id":session["user_id"], "contact_id":id})
        db.session.commit()
        return True
    except Exception:
        return False

def remove_contact(id):
    sql = "DELETE FROM contacts WHERE user_id=:user_id AND contact_id=:id;"
    db.session.execute(sql, {"user_id":session["user_id"], "id":id})
    db.session.commit()
    return True