<<<<<<< HEAD:backend/models/user.py
from backend import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
=======
from app import db
>>>>>>> be0fbd8c6dbd2242e7ca5ac5c0688c99fde2483d:backend/app/models/user.py

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    location = db.Column(db.String(100))
    avatar = db.Column(db.String(255))
    role = db.Column(db.String(20), default='user')  
    eco_score = db.Column(db.Integer, default=0)
    carbon_footprint = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    challenges = db.relationship('UserChallenge', back_populates='user')
    activities = db.relationship('EcoActivity', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)