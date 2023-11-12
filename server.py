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
def guardar():
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



@app.route('/modificar/<int:producto_id>', methods=['GET'])
def modificar_producto(producto_id):
    # Recuperar información del producto de la base de datos
    cursor.execute("SELECT * FROM Productos WHERE idProducto = %s", (producto_id,))
    producto = cursor.fetchone()

    # Renderizar la plantilla con el formulario de modificación
    return render_template('modificar_producto.html', producto=producto)


@app.route('/actualizar/<int:producto_id>', methods=['POST'])
def actualizar_producto(producto_id):
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    stock = request.form['stock']

    # Actualizar producto en la base de datos
    update_query = "UPDATE Productos SET nombre=%s, descripcion=%s, precio=%s, stock=%s WHERE idProducto=%s"
    cursor.execute(update_query, (nombre, descripcion, precio, stock, producto_id))
    db.commit()

    return redirect('/producto')

##Administracion de proveedor.......................................................................
@app.route('/proveedor')
def mostrar_proveedores():
    cursor = db.cursor()
    sql = "SELECT * FROM Proveedores"
    cursor.execute(sql)
    proveedores = cursor.fetchall()
    return render_template('proveedores.html', proveedores=proveedores)




@app.route('/guardar_proveedor', methods=['POST'])
def guardar_proveedor():
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']

    cursor = db.cursor()
    sql = "INSERT INTO Proveedores (nombre, direccion, telefono) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, direccion, telefono))
    db.commit()

    return redirect('/proveedor')






## Administracion de Empleados................................................................


## Extras.....................................................................................
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








## Area Inicial........................................................

@app.route('/')
def formulario():
    return render_template('login.html')


@app.route('/inicio')
def Inicio():
    return render_template('inicio.html')


@app.route('/seguridad')
def seguridad():
    return render_template('seguridad.html')

@app.route('/login1')
def login1():
    return render_template('login1.html')

@app.route('/admin')
def admin():
    return render_template('administracion.html')

## Area Administrativa.................................................



@app.route('/producto')
def producto():
    return render_template('productos.html')



@app.route('/proveedor')
def proveedore():
    return render_template('proveedores.html')





if __name__ == '__main__':
    app.run(debug=True, port=3000)
