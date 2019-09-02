import cv2 as cv
import numpy as np

imgOriginal = cv.imread("C:\\Users\\Pedro\\Desktop\\OpenCv\\Transformacoes_geomotricas\\einstein.jpg", 0)

imgReduzida = cv.resize(imgOriginal, None, fx = 0.5, fy = 0.5, interpolation = cv.INTER_CUBIC)
imgAmpliada = cv.resize(imgOriginal, None, fx = 2, fy = 2, interpolation = cv.INTER_CUBIC)

cv.imshow("Imagem Original", imgOriginal)
cv.imshow("Imagem Reduzida", imgReduzida)
cv.imshow("Imagem Ampliada", imgAmpliada)
cv.waitKey(0)
cv.destroyAllWindows()
