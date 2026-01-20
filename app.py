from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api

from models import db
from models import User

from flask_restful import Resource, reqparse


app = Flask(__name__)

CORS(app)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///note.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)

# Parser for incoming JSON
user_parser = reqparse.RequestParser()
user_parser.add_argument(
    "username", type=str, required=True, help="Username is required"
)
user_parser.add_argument("email", type=str, required=True, help="Email is required")
user_parser.add_argument(
    "password", type=str, required=True, help="Password is required"
)


class RegisterUser(Resource):
    def post(self):
        data = user_parser.parse_args()

        # Check if username or email already exists
        if User.query.filter_by(username=data["username"]).first():
            return {"message": "Username already exists"}, 400
        if User.query.filter_by(email=data["email"]).first():
            return {"message": "Email already exists"}, 400

        # Create new user
        user = User(username=data["username"], email=data["email"])
        user.set_password(data["password"])  # hash password

        db.session.add(user)
        db.session.commit()

        return {"message": f"User {user.username} created successfully"}, 201

# Register the route
api.add_resource(RegisterUser, "/register")
# 
