# pip install opencv-contrib-python
from cv2 import cv2
imagen=cv2.imread('contorno.jpg')
grises=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
umbral=cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)

# Mostrar
cv2.imshow('imagen original', imagen)
cv2.imshow('imagen en escala de grises', grises)
cv2.waitKey(0)
cv2.destroyAllWindows()