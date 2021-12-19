from db import db
from flask import session

def get_forums():
    sql = "SELECT f.id, f.topic, COUNT(t.id) as count " \
        "FROM forums f " \
        "LEFT JOIN topics t ON f.id=t.forum_id AND t.visible=True " \
        "WHERE f.visible=TRUE " \
        "GROUP BY f.id " \
        "ORDER BY f.topic;"

    return db.session.execute(sql).fetchall()

def get_forum_info(id):
    sql = "SELECT id, topic FROM forums WHERE visible=TRUE AND id=:id;"
    return db.session.execute(sql, {"id":id}).fetchone()

def get_topics(id):
    sql = "SELECT t.id as id , t.topic as topic, COUNT(m.id) as count " \
        "FROM topics t " \
        "LEFT JOIN messages m ON m.topic_id=t.id AND m.visible=True " \
        "WHERE t.forum_id=:id AND t.visible=True " \
        "GROUP BY t.id ORDER BY topic;"
    return db.session.execute(sql, {"id":id}).fetchall()

def get_forum_and_topic_info(topic_id):
    sql = "SELECT f.id as forum_id, f.topic as forum, t.id as topic_id, " \
        "t.topic as topic, u.visible as active " \
        "FROM forums f, topics t, users u " \
        "WHERE f.id=t.forum_id AND t.id=:topic_id AND u.id=:user_id;"
    return db.session.execute(sql, {"topic_id":topic_id,
                                    "user_id":session["user_id"]}).fetchone()

def create_new_forum(topic):
    try:
        sql = "INSERT INTO forums (topic, visible) VALUES (:topic, TRUE);"
        db.session.execute(sql, {"topic":topic})
        db.session.commit()
    except Exception:  
        db.session.execute("ROLLBACK")
        update_forum_to_visible(topic)
    
def update_forum_to_visible(topic):
    sql = "SELECT id FROM forums WHERE topic=:topic;"
    result = db.session.execute(sql, {"topic":topic}).fetchone()
    try:
        sql = "UPDATE forums SET visible=True WHERE topic=:topic;"
        db.session.execute(sql, {"topic":topic})
        db.session.commit()
        return True
    except Exception:
        return False

def create_new_topic(topic, forum_id):

    sql = "INSERT INTO topics (topic, forum_id, timestamp, visible) " \
        "VALUES (:topic, :forum_id, NOW(), TRUE);"
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

def remove_forum(forum_id):
    sql = "UPDATE forums SET visible=False WHERE id=:forum_id;"
    db.session.execute(sql, {"forum_id":forum_id})
    db.session.commit()

    sql = "SELECT id FROM topics WHERE forum_id=:forum_id;"
    results = db.session.execute(sql, {"forum_id":forum_id}).fetchall()
    for result in results:
        remove_topic(result[0])

def remove_topic(topic_id):
    sql = "UPDATE topics SET visible=False WHERE id=:topic_id;"
    db.session.execute(sql, {"topic_id":topic_id})
    db.session.commit()

    sql = "SELECT id FROM messages WHERE topic_id=:topic_id;"
    results = db.session.execute(sql, {"topic_id":topic_id}).fetchall()
    for result in results:
        remove_message(result[0])

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
    sql = "UPDATE messages SET visible=False WHERE id=:id;"
    try:
        db.session.execute(sql, {"id":id})
        db.session.commit()
    except Exception:
        db.session.execute("ROLLBACK")
        return False
    return True

def validate_message(content):
    return 0 < len(content) < 5000

def validate_topic_name(name):
    return 0 < len(name) < 50

def search_messages_from_forums(entry):
    sql = "SELECT m.id as message_id, m.content as content, m.user_id as user_id, "\
        "u.name as username, t.id as topic_id, t.topic as topic, f.id as forum_id, " \
        "f.topic as forum, m.timestamp as timestamp " \
        "FROM messages m " \
        "LEFT JOIN users u ON u.id=m.user_id " \
        "LEFT JOIN topics t ON t.id=m.topic_id AND t.visible=True " \
        "LEFT JOIN forums f ON f.id=t.forum_id AND f.visible=True " \
        "WHERE m.content LIKE :entry AND m.visible=True " \
        "ORDER BY timestamp DESC;"
    return db.session.execute(sql, {"entry":entry}).fetchall()
