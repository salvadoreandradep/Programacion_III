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

@app.route('/')
def tabla_alumnos():
    cursor = db.cursor()
    cursor.execute("SELECT nombre, apellido, dui , telefono FROM clientes")
    alumnos = cursor.fetchall()
    return render_template('principal.html', alumnos=alumnos)









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












if __name__ == '__main__':
    app.run(debug=True, port=3000)