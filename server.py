from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
import cv2

app = Flask(__name__, template_folder='templates')

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_freund"
)

cap = cv2.VideoCapture(0)

# Inicializa el detector de movimiento
motion_detector = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Aplica el detector de movimiento para obtener la máscara de movimiento
    mask = motion_detector.apply(frame)

    # Procesa la máscara para eliminar el ruido y resaltar las regiones de movimiento
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Encuentra los contornos de las regiones de movimiento
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 2000:  # Ajusta el valor para el umbral de detección
            # Dibuja un rectángulo alrededor de la región de movimiento
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Muestra el video con la detección de movimiento
    cv2.imshow('Detección de Movimiento', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Presiona Esc para salir
        break

# Libera la captura de video y cierra todas las ventanas
cap.release()
cv2.destroyAllWindows()


















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












if __name__ == '__main__':
    app.run(debug=True, port=3000)
