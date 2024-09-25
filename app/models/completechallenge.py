from app import db

class CompletedChallenge(db.Model):
    
    __tablename__ = 'completed_challenges'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenges.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('completed_challenges', lazy=True))
    challenge = db.relationship('Challenge', backref=db.backref('completed_challenges', lazy=True))

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "challenge_id": self.challenge_id,
        }
