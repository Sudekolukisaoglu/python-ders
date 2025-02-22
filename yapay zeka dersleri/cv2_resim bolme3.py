# pip install opencv-python
# https://www.tamindir.com/indir/paintnet/
# Resim açma
import cv2, numpy as np
# img = cv2.imread('resimler/squirrel1.jpg')
resim = cv2.imread('resimler/sincap.webp')
print(resim)
# cv2.imshow('Deneme',resim)
# newarr = np.array_split(img, 3)
# yenidizi = np.hsplit(resim, 3)
# yenidizi = resim[:200:]
# cv2.imshow('Parca',yenidizi)
# yenidizi2 = resim[200::]
# cv2.imshow('Parca2',yenidizi2)
yenidizi3 = resim[::10]
cv2.imshow('Parca3',yenidizi3)



# cv2.imwrite('squirrel4.bmp',img)
cv2.waitKey(0) # tuşa basılana kadar bekle
cv2.destroyAllWindows() # pencereleri kapa

