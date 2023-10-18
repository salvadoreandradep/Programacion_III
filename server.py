from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__, template_folder='templates')

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_freund"
)

@app.route('/clientes')
def tabla_alumnos():
    cursor = db.cursor()
    cursor.execute("SELECT nombre, apellido, dui , telefono FROM clientes")
    alumnos = cursor.fetchall()
    return render_template('clientes.html', alumnos=alumnos)

@app.route('/eliminar_cliente', methods=['POST'])
def eliminar_alumno():
    codigo = request.form['codigo']
    cursor = db.cursor()
    cursor.execute("DELETE FROM `clientes` WHERE nombre =  %s", (codigo,))
    db.commit()
    return redirect('/clientes')






@app.route('/productos')
def tabla_productos():
    cursor = db.cursor()
    cursor.execute("SELECT nombre, marca, area, disponibilidad FROM producto")
    alumnos = cursor.fetchall()
    return render_template('productos.html', alumnos=alumnos)






@app.route('/')
def formulario():
    return render_template('principal.html')


@app.route('/login')
def loginP():
    return render_template('login.html')

@app.route('/register')
def Inicio():
    return render_template('inicio.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')


@app.route('/productos')
def producto():
    return render_template('productos.html')

@app.route('/empleados')
def empleados():
    return render_template('empleados.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = %s AND contrasena = %s", (username, password))
    user = cursor.fetchone()
    if user:
        return redirect(url_for('Inicio'))
    else:
       error = "Contraseña incorrecta. Inténtalo de nuevo."
    return render_template('login.html', error=error)
    
        





@app.route('/guardar', methods=['POST'])
def guardar():
    cursor = db.cursor()
    codigo = request.form['txtCodigoAlumnos']
    nombre = request.form['txtNombreAlumnos']
    direccion = request.form['txtDireccionAlumnos']
    telefono = request.form['txtTelefonoAlumnos']


    query = "INSERT INTO clientes (nombre, apellido, dui, telefono) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (codigo, nombre, direccion, telefono))
    db.commit()
    cursor.close()

    return redirect(url_for('clientes'))


@app.route('/guardarP', methods=['POST'])
def guardarP():
    cursor = db.cursor()
    codigo = request.form['txtCodigoAlumnos']
    nombre = request.form['txtNombreAlumnos']
    direccion = request.form['txtDireccionAlumnos']
    telefono = request.form['txtTelefonoAlumnos']


    query = "INSERT INTO producto (nombre, marca, area, disponibilidad) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (codigo, nombre, direccion, telefono))
    db.commit()
    cursor.close()

    return redirect(url_for('producto'))



@app.route('/eliminar_producto', methods=['POST'])
def eliminar_producto():
    codigo = request.form['codigo']
    cursor = db.cursor()
    cursor.execute("DELETE FROM `producto` WHERE nombre =  %s", (codigo,))
    db.commit()
    return redirect('productos')







if __name__ == '__main__':
    app.run(debug=True, port=3000)