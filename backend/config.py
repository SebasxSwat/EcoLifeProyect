#Configuracion de la base de datos

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/ecolife'
    SQLALCHEMY_TRACK_MODIFICATIONS = False