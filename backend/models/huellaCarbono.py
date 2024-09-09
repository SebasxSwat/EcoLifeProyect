from datetime import datetime
from backend import db

class HuellaCarbono(db.Model):
    __tablename__ = 'huella_carbono'

    idHuella = db.Column(db.Integer, primary_key=True)
    fecha_calculo = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    transporte_tipo = db.Column(db.String(50), nullable=False)
    distancia_transporte = db.Column(db.Float, nullable=False)
    emisiones_transporte = db.Column(db.Float, nullable=False)
    consumo_electricidad = db.Column(db.Float, nullable=False)
    consumo_gas_natural = db.Column(db.Float, nullable=False)
    emisiones_energia = db.Column(db.Float, nullable=False)
    dispositivos_electronicos = db.Column(db.Integer, nullable=False)
    emisiones_electronica = db.Column(db.Float, nullable=False)
    huella_total_mensual = db.Column(db.Float, nullable=False)
    porcentaje_mensual = db.Column(db.Float, nullable=False)
    estado_mensual = db.Column(db.String(50), nullable=False)  


    user_id = db.Column(db.Integer, db.ForeignKey('usuario.idUser'), nullable=False)

    usuario = db.relationship('Usuario', back_populates='huellas_carbono')