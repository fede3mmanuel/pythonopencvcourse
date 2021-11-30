from cv2 import cv2

import numpy as np

valorGauss = 3
valorKernel = 3

original = cv2.imread('monedas.jpg')
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

gauss = cv2.GaussianBlur(gris, (valorGauss, valorKernel), 0)

#Mostrar resultado

cv2.imshow('Grises', gris)
cv2.imshow('Gaussian', gauss)
cv2.waitKey(0)