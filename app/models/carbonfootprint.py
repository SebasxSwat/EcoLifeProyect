from app import db

class CarbonFootprint(db.Model):
    __tablename__ = 'carbon_footprint'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    value = db.Column(db.Float, nullable=False)

    user = db.relationship('User', backref=db.backref('carbon_footprints', lazy=True))

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "value": self.value
        }
