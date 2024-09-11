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

    user_challenges = db.relationship('UserChallenge', back_populates='challenge')

    # Método para convertir el modelo a un diccionario (JSON serializable)
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'goal': self.goal,
            'reward': self.reward,
            'icon': self.icon,
            'created_at': self.created_at.isoformat()  # Formato de fecha compatible con JSON
        }
