import cv2
img = cv2.imread('mugla.jpg')
cv2.imshow('başlık',img)
cv2.waitKey(3000)
cv2.destroyAllWindows()