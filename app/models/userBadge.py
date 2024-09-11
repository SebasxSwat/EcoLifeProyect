from app import db
from datetime import datetime

class UserBadge(db.Model):
    __tablename__ = 'userbadge'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    badge_id = db.Column(db.Integer, db.ForeignKey('badge.id'), nullable=False)
    earned_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('Users', backref=db.backref('badges', lazy='dynamic'))
    badge = db.relationship('Badge', back_populates='user_badges')

    def __repr__(self):
        return f'<UserBadge user_id={self.user_id} badge_id={self.badge_id}>'

    def jsonfy(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'badge_id': self.badge_id,
            'earned_at': self.earned_at.isoformat() if self.earned_at else None,
            'user': self.user.jsonfy() if self.user else None,  # Asumiendo que Users tiene un método jsonfy
            'badge': self.badge.jsonfy() if self.badge else None  # Asumiendo que Badge tiene un método jsonfy
        }
