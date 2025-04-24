import cv2
import numpy as np

# Inicia a webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Converte para HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define a faixa da cor da tinta (ex: vermelho)
    lower_color = np.array([0, 100, 100])
    upper_color = np.array([10, 255, 255])

    # Máscara da cor
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Resultado final aplicando a máscara na imagem original
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Mostra as imagens
    cv2.imshow('Webcam - Original', frame)
    cv2.imshow('Detecção de Tinta', result)

    # Sai com 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()