"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@app.route('/signup', methods=['GET'])
def user_signup():

    response_body = {
        "message": "estos son mis datos"
    }
    return jsonify(response_body), 200

@app.route('/login', methods=['GET'])
def user_signup():
    return 'aqui meto mis datos username y password'

@app.route('/login', methods=['POST'])
def user_signup():
    return 'aqui meto mis datos username y password'