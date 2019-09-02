import cv2 as cv
import numpy as np

imgOriginal = cv.imread("C:\Users\megan\Desktop\Curso Udemy - Visao computacional com Python e OpenCV\Parte 3\Imagens\einstein.jpg")
totalLinhas, totalColunas = imgOriginal.shape[:2]

matriz = np.float32([[1,0,100],[0,1,100]])
imgDeslocada = cv.warpAffine(imgOriginal, matriz, (totalColunas, totalLinhas))

cv.imshow("Imagem Deslocada", imgDeslocada)
cv.waitKey(0)
cv.destroyAllWindows()
