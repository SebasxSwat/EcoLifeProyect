from backend import db

class Desafio(db.Model):
    __tablename__ = 'desafio'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)  # transporte, energia, alimentacion, consumo
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_fin = db.Column(db.DateTime, nullable=False)
    recompensa_puntos = db.Column(db.Integer, nullable=False)

    # Relaciones
    desafios_usuario = db.relationship('DesafioUsuario', backref='desafio', lazy=True)
