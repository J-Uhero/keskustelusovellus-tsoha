from db import db
from flask import session

def get_contacts():
    sql = "SELECT c.contact_id as contact_id, u.name as username " \
        "FROM contacts c, users u " \
        "WHERE c.user_id=:user_id AND u.id=c.contact_id " \
        "ORDER BY username;"
    return db.session.execute(sql, {"user_id":session["user_id"]}).fetchall()

def create_contact(id):
    try:
        sql = "INSERT INTO contacts (user_id, contact_id, timestamp) " \
            "VALUES (:user_id, :contact_id, NOW());"
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
