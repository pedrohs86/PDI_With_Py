import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\megan\\Desktop\\Curso Udemy - Visao computacional com Python e OpenCV\\Parte 3\\Imagens\\einstein.jpg",0)

imgEqualizada = cv2.equalizeHist(img)

cv2.imshow("Imagem Original", img)
cv2.imshow("Imagem Equalizada", imgEqualizada)

plt.hist(img.ravel(), 256, [0,256])
plt.figure()
plt.hist(imgEqualizada.ravel(), 256, [0,256])
plt.show()
