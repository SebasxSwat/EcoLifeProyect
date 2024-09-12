from app import db
from datetime import datetime

class EcoActivity(db.Model):
    __tablename__ = 'ecoactividad'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Corregido 'user.id' a 'users.id'
    activity_type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('Users', back_populates='activities')  # Corregido 'User' a 'Users'

    def __repr__(self):
        return f'<EcoActivity user_id={self.user_id} activity_type={self.activity_type}>'

    def jsonfy(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'activity_type': self.activity_type,
            'value': self.value,
            'unit': self.unit,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
            'user': self.user.jsonfy() if self.user else None  # Asumiendo que Users tiene un método jsonfy
        }
