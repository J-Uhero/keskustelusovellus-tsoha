from app import app
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
