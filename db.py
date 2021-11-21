from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import re

uri = getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

#tehty muutos pohjautuen tähän ohjeeseen:
#https://help.heroku.com/ZKNTJQSK/why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres

app.config["SQLALCHEMY_DATABASE_URI"] = uri
db = SQLAlchemy(app)
