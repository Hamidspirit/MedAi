from flask import Blueprint, request, jsonify, render_template
from ..utils.errors import ConflictError, UnauthorizedError

default_bp = Blueprint("default", __name__, url_prefix="/")


@default_bp.get("")
def return_home():
    return render_template("index.html")
