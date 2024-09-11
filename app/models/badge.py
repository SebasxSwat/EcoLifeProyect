from app import db
from datetime import datetime

class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.String(255), nullable=True)  # Ruta del icono
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_badges = db.relationship('UserBadge', back_populates='badge')

    def __repr__(self):
        return f'<Badge name={self.name}>'

    def jsonfy(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'icon': self.icon,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'user_badges': [user_badge.jsonfy() for user_badge in self.user_badges]  # Asumiendo que UserBadge tiene un método jsonfy
        }
