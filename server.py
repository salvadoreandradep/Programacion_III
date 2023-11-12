from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error


app = Flask(__name__, template_folder='templates')

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mitienda"
)


cursor = db.cursor()

## Administracion de productos................................................................

@app.route('/producto')
def mostrar_productos():
    # Obtener productos de la base de datos
    cursor.execute("SELECT * FROM Productos")
    productos = cursor.fetchall()

    # Renderizar la plantilla con la lista de productos
    return render_template('productos.html', productos=productos)


@app.route('/guardar', methods=['POST'])
def guardarP():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    stock = request.form['stock']

    # Insertar datos en la base de datos
    insert_query = "INSERT INTO Productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (nombre, descripcion, precio, stock))
    db.commit()

    return redirect('/producto')

@app.route('/eliminar/<int:producto_id>', methods=['POST'])
def eliminar_producto(producto_id):
    # Eliminar producto de la base de datos
    delete_query = "DELETE FROM Productos WHERE idProducto = %s"
    cursor.execute(delete_query, (producto_id,))
    db.commit()

    return redirect('/producto')



##Administracion de clientes.......................................................................




## Administracion de Empleados................................................................



@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombreUsuario = %s AND contrasena = %s", (username, password))
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
    cursor.execute("SELECT * FROM usuarios WHERE nombreUsuario = %s AND contrasena = %s", (username, password))
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
