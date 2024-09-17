from app import db

class Badge(db.Model):
    
    __tablename__ = 'badges'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255))
    required_challenges = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    users = db.relationship('User', back_populates='badges')

    def to_json(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "required_challenges": self.required_challenges,
            "user_id": self.user_id
        }