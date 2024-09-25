from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail


db = SQLAlchemy()
mail = Mail()


def create_app():
    app = Flask(__name__)
    
    
    app.config.from_object('config.Config')

    db.init_app(app)
    mail.init_app(app)
    
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    app.config['JWT_SECRET_KEY'] = 'ecolifepassword'  
    app.config['JWT_ALGORITHM'] = 'HS256' 


    jwt = JWTManager(app)

    from app.routes import authRoute, userRoutes, carbonfootprintRoute, challengeRoute, completechallengeRoute

    app.register_blueprint(authRoute.bp)
    app.register_blueprint(userRoutes.bp)
    app.register_blueprint(carbonfootprintRoute.bp)
    app.register_blueprint(challengeRoute.bp)
    app.register_blueprint(completechallengeRoute.bp)

    with app.app_context():
        db.create_all()

    return app
