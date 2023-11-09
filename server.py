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

@app.route('/producto')
def tabla_productos():
    cursor = db.cursor()
    cursor.execute("SELECT nombre, marca, area, disponibilidad FROM producto")
    alumnos = cursor.fetchall()
    return render_template('productos.html', alumnos=alumnos)


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
    return redirect('producto')





@app.route("/reportes")
def view_reports():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `problemas`")
    reports = cursor.fetchall()
    return render_template("reportes.html", reports=reports)



@app.route("/submit_report", methods=["POST"])
def submit_report():
    hora = request.form["hora"]
    dia = request.form["dia"]
    problema = request.form["problema"]
    empleado_nombre = request.form["empleado_nombre"]

    cursor = db.cursor()
    insert_query = "INSERT INTO problemas (hora, dia, problema, empleado_nombre) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (hora, dia, problema, empleado_nombre))
    db.commit()

    return redirect(url_for("Inicio"))


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



@app.route('/Rlogin', methods=['POST'])
def Relogin():
    username = request.form['username']
    password = request.form['password']
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = %s AND contrasena = %s", (username, password))
    user = cursor.fetchone()
    if user:
        return redirect(url_for('admin'))
    else:
       error = "Contraseña incorrecta. Inténtalo de nuevo."
    return render_template('login1.html', error=error)










@app.route('/')
def formulario():
    return render_template('login.html')


@app.route('/inicio')
def Inicio():
    return render_template('inicio.html')


@app.route('/reportes')
def reporte():
    return render_template('reportes.html')


@app.route('/seguridad')
def seguridad():
    return render_template('seguridad.html')

@app.route('/login1')
def login1():
    return render_template('login1.html')


@app.route('/admin')
def admin():
    return render_template('administracion.html')

@app.route('/producto')
def producto():
    return render_template('productos.html')

@app.route('/cliente')
def cliente():
    return render_template('clientes.html')


@app.route('/empleado')
def empleado():
    return render_template('empleados.html')


@app.route('/proveedore')
def proveedore():
    return render_template('proveedores.html')


@app.route('/bitacora')
def bitacora():
    return render_template('bitacora.html')

@app.route('/reportetabla')
def reportete():
    return render_template('reportetabla.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
