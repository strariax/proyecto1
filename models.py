from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicializar la extension SQLALCHEMY

db = SQLAlchemy()

# Definimos una clase que representa una tabla en la base de datos

class Usuarios(db.Model): # Heredando de la clase 
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellido = db.Column(db.String(20), nullable=False)
    cedula = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String, nullable=False)

    # Constructor de clase

    def __init__(self, nombre, apellido, cedula, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo

class Gastos(db.Model):
    __bind_key__ = 'gastos' 
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String, nullable=False)
    fecha_de_gasto = db.Column(db.Integer, nullable=False)
    monto = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String)


    def __init__(self, categoria, fecha_de_gasto, monto, descripcion):
        self.categoria = categoria
        self.fecha_de_gasto = fecha_de_gasto
        self.monto = monto
        self.descripcion = descripcion

