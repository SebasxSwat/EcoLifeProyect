from app import db

class Challenge(db.Model):
    __tablename__ = 'challenges'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    points = db.Column(db.Integer, nullable=False)
    carbon_reduction = db.Column(db.Float, nullable=False)
    challenge_type = db.Column(db.String(50)) 

    completed_challenges = db.relationship('CompletedChallenge', back_populates='challenge')

    def to_json(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "points": self.points,
            "carbon_reduction": self.carbon_reduction,
            "challenge_type": self.challenge_type
        }