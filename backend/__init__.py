from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Inicializa las extensiones una sola vez
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Configuraciones de la aplicación
    app.config['SECRET_KEY'] = os.urandom(24)  # Genera una clave secreta aleatoria
    app.config.from_object('config.Config')  # Carga la configuración desde config.py

    # Inicializa las extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Página de login por defecto

    # Cargador de usuarios para Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from backend.models.user import Usuario  # Asegúrate de que el modelo está correctamente importado
        return Usuario.query.get(int(user_id))

    # Registra los blueprints (rutas) para la aplicación
    from backend.routes import HuellaCarbonoRoutes, authRoutes
    app.register_blueprint(HuellaCarbonoRoutes.bp)
    app.register_blueprint(authRoutes.bp)

    return app
