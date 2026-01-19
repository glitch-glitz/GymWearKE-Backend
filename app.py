from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from models import db

app = Flask(__name__)

CORS(app)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///note.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)
