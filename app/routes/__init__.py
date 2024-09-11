from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicialización de la aplicación y la base de datos
app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importa las rutas desde los diferentes módulos
from challenges_routes import challenges_bp

# Aquí puedes importar otras rutas, como usuarios, productos, etc.
# from user_routes import user_bp
# from product_routes import product_bp

# Registro de blueprints
app.register_blueprint(challenges_bp)


# Registro de otras rutas si las tienes
# app.register_blueprint(user_bp)
# app.register_blueprint(product_bp)

# Configuración adicional
@app.route('/')
def index():
    return "Welcome to Ecolife!"

if __name__ == '__main__':
    app.run(debug=True)
