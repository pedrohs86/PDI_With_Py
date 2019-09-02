import cv2 as cv
import numpy as np

imgOrigin = cv.imread("C:\\Users\\Pedro\\Desktop\\OpenCv\\Transformacoes_geomotricas\\einstein.jpg", 0)
totalLinhas, totalColunas = imgOrigin.shape[:2]


matriz = np.float32([[1,0,100],[0,1,200]])
imgDeslocada = cv.warpAffine(imgOrigin, matriz, (totalColunas, totalLinhas))

cv.imshow("Imagem Deslocada", imgDeslocada)
cv.waitKey(0)
cv.destroyAllWindows()
