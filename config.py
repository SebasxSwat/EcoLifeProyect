import os

class Config:
   
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/ecolife'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

 
    MAIL_SERVER = 'smtp.gmail.com'  # Cambia esto si usas otro proveedor de correo
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'tu_correo@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'tu_contraseña_de_correo'
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'tu_correo@gmail.com'

    # Clave secreta para Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_muy_segura'