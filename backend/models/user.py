from backend import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    idUser = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    # Relaciones
    huellas_carbono = db.relationship('HuellaCarbono', back_populates='usuario')
    sugerencias_personalizadas = db.relationship('SugerenciaPersonalizada', backref='usuario', lazy=True)
    desafios_usuario = db.relationship('DesafioUsuario', backref='usuario', lazy=True)
    notificaciones = db.relationship('Notificacion', backref='usuario', lazy=True)
