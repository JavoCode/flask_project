import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = './app/static/uploads'

SECRET_KEY = 'Sup3r$3cretkey'

SQLALCHEMY_DATABASE_URI = 'postgresql://mwkqpabdspddvf:c444054ca1e8972fd483f0066c2ebf63b609f9a336c95991cc0123d225fbc3f6@ec2-23-21-229-200.compute-1.amazonaws.com/dcgj5er7alr0pn'
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
