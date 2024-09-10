from backend import db

class UserChallenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id'), nullable=False)
    status = db.Column(db.String(20), default='available') 
    completed_at = db.Column(db.DateTime)

    user = db.relationship('User', back_populates='challenges')
    challenge = db.relationship('Challenge', back_populates='user_challenges')