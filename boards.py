from db import db
from flask import session

def get_forums():
    sql = "SELECT id, topic FROM forums ORDER BY topic;"
    result = db.session.execute(sql).fetchall()
    return result

def get_topics(id):
    sql = "SELECT id, topic FROM topics WHERE forum_id=:id;"
    return db.session.execute(sql, {"id":id}).fetchall()

