
from flask import Blueprint, request, jsonify
from .db import *

api = Blueprint("_api", __package__, url_prefix="/_api")

@api.route("/calls/<call_id>", methods=["GET"])
def find_call(call_id = None):
    res = Call.query.filter(Call.id == call_id)
    return jsonify(res)
