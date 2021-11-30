from cv2 import cv2

import numpy as np

original = cv2.imread('monedas.jpg')
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

#Mostrar resultado

cv2.imshow('Grises', gris)
cv2.waitKey(0)