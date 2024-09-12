
from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))
    eco_score = db.Column(db.Integer, default=0)        
    carbon_footprint = db.Column(db.Float, default=0.0)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "eco_score": self.eco_score,
            "carbon_footprint": self.carbon_footprint
        }
