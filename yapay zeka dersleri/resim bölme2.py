import cv2, numpy as np
img =cv2.imread("resimler/sincap.webp")
print(img)
cv2.imshow('deneme',img)
newarr = np.array_split(img, 4)
print("\nBölünmedeki parçaları alma")
cv2.imshow("1.parça :",newarr[0])
cv2.imshow("2.parça :",newarr[1])
cv2.imshow("3.parça :",newarr[2])
cv2.imshow("4.parça :",newarr[3])


cv2.waitKey(0) # 3 saniye bekle
cv2.destroyAllWindows