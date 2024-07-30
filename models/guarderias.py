from db import db
from models.cuidadores import Cuidadores

class Guarderias(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(192), nullable = False)
    direccion = db.Column(db.String, nullable = False)
    telefono = db.Column(db.String(45), nullable = False)

    cuidadores = db.relationship('Cuidadores', backref='guarderias', lazy=True)
    perros = db.relationship('Perros', backref='guarderias', lazy=True)