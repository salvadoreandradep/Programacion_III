import cv2

# Inicializa la captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Inicializa el detector de movimiento
motion_detector = cv2.createBackgroundSubtractorMOG2()

# Inicializa el clasificador de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Lee el frame de la cámara
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

            # Convierte la región de interés a escala de grises
            roi_gray = cv2.cvtColor(frame[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)

            # Detecta rostros en la región de interés
            faces = face_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=5)

            for (fx, fy, fw, fh) in faces:
                # Dibuja un rectángulo alrededor del rostro detectado
                cv2.rectangle(frame, (x + fx, y + fy), (x + fx + fw, y + fy + fh), (255, 0, 0), 2)

                # Guarda una captura de pantalla cuando se detecta un rostro
                cv2.imwrite("captura_rostro.png", frame)

    # Muestra el video con la detección de movimiento
    cv2.imshow('Detección de Movimiento', frame)

    # Sale del bucle cuando se presiona la tecla Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Libera la captura de video y cierra todas las ventanas
cap.release()
cv2.destroyAllWindows()

