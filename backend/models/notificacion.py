from backend import db

class Notificacion(db.Model):
    __tablename__ = 'notificacion'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.idUser'), nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # desafio, recurso, general
    fecha_envio = db.Column(db.DateTime, nullable=False)
    leida = db.Column(db.Boolean, default=False)
