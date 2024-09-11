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
    user = db.relationship('Users', back_populates='user_challenges')
    challenge = db.relationship('Challenge', back_populates='user_challenges')

    def __init__(self, user_id, challenge_id, points_earned):
        self.user_id = user_id
        self.challenge_id = challenge_id
        self.points_earned = points_earned

    def __repr__(self):
        return f'<UserChallenge user_id={self.user_id} challenge_id={self.challenge_id}>'

    def jsonfy(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'challenge_id': self.challenge_id,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'points_earned': self.points_earned,
            'user': self.user.jsonfy() if self.user else None,  # Asumiendo que Users tiene un método jsonfy
            'challenge': self.challenge.jsonfy() if self.challenge else None  # Asumiendo que Challenge tiene un método jsonfy
        }
