from app import db

class Insignia(db.Model):

    __tablename__ = 'insignias'

    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(200), nullable=False) 
    
    user_badges = db.relationship('UserBadge', back_populates='insignias')
