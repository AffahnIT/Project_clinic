from flask import Blueprint

bp = Blueprint("doctor", __name__, url_prefix="/doctor")

@bp.route("/dashboard")
def dashboard():
    return "Doctor Dashboard"
