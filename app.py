from flask import Flask
from flask import redirect, render_template
from flask.globals import request
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import routes
