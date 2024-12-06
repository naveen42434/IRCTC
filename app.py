from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)

    from Routes.auth import auth_bp
    from Routes.train import train_bp
    from Routes.booking import booking_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(train_bp, url_prefix='/train')
    app.register_blueprint(booking_bp, url_prefix='/booking')

    return app