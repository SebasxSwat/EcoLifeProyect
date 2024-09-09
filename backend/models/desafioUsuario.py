from backend import db

class DesafioUsuario(db.Model):
    __tablename__ = 'desafio_usuario'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.idUser'), nullable=False)
    desafio_id = db.Column(db.Integer, db.ForeignKey('desafio.id'), nullable=False)
    fecha_completado = db.Column(db.DateTime)
    progreso = db.Column(db.Integer, nullable=False, default=0)  # Valor entre 0 y 100
