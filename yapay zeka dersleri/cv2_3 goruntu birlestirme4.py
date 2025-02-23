import cv2, numpy as np

video = cv2.VideoCapture(0)

while video.isOpened():
    aa, alınanGoruntu = video.read()
    yeniDizi = np.hsplit(alınanGoruntu, 2)

    yukseklik, genıslık, renk = yeniDizi[1].shape

    yeniResim =np.full((yukseklik,genıslık, 3),(150,200,200), dtype=np.uint8)
    yeniDizi[1] = np.add(yeniDizi[1],yeniResim)
    gosterilecekSekli =np.concatenate((yeniDizi[0],yeniResim,yeniDizi[1]),axis=1) 

    cv2.imshow("Alınan goruntu1:",gosterilecekSekli)
    tus = cv2.waitKey(1)

    if tus == 97  or tus == ord('q'): break
video.release()
cv2.destroyAllWindows()