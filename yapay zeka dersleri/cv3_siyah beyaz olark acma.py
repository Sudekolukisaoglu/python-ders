import cv2
img1 = cv2.imread('resimler/mugla.jpg')
img2 = cv2.imread('resimler/mugla.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('deneme1',img1)
cv2.imshow('deneme2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
