from app import db
from datetime import datetime, timedelta
import secrets

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))
    first_login = db.Column(db.Boolean, default=True)
    eco_score = db.Column(db.Integer, default=0)
    trees_planted = db.Column(db.Integer, default=0)
    water_saved = db.Column(db.Float, default=0.0)  
    waste_recycled = db.Column(db.Float, default=0.0)  
    reset_token = db.Column(db.String(100), nullable=True)
    reset_token_expiry = db.Column(db.DateTime, nullable=True)
    role = db.Column(db.String(50), default='user')
    
    user_badges = db.relationship('UserBadge', back_populates='user')    
    activities = db.relationship('Activity', back_populates='user')    

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "lastname": self.lastname,
            "phone": self.phone,
            "email": self.email,
            "password": self.password,
            "first_login": self.first_login,
            "eco_score": self.eco_score,
            "trees_planted": self.trees_planted,
            "water_saved": self.water_saved,
            "waste_recycled": self.waste_recycled,
        }

    def set_password_reset_token(self):
        self.reset_token = secrets.token_urlsafe(32)
        self.reset_token_expiry = datetime.utcnow() + timedelta(hours=1)

    def check_password_reset_token(self, token):
        return self.reset_token == token and self.reset_token_expiry > datetime.utcnow()
