from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')

    db.init_app(app)


    from app.routes import userRoute

    app.register_blueprint(userRoute.bp)

    
    with app.app_context():
        db.create_all()

    return app
 
