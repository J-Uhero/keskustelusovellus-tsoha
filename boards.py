from db import db
from flask import session

def get_forums():
    sql = "SELECT id, topic FROM forums ORDER BY topic;"
    result = db.session.execute(sql).fetchall()
    return result

def get_topics(id):
    sql = "SELECT id, topic FROM topics WHERE forum_id=:id;"
    return db.session.execute(sql, {"id":id}).fetchall()

def create_new_forum(topic):
    sql = "INSERT INTO forums (topic) VALUES (:topic);"
    try:
        db.session.execute(sql, {"topic":topic})
        db.session.commit()
    except:
        return False
    return True

def create_new_topic(topic, forum_id):
    sql = "INSERT INTO topics (topic, forum_id, timestamp) VALUES (:topic, :forum_id, NOW());"
    try:
        db.session.execute(sql, {"topic":topic, "forum_id":forum_id})
        db.session.commit()
    except:
        return False
    return True

def get_thread(topic_id):
    sql = "SELECT u.name, m.content, m.timestamp " \
          "FROM messages m, users u " \
          "WHERE m.topic_id=:topic_id AND u.id=m.user_id " \
          "ORDER BY m.timestamp;"
    return db.session.execute(sql, {"topic_id":topic_id}).fetchall()

def create_new_message(content, topic_id):
    sql = "INSERT INTO messages (content, user_id, topic_id, timestamp) " \
          "VALUES (:content, :user_id, :topic_id, NOW());"
    try:
        db.session.execute(sql, {"content":content,
                                 "user_id":session["user_id"],
                                 "topic_id":topic_id})
        db.session.commit()
    except:
        return False
    return True
