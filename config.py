import os

class Config:
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/ecolife'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'resetecolife@gmail.com'
    MAIL_PASSWORD = 'akgu mndo peif aguy' 
    MAIL_DEFAULT_SENDER = '1097664747f@gmail.com'

    JWT_SECRET_KEY = 'ecolifepassword'
    JWT_ALGORITHM = 'HS256'


# import os

# class Config:
    
#     USER = os.getenv('MYSQLUSER', 'root')
#     PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD', 'qcTcijBSbRspLEWTuSqOZCmXIuiRxeLr')
#     HOST = os.getenv('RAILWAY_PRIVATE_DOMAIN', 'autorack.proxy.rlwy.net')
#     PORT = os.getenv('MYSQL_PORT', 17381)
#     DATABASE = os.getenv('MYSQL_DATABASE', 'ecolife')

#     SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

#     MAIL_SERVER = 'smtp.gmail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = 'resetecolife@gmail.com'
#     MAIL_PASSWORD = 'akgu mndo peif aguy' 
#     MAIL_DEFAULT_SENDER = '1097664747f@gmail.com'

#     JWT_SECRET_KEY = 'ecolifepassword'
#     JWT_ALGORITHM = 'HS256'
