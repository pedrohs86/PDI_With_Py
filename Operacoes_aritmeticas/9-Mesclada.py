import cv2 as cv

img1 = cv.imread('C:\\Users\\Pedro\\Desktop\\OpenCv\\Operacoes_aritmeticas\\Superman.png')
img2 = cv.imread('C:\\Users\\Pedro\\Desktop\\OpenCv\\Operacoes_aritmeticas\\batman.png')

imgTotal = cv.addWeighted(img1, 0.8, img2, 1.0, 0)

cv.imshow("Imagem Subtraida", img1)
cv.waitKey(0)
cv.imshow("Imagem Subtraida", img2)
cv.waitKey(0)
cv.imshow("Imagem Mesclada", imgTotal)
cv.waitKey(0)
cv.destroyAllWindows()
