from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    jwt.init_app(app)

    from app.routes import auth, patient, doctor, admin
    app.register_blueprint(auth.bp)
    app.register_blueprint(patient.bp)
    app.register_blueprint(doctor.bp)
    app.register_blueprint(admin.bp)

    return app
