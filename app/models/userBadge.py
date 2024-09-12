from app import db

class UserBadge(db.Model):

    __tablename__ = 'user_badges'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    insignia_id = db.Column(db.Integer, db.ForeignKey('insignias.id'), nullable=False)

    user = db.relationship('Users', backref=db.backref('insignias', lazy='dynamic'))
    badge = db.relationship('Insignia', back_populates='user_badges')