
from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)    
    lastname = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))
    first_login = db.Column(db.Boolean, default=True)
    eco_score = db.Column(db.Integer, default=0)

    carbon_footprint = db.relationship('CarbonFootprint', back_populates='user', uselist=False)
    completed_challenges = db.relationship('CompletedChallenge', back_populates='user')
    badges = db.relationship('Badge', backref='user', lazy=True)       

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
        }
