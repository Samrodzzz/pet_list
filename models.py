from flask_sqlalchemy import SQLAlchemy

# Inicializar la extension SQLALCHEMY

db = SQLAlchemy()

# Definimos una clase que representa una tabla en la base de datos

class Mascotas(db.Model): # Heredando de la clase 
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    raza = db.Column(db.String(20), nullable=False)
    servicio = db.Column(db.String, nullable=False)
    duenho = db.Column(db.String, nullable=False)
    fecha = db.Column(db.String, nullable=False)
    costo = db.Column(db.Integer, nullable = False)

    # Constructor de clase

    def __init__(self, nombre,tipo, raza, servicio, duenho, fecha,costo):
        self.nombre = nombre
        self.tipo = tipo
        self.raza = raza
        self.servicio = servicio
        self.duenho = duenho
        self.fecha = fecha 
        self.costo = costo
        
