<<<<<<< HEAD:backend/models/notificacion.py
from backend import db
from datetime import datetime
=======
from app import db
>>>>>>> be0fbd8c6dbd2242e7ca5ac5c0688c99fde2483d:backend/app/models/notificacion.py

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('notifications', lazy='dynamic'))
