from flask import Flask
from database.database import db
from flask import jsonify, request, render_template
from database.models import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
import requests as http_request

# Restante do código foi suprimido para facilitar a localização nos códigos
app = Flask(__name__, template_folder="templates")
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

@app.route("/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # Query your database for username and password
    user = User.query.filter_by(email=username, password=password).first()
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401
    
    # create a new token with the user id inside
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id })

# Código anterior suprimido para facilitar a localização nos códigos

@app.route("/user-login", methods=["GET"])
def user_login():
    return render_template("login.html")

# Código superior suprimido para facilitar a localização nos códigos
@app.route("/user-register", methods=["GET"])
def user_register():
    return render_template("register.html")

# Código anterior suprimido
@app.route("/content", methods=["GET"])
def content():
    return render_template("content.html")

@app.route("/error", methods=["GET"])
def error():
    return render_template("error.html")

# Código anterior suprimido para facilitar a localização nos códigos

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    # Verifica os dados enviados não estão nulos
    if username is None or password is None:
        # the user was not found on the database
        return render_template("error.html", message="Bad username or password")
    # faz uma chamada para a criação do token
    token_data = http_request.post("http://localhost:5000/token", json={"username": username, "password": password})
    if token_data.status_code != 200:
        return render_template("error.html", message="Bad username or password")
    # recupera o token
    response = make_response(render_template("content.html"))
    set_access_cookies(response, token_data.json()['token'])
    return response

# Restante do código foi suprimido para facilitar a localização nos códigos