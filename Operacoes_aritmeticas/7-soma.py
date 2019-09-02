
import cv2 as cv

img1 = cv.imread('C:\\Users\\Pedro\\Desktop\\OpenCv\\Operacoes_aritmeticas\\Superman.png')
img2 = cv.imread('C:\\Users\\Pedro\\Desktop\\OpenCv\\Operacoes_aritmeticas\\batman.png')

imgSomada = cv.add(img1, img2)

cv.imshow("Imagem Somada", imgSomada)
cv.waitKey(0)
cv.destroyAllwindows()
