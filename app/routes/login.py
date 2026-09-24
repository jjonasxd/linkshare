from flask import Blueprint, request, jsonify, make_response
from werkzeug.wrappers import response
from config import Config
from flask_jwt_extended import create_access_token, jwt_required, set_access_cookies, create_refresh_token, set_refresh_cookies, get_jwt_identity

auth_bp = Blueprint("BP_login", __name__)

@auth_bp.route("/api/login", methods=["POST"])
def login():
    dados = request.json
    username = dados.get("username")
    password = dados.get("password")
    
    if not username or not password:
        return jsonify({"status": "Dados incompletos"}), 400

    if username != Config.username or password != Config.password:
        return jsonify({"status": "Credenciais invalidas"}), 401

    access_token = create_access_token(identity=username)
    refresh_roken = create_refresh_token(identity=username)

    response = make_response(jsonify({"login": True}))
    
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_roken)
    
    return response, 201

@auth_bp.route("/api/refresh", methods=["GET"])
@jwt_required()
def refresh_AccessToken():
    username = get_jwt_identity()

    if not username:
        return jsonify({"status": "Impossivel criar outro access token", "access": False})

    response = make_response(jsonify({"access": True}))
    access_token = create_access_token(identity=username)

    set_access_cookies(response, access_token)

    return response, 201


