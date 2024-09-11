from app import db
from datetime import datetime

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Corregido 'user.id' a 'users.id'
    message = db.Column(db.Text, nullable=False)
    read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('Users', backref=db.backref('notifications', lazy='dynamic'))

    def __repr__(self):
        return f'<Notification user_id={self.user_id} message={self.message[:20]}>'  # Mostrar solo los primeros 20 caracteres del mensaje para evitar sobrecargar el log

    def jsonfy(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'message': self.message,
            'read': self.read,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'user': self.user.jsonfy() if self.user else None  # Asumiendo que Users tiene un método jsonfy
        }
