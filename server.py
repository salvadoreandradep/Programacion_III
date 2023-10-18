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
        return "Usuario o contraseña incorrectos"




if __name__ == '__main__':
    app.run(debug=True, port=3000)