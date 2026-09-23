from flask import Blueprint, request, jsonify
from config import Config

BP_login = Blueprint("BP_login", __name__)

@BP_login.route("/api/login", methods=["POST"])
def login():
    dados = request.json
    print(dados, flush=True)
    if not dados:
        return jsonify({"status": "Nenhum dado enviado"}), 400

    try:
        if dados.get("password") == Config.password and dados.get("username") == Config.username:
            return jsonify({"status": "Parabens"})
        else:
            return jsonify({"status": "Dados incorretos"})
    except KeyError:
        return jsonify({"status": "Requisição incompleta"})
