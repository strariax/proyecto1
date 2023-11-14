from flask import render_template, request, redirect, url_for
from conexion import app, db
from models import Usuarios, Gastos

@app.route('/',methods =['POST','GET'])

def index():

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']
        correo = request.form['correo']

        # Creamos un objeto de la clase usuario con los datos obtenidos

        datos_usuario = Usuarios(nombre, apellido, cedula, correo)

        db.session.add(datos_usuario)
        db.session.commit()

        return render_template('/cargar_gastos.html')

    return render_template('index.html')

# CRUD (Crear, Leer, Actualizar, Eliminar)

@app.route('/cargar_gastos', methods = ['POST', 'GET'])
def cargar_gastos():

    if request.method == 'POST':
        categoria = request.form['categoria']
        fecha_de_gasto = request.form['fecha_de_gasto']
        monto = request.form['monto']
        descripcion = request.form['descripcion']

        gastos_registrados = Gastos(categoria, fecha_de_gasto, monto, descripcion)

        db.session.add(gastos_registrados)
        db.session.commit()

        return render_template('cargar_gastos.html')

    return render_template('cargar_gastos.html')

@app.route('/mostrar_gastos', methods = ['GET', 'POST'])
def mostrar_gastos():
    lista_de_gastos = Gastos.query.all()
    return render_template('mostrar_gastos.html', lista_de_gastos=lista_de_gastos)


@app.route('/actualizar/<int:gasto_id>', methods=['GET','POST'])
def actualizar(gasto_id):
    gasto_a_actualizar = Gastos.query.get(gasto_id)

    if request.method == 'POST':
        categoria = request.form['categoria']
        fecha_de_gasto = request.form['fecha_de_gasto']
        monto = request.form['monto']
        descripcion = request.form['descripcion']

        gasto_a_actualizar.categoria = categoria
        gasto_a_actualizar.fecha_de_gasto = fecha_de_gasto
        gasto_a_actualizar.monto = monto
        gasto_a_actualizar.descripcion = descripcion

        db.session.commit()

        return redirect(url_for('mostrar_gastos'))
    
    return render_template("actualizar.html", gasto_a_actualizar=gasto_a_actualizar)

@app.route('/eliminar', methods = ['GET','POST'])
def eliminar():
    if request.method == 'POST':
        id = request.form['gasto_id']
        gasto_a_eliminar = Gastos.query.filter_by(id=id).first()

        db.session.delete(gasto_a_eliminar)
        db.session.commit()

        return redirect(url_for('mostrar_gastos'))
    
if __name__ == ("__main__"):
    app.run(debug = True, port=8000)