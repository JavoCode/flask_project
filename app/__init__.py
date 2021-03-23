from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = './app/static/uploads'

SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
