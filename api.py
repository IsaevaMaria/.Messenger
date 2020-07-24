from flask import Blueprint, jsonify


api = Blueprint("api", __name__, template_folder="templates")


@api.route("/api/test", methods=["GET"])
def test():
    return jsonify({"test": 1})


@api.route("/api", methods=["GET"])
def index():
    return jsonify(["Welcome to the API"])

