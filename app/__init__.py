from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configura la aplicación desde el archivo de configuración
    app.config.from_object('config.Config')  # Asegúrate de que 'config.Config' esté correctamente definido en config.py

    # Inicializa la extensión SQLAlchemy con la aplicación Flask
    db.init_app(app)

    from app.routes import login_routes
    from app.routes import challenges_routes
    from app.routes import badge_routes

    app.register_blueprint(login_routes.bp)
    app.register_blueprint(challenges_routes.bp)
    app.register_blueprint(badge_routes.bp)  # Usa '/auth' como prefijo para las rutas de login
    
    # Crear tablas en la base de datos si no existen
    with app.app_context():
        db.create_all()

    return app
