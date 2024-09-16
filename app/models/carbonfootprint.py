from app import db

class CarbonFootprint(db.Model):

    __tablename__ = 'carbon_footprint'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    value = db.Column(db.Float, nullable=False)

    user = db.relationship('User', back_populates='carbon_footprint')

    def to_json(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "value": self.value
        }