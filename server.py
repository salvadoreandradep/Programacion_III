from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__, template_folder='templates')

# Configura la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_freund"
)

# Ruta para mostrar el formulario
@app.route('/')
def formulario():
    return render_template('index.html')

# Ruta para procesar los datos del formulario
@app.route('/guardar', methods=['POST'])
def guardar():
    cursor = db.cursor()
    codigo = request.form['txtCodigoAlumnos']
    nombre = request.form['txtNombreAlumnos']
    direccion = request.form['txtDireccionAlumnos']
    telefono = request.form['txtTelefonoAlumnos']

    # Inserta los datos en la base de datos
    query = "INSERT INTO alumnos (codigo, nombre, direccion, telefono) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (codigo, nombre, direccion, telefono))
    db.commit()
    cursor.close()

    return redirect(url_for('formulario'))

if __name__ == '__main__':
    app.run(debug=True, port=3000)