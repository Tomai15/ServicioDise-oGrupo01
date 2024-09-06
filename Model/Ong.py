from Model.Persistente import Persistente
from database import db


class Ong(Persistente):
    __tablename__ = 'Ongs'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50), nullable=False)
    ubicacionId = db.Column(db.Integer, db.ForeignKey('Ubicaciones.id'), nullable=False)
    ubicacion  = db.relationship('Ubicacion', backref='ong', lazy=True)

    def __init__(self, nombre, direccion, ubicacion):
        self.nombre = nombre
        self.direccion = direccion
        self.ubicacion = ubicacion


