from flask import Flask

from cloudtestenvironment import routes
from cloudtestenvironment import models

models.db.create_all()
app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


