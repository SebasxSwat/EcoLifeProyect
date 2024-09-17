from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')

    db.init_app(app)

    
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    from app.routes import authRoute, userRoutes

    app.register_blueprint(authRoute.bp)
    app.register_blueprint(userRoutes.bp)

    with app.app_context():
        db.create_all()

    return app
