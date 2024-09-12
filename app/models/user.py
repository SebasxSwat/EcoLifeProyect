from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db
from app.models.userChallenge import UserChallenge
from app.models.challenge import Challenge

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    eco_score = db.Column(db.Integer, default=0)        
    carbon_footprint = db.Column(db.Float, default=0.0)
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    # Relación con UserChallenge
    user_challenges = db.relationship('UserChallenge', back_populates='user', cascade='all, delete-orphan')

    # Relación secundaria con Challenge
    completed_challenges = db.relationship('Challenge', secondary='user_challenges', back_populates='users_completed')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def update_eco_score(self, points):
        self.eco_score += points
        db.session.commit()

    def update_carbon_footprint(self, value):
        self.carbon_footprint = value
        db.session.commit()

    def complete_challenge(self, challenge):
        if challenge not in self.completed_challenges:
            user_challenge = UserChallenge(user_id=self.id, challenge_id=challenge.id, points_earned=challenge.reward)
            db.session.add(user_challenge)
            self.update_eco_score(challenge.reward)
            db.session.commit()

    def __repr__(self):
        return f'<User {self.username}>'

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'eco_score': self.eco_score,
            'carbon_footprint': self.carbon_footprint,
            'date_registered': self.date_registered.isoformat() if self.date_registered else None,
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'completed_challenges': [challenge.jsonfy() for challenge in self.completed_challenges]  # Asumiendo que Challenge también tiene un método jsonfy
        }
