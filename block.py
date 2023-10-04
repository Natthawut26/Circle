import numpy as np 
import cv2 as cv

imgA = cv.imread('images.jpg', cv.IMREAD_GRAYSCALE) 
imgB = cv.imread('img.jpg', cv.IMREAD_GRAYSCALE)

histB = cv.calcHist([imgB], [0], None, [256], [0, 256])
imgAtoB= cv.equalizeHist(imgA, histB)


cv.imwrite('imgA.png', imgA) 
cv.imwrite('imgB.png', imgB)
cv.imwrite('imgAtoB.png',imgAtoB)
cv.waitKey(0)