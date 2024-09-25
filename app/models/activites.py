from app import db
from datetime import datetime


class Activity(db.Model):
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_completed = db.Column(db.DateTime, default=datetime.utcnow)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenges.id'), nullable=False)

    user = db.relationship('User', back_populates='activities')
    challenge = db.relationship('Challenge', back_populates='activities')

    def to_json (self):
        return {
            "id": self.id,
            "date_completed": self.date_completed
        }