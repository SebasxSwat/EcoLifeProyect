from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)

    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    from app.routes import login_routes, challenges_routes, badge_routes

    app.register_blueprint(login_routes.bp)
    app.register_blueprint(challenges_routes.bp)
    app.register_blueprint(badge_routes.bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)
