from app import db

class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(50))

    user_badges = db.relationship('UserBadge', back_populates='badge')

    def __repr__(self):
        return f'<Badge name={self.name}>'

    def jsonfy(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'icon': self.icon,
            'user_badges': [user_badge.jsonfy() for user_badge in self.user_badges]  # Asumiendo que UserBadge tiene un método jsonfy
        }
