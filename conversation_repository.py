from db import db
from flask import session

def get_conversation(id):
    sql = "SELECT u.id, u.name, p.content, p.timestamp " \
        "FROM private_messages p, users u " \
        "WHERE (p.user1_id=:id1 AND p.user2_id=:id2 AND p.user1_id=u.id) " \
        "OR (user1_id=:id2 AND user2_id=:id1 AND p.user1_id=u.id) " \
        "AND p.visible=True ORDER BY p.timestamp;"
    return db.session.execute(sql, {"id1":session["user_id"], "id2":id}).fetchall()

def add_private_message(id, content):
    sql = "INSERT INTO private_messages (user1_id, user2_id, content, timestamp, visible) " \
        "VALUES (:user_id, :id, :content, NOW(), True);"
    db.session.execute(sql, {"user_id":session["user_id"], "id":id, "content":content})
    db.session.commit()
