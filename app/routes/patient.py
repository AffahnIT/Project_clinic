from flask import Blueprint

bp = Blueprint("patient", __name__, url_prefix="/patient")

@bp.route("/dashboard")
def dashboard():
    return "Patient Dashboard"
