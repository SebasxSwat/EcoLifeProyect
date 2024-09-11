from app import db
from datetime import datetime

class Challenge(db.Model):
    __tablename__ = 'challenges'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    goal = db.Column(db.String(255), nullable=False)
    reward = db.Column(db.Integer, nullable=False)  
    icon = db.Column(db.String(50)) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación con UserChallenge
    user_challenges = db.relationship('UserChallenge', back_populates='challenge', cascade='all, delete-orphan')

    # Relación secundaria con Users
    users_completed = db.relationship('Users', secondary='user_challenges', back_populates='completed_challenges')

    def __repr__(self):
        return f'<Challenge {self.title}>'

    def jsonfy(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'goal': self.goal,
            'reward': self.reward,
            'icon': self.icon,
            'created_at': self.created_at.isoformat(),  # Formato de fecha ISO 8601
            'user_challenges': [uc.jsonfy() for uc in self.user_challenges],  # Asumiendo que UserChallenge también tiene un método jsonfy
            'users_completed': [user.jsonfy() for user in self.users_completed]  # Asumiendo que Users también tiene un método jsonfy
        }
