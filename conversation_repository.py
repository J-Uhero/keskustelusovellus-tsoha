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
    sql = "INSERT INTO private_messages (user1_id, user2_id, content, timestamp, visible, seen) " \
        "VALUES (:user_id, :id, :content, NOW(), True, False);"
    db.session.execute(sql, {"user_id":session["user_id"], "id":id, "content":content})
    db.session.commit()

def update_messages_as_seen(sender_id):
    try:
        sql = "UPDATE private_messages SET seen=True " \
            "WHERE user1_id=:sender_id AND user2_id=:user_id;"
        db.session.execute(sql, {"sender_id":sender_id, "user_id":session["user_id"]})
        db.session.commit()
        return True
    except:
        return False

def get_private_messages_info():
    sql = "SELECT p.user1_id as contact_id, MAX(p.timestamp) as viimeisin, COUNT(*) as count, " \
        "(SELECT u.name FROM users u WHERE p.user1_id=u.id) as name, " \
        "(SELECT COUNT(*) FROM private_messages p2 " \
        "WHERE p2.user1_id=p.user1_id AND p2.user2_id=:user_id AND p2.seen=False) as not_seen " \
        "FROM private_messages p " \
        "WHERE p.user2_id=:user_id AND p.visible=True " \
        "GROUP BY p.user1_id " \
        "ORDER BY viimeisin DESC;"

    return db.session.execute(sql, {"user_id":session["user_id"]}).fetchall()

def count_all_not_seen_messages():
    sql = "SELECT COUNT(*) FROM private_messages " \
        "WHERE user2_id=:user_id AND seen=False AND visible=True;"
    return db.session.execute(sql, {"user_id":session["user_id"]}).fetchone()[0]

def count_messages(id):
    sql3 = "SELECT p.user1_id as contact_id, COUNT(p.user1_id), MAX(p.timestamp) as count " \
        "FROM private_messages p " \
        "WHERE p.user2_id=:user_id AND visible=True GROUP BY p.user1_id"

def search_private_messages(query):
    sql = "SELECT p.id as message_id, p.content as content, p.user1_id as sender_id, " \
        "u.name as username, p.timestamp as timestamp " \
        "FROM private_messages p " \
        "LEFT JOIN users u ON u.id=p.user1_id " \
        "WHERE p.content LIKE :query AND p.user2_id=:user_id AND p.visible=True " \
        "ORDER BY timestamp DESC;"
    return db.session.execute(sql, {"query":query, "user_id":session["user_id"]}).fetchall()  
