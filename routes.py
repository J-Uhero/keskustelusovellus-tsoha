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
    return render_template("forum.html", forums=forums)

@app.route("/forum/<int:id>", methods=["GET", "POST"])
def topics(id):
    print("printataan id:", id)
    topic = boards.get_topics(id)
    #name =request.form["forum.topic"]
    return render_template("topics.html", topic=topic, forum_id=id)

@app.route("/profile", methods=["GET"])
def profile():
    print("haetaan tietokannasta viestit")
    messages = users.count_users_messages()
    print("viestejä:", messages)
    return render_template("profile.html", messages=messages)
