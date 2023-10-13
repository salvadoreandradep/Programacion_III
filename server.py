from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__, template_folder='templates')

usuarios = {'1': '1'}


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_freund"
)


@app.route('/')
def formulario():
    return render_template('login.html')


@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/productos.html')
def productos():
    return render_template('productos.html')

@app.route('/empleados.html')
def empleados():
    return render_template('empleados.html')


@app.route('/guardar', methods=['POST'])
def guardar():
    cursor = db.cursor()
    codigo = request.form['txtCodigoAlumnos']
    nombre = request.form['txtNombreAlumnos']
    direccion = request.form['txtDireccionAlumnos']
    telefono = request.form['txtTelefonoAlumnos']


    query = "INSERT INTO alumnos (codigo, nombre, direccion, telefono) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (codigo, nombre, direccion, telefono))
    db.commit()
    cursor.close()

    return redirect(url_for('formulario'))



@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in usuarios and usuarios[username] == password:
    
        return redirect(url_for('inicio'))
    else:
        return "Nombre de usuario o contraseña incorrectos"

if __name__ == '__main__':
    app.run(debug=True, port=3000)