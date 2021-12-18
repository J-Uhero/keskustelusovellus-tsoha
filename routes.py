from app import app
import boards
import contact_repository
import conversation_repository
from flask import redirect, render_template, request, session
import users

@app.route("/")
def index():
    message = None
    if session.get("user_id") is not None:
        message = conversation_repository.count_all_not_seen_messages()
    return render_template("index.html", message=message)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        if users.login(name, password):
            return redirect("/")
        else:
            message="väärä käyttäjänimi tai salasana"
            return render_template("login.html", message=message)

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username, password):
            return redirect("/")
        else:
            return render_template("register.html",
                                    message="käyttäjänimi ei kelpaa")

@app.route("/logout")
def logout():
    users.logout()
    return render_template("logout.html")

@app.route("/forum", methods=["GET", "POST"])
def forum():
    forums = boards.get_forums()
    #print(forums)
    if request.method == "GET":
        return render_template("forum.html", forums=forums)
    if request.method == "POST":
        if "new" in request.form:
            main_topic = request.form["main_topic"]
            if boards.validate_topic_name(main_topic):
                boards.create_new_forum(main_topic)
        if "remove" in request.form:
            choice_id = request.form["remove_id"]
            boards.remove_forum(choice_id)
        return redirect("/forum")

@app.route("/forum/<int:id>", methods=["GET", "POST"])
def topics(id):
    topics = boards.get_topics(id)
    print(topics)
    if request.method == "GET":
        return render_template("topics.html", topics=topics, forum_id=id)
    if request.method == "POST":
        if "add" in request.form:
            sub_topic = request.form["sub_topic"]
            if boards.validate_topic_name:
                boards.create_new_topic(sub_topic, id)
        if "remove" in request.form:
            choice_id = request.form["remove_id"]
            boards.remove_topic(choice_id)
        return redirect(f"/forum/{id}")

@app.route("/forum/<int:id>/<int:id2>", methods=["GET", "POST"])
def thread(id, id2):
    messages = boards.get_thread(id2)
    info = boards.get_forum_and_topic_info(id2)
    if request.method == "GET":
        return render_template("thread.html",
                                messages=messages,
                                info=info)
    if request.method == "POST":
        if "send" in request.form:
            content = request.form["message"]
            boards.create_new_message(content, id2)
            return redirect(f"/forum/{id}/{id2}")
        #if "" == ""

@app.route("/forum/<int:id>/<int:id2>/<int:message_id>", methods=["POST"])
def remove_message(id, id2, message_id):
    boards.remove_message(message_id)
    return redirect(f"/forum/{id}/{id2}")

@app.route("/profile/<int:id>", methods=["GET", "POST"])
def profile(id):
    if request.method == "GET":
        profile = users.count_users_messages(id)
        return render_template("profile.html", profile=profile)
    if request.method == "POST":
        if "add_contact" in request.form:
            contact_repository.create_contact(id)
        if "remove_contact" in request.form:
            contact_repository.remove_contact(id)
        return redirect(f"/profile/{id}")

@app.route("/contacts")
def contacts():
    contacts = contact_repository.get_contacts()
    return render_template("contacts.html", contacts=contacts)

@app.route("/conversation/<int:id>", methods=["GET", "POST"])
def conversation(id):
    if request.method == "GET":
        messages = conversation_repository.get_conversation(id)
        conversation_repository.update_messages_as_seen(id)
        return render_template("conversation.html",
                               messages=messages,
                               contact_id=id)
    if request.method == "POST":
        message = request.form["message"]
        conversation_repository.add_private_message(id, message)
        return redirect(f"/conversation/{id}")

@app.route("/messages", methods=["GET"])
def messages():
    messages = conversation_repository.get_private_messages_info()
    return render_template("messages.html", messages=messages)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    results = None
    searched = False
    found = False
    search_type = {  
        "username": False,
        "forum_message": False,
        "private_message": False,  
    }
    if query is not None and len(query) > 0:
        query = "%" + query + "%"
        searched = True
        search_type[request.args.get("type")] = True
        if search_type["username"]:
            results = users.search_user_by_name(query)
        if search_type["forum_message"]:
            results = boards.search_messages_from_forums(query)
        if search_type["private_message"]:
            results = conversation_repository.search_private_messages(query)
        if results is not None and len(results) > 0:
            found = True
    return render_template("search.html",
                           results=results,
                           search_type=search_type,
                           searched=searched,
                           found=found)

