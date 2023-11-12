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


@app.route('/eliminar_proveedor', methods=['POST'])
def eliminar_proveedor():
    id_proveedor = request.form['id_proveedor']

    cursor = db.cursor()
    sql = "DELETE FROM Proveedores WHERE idProveedor = %s"
    cursor.execute(sql, (id_proveedor,))
    db.commit()

    return redirect('/proveedor')

@app.route('/modificar_proveedor', methods=['GET'])
def modificar_proveedor():
    id_proveedor = request.args.get('id_proveedor')

    cursor = db.cursor()
    sql = "SELECT * FROM Proveedores WHERE idProveedor = %s"
    cursor.execute(sql, (id_proveedor,))
    proveedor = cursor.fetchone()

    return render_template('modificar_proveedor.html', proveedor=proveedor)

@app.route('/guardar_modificacion', methods=['POST'])
def guardar_modificacion():
    id_proveedor = request.form['id_proveedor']
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']

    cursor = db.cursor()
    sql = "UPDATE Proveedores SET nombre=%s, direccion=%s, telefono=%s WHERE idProveedor=%s"
    cursor.execute(sql, (nombre, direccion, telefono, id_proveedor))
    db.commit()

    return redirect('/proveedor')

## Administracion de Cliente................................................................

@app.route('/cliente')
def mostrar_clientes():
 
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    return render_template('clientes.html', clientes=clientes)
    

@app.route('/guardar_cliente', methods=['POST'])
def guardar_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']

        # Inserta el nuevo cliente en la base de datos
        cursor.execute("INSERT INTO Clientes (nombre, direccion, telefono) VALUES (%s, %s, %s)",
                       (nombre, direccion, telefono))
        db.commit()

        return redirect('/cliente')
    
@app.route('/eliminar_cliente', methods=['POST'])
def eliminar_cliente():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        cursor.execute("DELETE FROM Clientes WHERE idCliente = %s", (id_cliente,))
        db.commit()

        return redirect('/cliente')
    

@app.route('/modificar_cliente', methods=['GET'])
def modificar_cliente():
    if request.method == 'GET':
        id_cliente = request.args.get('id_cliente')

        # Obtiene la información del cliente de la base de datos
        cursor.execute("SELECT * FROM Clientes WHERE idCliente = %s", (id_cliente,))
        cliente = cursor.fetchone()

        return render_template('modificar_cliente.html', cliente=cliente)
    

@app.route('/guardar_modificacionC', methods=['POST'])
def guardar_modificacionC():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']

        # Actualiza la información del cliente en la base de datos
        cursor.execute("UPDATE Clientes SET nombre=%s, direccion=%s, telefono=%s WHERE idCliente=%s",
                       (nombre, direccion, telefono, id_cliente))
        db.commit()

        return redirect('cliente')
   

## Administracion de empleados..............................................................  

@app.route('/empleados')
def mostrar_empleados():
    # Consulta la base de datos para obtener la lista de empleados
    cursor.execute("SELECT * FROM Empleados")
    empleados = cursor.fetchall()
    return render_template('empleados.html', empleados=empleados)


@app.route('/guardar_empleado', methods=['POST'])
def guardar_empleado():
    nombre = request.form['nombre']
    cargo = request.form['cargo']
    salario = request.form['salario']
    fecha_contratacion = request.form['fecha_contratacion']

    # Realiza la inserción en la base de datos
    cursor.execute("INSERT INTO Empleados (nombre, cargo, salario, fechaContratacion) VALUES (%s, %s, %s, %s)",
                   (nombre, cargo, salario, fecha_contratacion))
    db.commit()

    return redirect(url_for('empleados'))



@app.route('/eliminar_empleado', methods=['POST'])
def eliminar_empleado():
    id_empleado = request.form['id_empleado']

    # Realiza la eliminación en la base de datos
    cursor.execute("DELETE FROM Empleados WHERE idEmpleado = %s", (id_empleado,))
    db.commit()

    return redirect(url_for('empleados'))

@app.route('/editar_empleado', methods=['GET'])
def editar_empleado():
    id_empleado = request.args.get('id_empleado')

    # Consulta la base de datos para obtener los datos del empleado seleccionado
    cursor.execute("SELECT * FROM Empleados WHERE idEmpleado = %s", (id_empleado,))
    empleado = cursor.fetchone()

    return render_template('modificar_empleado.html', empleado=empleado)


