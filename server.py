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



@app.route('/')
def formulario():
    return render_template('login.html')


@app.route('/inicio')
def Inicio():
    return render_template('inicio.html')


@app.route('/reportes')
def reporte():
    return render_template('reportes.html')










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



if __name__ == '__main__':
    app.run(debug=True, port=3000)
