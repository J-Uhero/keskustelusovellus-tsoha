from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(name, password):
    sql = "SELECT id, name, password FROM users WHERE name=:name;"
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["username"] = user[1]
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["username"]

def register(name, password):
    hash_value = generate_password_hash(password)
    sql = "SELECT id FROM users WHERE name=:name;"
    user = db.session.execute(sql, {"name":name}).fetchone()
    if not user:
        print("ei käyttäjää")
        sql = "INSERT INTO users (name, password, admin) VALUES \
               (:name, :password, FALSE);"
        db.session.execute(sql, {"name":name, "password":hash_value})
        db.session.commit()
        print("lisätty, kirjaudutaan")
        return login(name, password)
    else:
        return False