@app.route('/guardar_edicion', methods=['POST'])
def guardar_edicion():
    id_empleado = request.form['id_empleado']
    nombre = request.form['nombre']
    cargo = request.form['cargo']
    salario = request.form['salario']
    fecha_contratacion = request.form['fecha_contratacion']

    # Actualiza los datos en la base de datos
    cursor.execute("UPDATE Empleados SET nombre = %s, cargo = %s, salario = %s, fechaContratacion = %s WHERE idEmpleado = %s",
                   (nombre, cargo, salario, fecha_contratacion, id_empleado))
    db.commit()

    return redirect(url_for('empleados'))


## Administracion de entradas...............................................................


@app.route("/entradas")
def index():
    # Consulta a la base de datos para obtener las opciones de Producto y Proveedor
    cursor.execute("SELECT idProducto, nombre FROM Productos")
    productos = cursor.fetchall()
    cursor.execute("SELECT idProveedor, nombre FROM Proveedores")
    proveedores = cursor.fetchall()
    


    cursor.execute("SELECT Entradas.idEntrada, Productos.nombre, Proveedores.nombre, Entradas.cantidad, Entradas.fechaEntrada FROM Entradas \
                    INNER JOIN Productos ON Entradas.idProducto = Productos.idProducto \
                    INNER JOIN Proveedores ON Entradas.idProveedor = Proveedores.idProveedor")
    entradas = cursor.fetchall()

    return render_template("entradas.html", productos=productos, proveedores=proveedores, entradas=entradas)



@app.route("/guardar_entrada", methods=["POST"])
def guardar_entrada():
    # Obtener datos del formulario
    id_producto = request.form.get("id_producto")
    id_proveedor = request.form.get("id_proveedor")
    cantidad = request.form.get("cantidad")
    fecha = request.form.get("fecha")

    # Insertar datos en la base de datos
    cursor.execute("INSERT INTO Entradas (idProducto, idProveedor, cantidad, fechaEntrada) VALUES (%s, %s, %s, %s)",
                   (id_producto, id_proveedor, cantidad, fecha))
    db.commit()

    return redirect(url_for('entradas'))



@app.route("/eliminar_entrada", methods=["POST"])
def eliminar_entrada():
    # Obtener el ID de la entrada a eliminar
    id_entrada = request.form.get("id_entrada")

    # Eliminar la entrada de la base de datos
    cursor.execute("DELETE FROM Entradas WHERE idEntrada = %s", (id_entrada,))
    db.commit()

    return redirect(url_for('entradas'))

## Administracion de salidas................................................................


@app.route('/salidas')
def salidasMOstras():
    # Obtén las opciones para idProducto y idCliente desde la base de datos
    cursor.execute("SELECT idProducto, nombre FROM Productos")
    productos = cursor.fetchall()

    cursor.execute("SELECT idCliente, nombre FROM Clientes")
    clientes = cursor.fetchall()


    cursor.execute("SELECT Salidas.idSalida, Productos.nombre AS nombre_producto, Clientes.nombre AS nombre_cliente, Salidas.cantidad, Salidas.fechaSalida "
                   "FROM Salidas "
                   "JOIN Productos ON Salidas.idProducto = Productos.idProducto "
                   "JOIN Clientes ON Salidas.idCliente = Clientes.idCliente")
    salidas = cursor.fetchall()

        
    return render_template('salidas.html', productos=productos, clientes=clientes, salidas=salidas)



@app.route('/guardar_salida', methods=['POST'])
def guardar_salida():
    try:
        # Obtiene los datos del formulario
        id_producto = request.form['id_producto']
        id_cliente = request.form['id_cliente']
        cantidad = request.form['cantidad']
        fecha_salida = request.form['fecha_salida']

        # Guarda los datos en la base de datos
        cursor.execute("INSERT INTO Salidas (idProducto, idCliente, cantidad, fechaSalida) VALUES (%s, %s, %s, %s)",
                       (id_producto, id_cliente, cantidad, fecha_salida))
        
        # Realiza el commit para aplicar los cambios en la base de datos
        db.commit()

        return redirect(url_for('salidas'))
    except Exception as e:
        
        db.rollback()
        return redirect(url_for('salidas'))


@app.route('/salida', methods=['POST'])
def eliminar_salida():
    
        id_salida = request.form['id_salida']

        # Elimina la salida de la base de datos
        cursor.execute("DELETE FROM Salidas WHERE idSalida = %s", (id_salida,))
        db.commit()

        return redirect('/salidas')
  














## Extras...................................................................................
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

@app.route('/cliente')
def cliente():
    return render_template('clientes.html')

@app.route('/empleados')
def empleados():
    return render_template('empleados.html')

@app.route('/entradas')
def entradas():
    return render_template('entradas.html')

@app.route('/salidas')
def salidas():
    return render_template('salidas.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
