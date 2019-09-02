import cv2 as cv

img1 = cv.imread('C:\\Users\\Pedro\\Desktop\\OpenCv\\Operacoes_aritmeticas\\Superman.png')
img2 = cv.imread('C:\\Users\\Pedro\\Desktop\\OpenCv\\Operacoes_aritmeticas\\batman.png')

imgSub = cv.subtract(img1, img2)

cv.imshow("Imagem Subtraida", img1)
cv.waitKey(0)
cv.imshow("Imagem Subtraida", img2)
cv.waitKey(0)
cv.imshow("Imagem Subtraida", imgSub)
cv.waitKey(0)
cv.destroyAllWindows()