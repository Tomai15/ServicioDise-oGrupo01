
from Model.Persistente import Persistente
from database import db


class Ubicacion(Persistente):
    __tablename__ = 'Ubicaciones'
    id = db.Column(db.Integer, primary_key=True)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float,nullable=False)

    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        