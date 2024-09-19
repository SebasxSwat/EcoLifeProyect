from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')

    # Configuración de Flask-Mail
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Usa el servidor SMTP de tu proveedor de correo
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = app.config.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = app.config.get('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = app.config.get('MAIL_DEFAULT_SENDER')

    db.init_app(app)
    mail.init_app(app)

    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    from app.routes import authRoute, userRoutes

    app.register_blueprint(authRoute.bp)
    app.register_blueprint(userRoutes.bp)

    with app.app_context():
        db.create_all()

    return app