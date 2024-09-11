from app import db
from datetime import datetime

class UserChallenge(db.Model):
    __tablename__ = 'user_challenges'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenges.id'), nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    points_earned = db.Column(db.Integer, nullable=False)

    # Relaciones
    user = db.relationship('User', back_populates='user_challenges')
    challenge = db.relationship('Challenge', back_populates='user_challenges')

    def __init__(self, user_id, challenge_id, points_earned):
        self.user_id = user_id
        self.challenge_id = challenge_id
        self.points_earned = points_earned
