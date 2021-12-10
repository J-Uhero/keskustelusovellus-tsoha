from db import db
from flask import session

def get_forums():
    sql = "SELECT id, topic FROM forums WHERE visible=TRUE ORDER BY topic;"
    result = db.session.execute(sql).fetchall()
    return result

def get_forum(id):
    sql = "SELECT id, topic FROM forums WHERE visible=TRUE AND id=:id;"
    result = db.session.execute(sql, {"id":id}).fetchone()
    print(result)
    return result

def get_topics(id):
    sql = "SELECT id, topic FROM topics WHERE forum_id=:id AND visible=TRUE;"
    return db.session.execute(sql, {"id":id}).fetchall()

def get_forum_and_topic(forum_id, topic_id):
    sql = "SELECT f.id, f.topic, t.id, t.topic FROM forums f LEFT JOIN topic t WHERE " 

def create_new_forum(topic):
    sql = "INSERT INTO forums (topic, visible) VALUES (:topic, TRUE);"
    try:
        db.session.execute(sql, {"topic":topic})
        db.session.commit()
    except:
        return False
    return True

def create_new_topic(topic, forum_id):
    sql = "INSERT INTO topics (topic, forum_id, timestamp, visible) \
           VALUES (:topic, :forum_id, NOW(), TRUE);"
    try:
        db.session.execute(sql, {"topic":topic, "forum_id":forum_id})
        db.session.commit()
    except:
        return False
    return True

def get_thread(topic_id):
    sql = "SELECT m.id as message_id, u.id as user_id, u.name, m.content, m.timestamp " \
          "FROM messages m, users u " \
          "WHERE m.topic_id=:topic_id AND u.id=m.user_id AND m.visible=TRUE " \
          "ORDER BY m.timestamp;"
    return db.session.execute(sql, {"topic_id":topic_id}).fetchall()

def create_new_message(content, topic_id):
    sql = "INSERT INTO messages (content, user_id, topic_id, timestamp, visible) " \
          "VALUES (:content, :user_id, :topic_id, NOW(), TRUE);"
    try:
        db.session.execute(sql, {"content":content,
                                 "user_id":session["user_id"],
                                 "topic_id":topic_id})
        db.session.commit()
    except Exception:
        return False
    return True

def remove_message(id):
    print(id)
    sql = "UPDATE messages SET visible=FALSE WHERE id=:id;"
    try:
        db.session.execute(sql, {"id":id})
        db.session.commit()
    except Exception:
        print("viestin poisto ei onnistunut")
        return False
    return True

def validate_message(content):
    return len(content) < 5000

def validate_topic(name):
    return len(name) < 50
