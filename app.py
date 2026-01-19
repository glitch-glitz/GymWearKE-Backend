from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# setup cors
CORS(app)

# setup flask-restful
api = Api(app)

# configure database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///note.db"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize db
db = SQLAlchemy(app)

# initialize migrate
migrate = Migrate(app, db)
