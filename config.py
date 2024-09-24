import os

class Config:
   
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/ecolife'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

 
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '1097664747f@gmail.com'  
    MAIL_PASSWORD = '53089772fabian' 
    MAIL_DEFAULT_SENDER = '1097664747f@gmail.com'  