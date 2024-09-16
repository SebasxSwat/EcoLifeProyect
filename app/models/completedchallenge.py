from app import db

class CompletedChallenge(db.Model):
    __tablename__ = 'completed_challenges'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenges.id'), nullable=False)

    user = db.relationship('User', back_populates='completed_challenges')
    challenge = db.relationship('Challenge', back_populates='completed_challenges')

    def to_json(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "challenge_id": self.challenge_id
        }