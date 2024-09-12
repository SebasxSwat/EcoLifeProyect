from app import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    # Relaciones
    challenges = db.relationship('Challenge', back_populates='category', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Category name={self.name}>'

    def jsonfy(self):
        return {
            'id': self.id,
            'name': self.name,
            'challenges': [challenge.jsonfy() for challenge in self.challenges]  # Asumiendo que Challenge tiene un método jsonfy
        }
