from app import db

class Challenge(db.Model):
    __tablename__ = 'challenges'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    # Relaciones
    category = db.relationship('Category', back_populates='challenges')
    user_challenges = db.relationship('UserChallenge', back_populates='challenge', cascade='all, delete-orphan')
    users_completed = db.relationship('User', secondary='user_challenges', back_populates='completed_challenges')

    def __repr__(self):
        return f'<Challenge {self.title}>'