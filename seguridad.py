import cv2

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
