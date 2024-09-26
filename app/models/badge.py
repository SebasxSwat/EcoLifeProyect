from app import db

class Badge(db.Model):
    
    __tablename__ = 'badges'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)  
    description = db.Column(db.String(255)) 
    required_challenges = db.Column(db.Integer, nullable=False) 
    eco_points_required = db.Column(db.Integer, nullable=True)  
    trees_planted_required = db.Column(db.Integer, nullable=True)  
    water_saved_required = db.Column(db.Integer, nullable=True) 
    waste_recycled_required = db.Column(db.Integer, nullable=True)  
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  

    user_badges = db.relationship('UserBadge', back_populates='badge')

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "required_challenges": self.required_challenges,
            "eco_points_required": self.eco_points_required,
            "trees_planted_required": self.trees_planted_required,
            "water_saved_required": self.water_saved_required,
            "waste_recycled_required": self.waste_recycled_required,
            "user_id": self.user_id
        }
