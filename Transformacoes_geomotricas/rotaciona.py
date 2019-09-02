# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

imgOrigin = cv.imread("C:\\Users\\Pedro\\Desktop\\OpenCv\\Transformacoes_geomotricas\\einstein.jpg", 0)
totalL, totalC = imgOrigin.shape

# Função que rotaciona a matriz da imagem (centro, angulo, escala)

mat = cv.getRotationMatrix2D((totalC/2, totalL/2), 45,1)

imgRota = cv.warpAffine(imgOrigin, mat, (totalC, totalL))

cv.imshow("Imagem rotacionada 45", imgRota)
cv.waitKey(0)
cv.destroyAllWindows()