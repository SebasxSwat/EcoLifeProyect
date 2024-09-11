from app import db
from datetime import datetime

class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.String(255), nullable=True)  # Ruta del icono
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_badges = db.relationship('UserBadge', back_populates='badge')