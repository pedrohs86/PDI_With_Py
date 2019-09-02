import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("C:\\Users\\Pedro\\Desktop\\OpenCv\\Equalizacao\\einstein.jpg", 0)

imgEqual = cv.equalizeHist(img)

cv.imshow("Imagem Original", img)   
cv.imshow("Imagem Equalizada", imgEqual)

plt.hist(img.ravel(), 256, [0,256])
plt.figure()
plt.hist(imgEqual.ravel(), 256, [0,256])
plt.show()