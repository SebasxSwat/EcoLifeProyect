from app import db

class SugerenciaPersonalizada(db.Model):
    __tablename__ = 'sugerencia_personalizada'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.idUser'), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)  
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    completada = db.Column(db.Boolean, default=False)
