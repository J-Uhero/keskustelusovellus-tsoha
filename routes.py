from app import app
import boards
from flask import redirect, render_template, request, session
import users

@app.route("/")
def index():
    return render_template("index.html")

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
    if request.method == "GET":
        return render_template("forum.html", forums=forums)
    if request.method == "POST":
        main_topic = request.form["main_topic"]
        if boards.create_new_forum(main_topic):
            return redirect("/forum")
        else:
            message = "Aihealue ei kelvannut"
            return render_template("forum.html",
                                    forums=forums,
                                    message=message)

@app.route("/forum/<int:id>", methods=["GET", "POST"])
def topics(id):
    topics = boards.get_topics(id)
    if request.method == "GET":
        return render_template("topics.html", topics=topics, forum_id=id)
    if request.method == "POST":
        sub_topic = request.form["sub_topic"]
        if boards.create_new_topic(sub_topic, id):
            return redirect(f"/forum/{id}")
        else:
            message = "Keskustelu ei kelvannut"
            return render_template("topic.html",
                                    topics=topics,
                                    forum_id=id,
                                    message=message)

@app.route("/forum/<int:id>/<int:id2>", methods=["GET", "POST"])
def thread(id, id2):
    messages = boards.get_thread(id2)
    if request.method == "GET":
        print("viestit",messages)
        print("id:t", id, id2)
        return render_template("thread.html",
                                messages=messages,
                                forum_id=id,
                                topic_id=id2)
    if request.method == "POST":
        content = request.form["message"]
        print("viesti", content)
        tf = boards.create_new_message(content, id2)
        print("onnistuiko viestin lisäys", tf)
        if tf:
            print("onnistui redirect/",id,id2)
            return redirect(f"/forum/{id}/{id2}")
        else:
            print("viestin lisääminen ei onnistunut")


@app.route("/profile", methods=["GET"])
def profile():
    print("haetaan tietokannasta viestit")
    messages = users.count_users_messages()
    print("viestejä:", messages)
    return render_template("profile.html", messages=messages)
