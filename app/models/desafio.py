from app import db
from datetime import datetime

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    goal = db.Column(db.String(255), nullable=False)
    reward = db.Column(db.Integer, nullable=False)  
    icon = db.Column(db.String(50)) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_challenges = db.relationship('UserChallenge', back_populates='challenge')