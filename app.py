from flask import render_template, request, redirect, url_for
from conexion import app, db
from models import Mascotas

@app.route('/')
def index():
    return render_template('index.html')

# CRUD (Crear, Leer, Actualizar, Eliminar)

@app.route('/cargar_datos', methods = ['POST', 'GET'])
def cargar_datos():

    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        servicio = request.form['servicio']
        raza = request.form['raza']
        duenho = request.form['duenho']
        fecha = request.form['fecha']
        costo = request.form['costo']



        # Creamos un objeto de la clase empleados con los datos obtenidos

        datos_mascotas = Mascotas(nombre,tipo,raza,servicio,duenho,fecha,costo)

        db.session.add(datos_mascotas)
        db.session.commit()
        
        return render_template('cargar_datos.html')

    return render_template('cargar_datos.html')

@app.route('/mostrar_datos', methods = ['GET', 'POST'])
def mostrar_datos():
    lista_mascotas = Mascotas.query.all()
    return render_template('mostrar_datos.html', lista_mascotas=lista_mascotas)

@app.route('/actualizar/<int:mascota_id>', methods=['GET','POST'])
def actualizar(mascota_id):
    mascota_a_actualizar = Mascotas.query.get(mascota_id)

    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        raza = request.form['raza']
        servicio = request.form['servicio']
        duenho = request.form['duenho']
        fecha = request.form['fecha']
        costo = request.form['costo']



        mascota_a_actualizar.nombre = nombre
        mascota_a_actualizar.tipo = tipo
        mascota_a_actualizar.raza = raza
        mascota_a_actualizar.servicio = servicio
        mascota_a_actualizar.duenho = duenho
        mascota_a_actualizar.fecha = fecha
        mascota_a_actualizar.costo = costo

        db.session.commit()

        return redirect(url_for('mostrar_datos'))
    
    return render_template("actualizar.html", mascota_a_actualizar=mascota_a_actualizar)

@app.route('/eliminar', methods = ['GET','POST'])
def eliminar():
    if request.method == 'POST':
        id = request.form['mascota_id']
        mascota_a_eliminar = Mascotas.query.filter_by(id=id).first()

        db.session.delete(mascota_a_eliminar)
        db.session.commit()

        return redirect(url_for('mostrar_datos'))
    
# if __name__ == ("__main__"):
    # app.run(debug = True, port=8000)