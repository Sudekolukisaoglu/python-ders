import cv2, numpy as np

video = cv2.VideoCapture(0)

while video.isOpened():
    aa, alınanGoruntu = video.read()
    # print(alınanGoruntu)
    yeniDizi = np.hsplit(alınanGoruntu, 4)

    yukseklik, genıslık, renk = yeniDizi[1].shape

    yeniResim =np.full((yukseklik,genıslık, 3),(45,45,45), dtype=np.uint8)
    yeniDizi[2] = np.add(yeniDizi[2],yeniResim)
    gosterilecekSekli =np.concatenate((yeniDizi[0],yeniResim,yeniDizi[2]),axis=1) 

    # print(f'Yükseklik:{yukseklik}, Genişlik:{genıslık}, renk: [renk]')
    # yenisi = np.array_split(alınanGoruntu, 2)
    # dparça1 = np.hsplit(yenisi[0],2)
    # dparça2 = np.hsplit(yenisi[1],2)

    # birlesik = np.concatenate((dparça1[0],dparça2[1],dparça2[0]), axis=1)
    # # cv2.imshow("Alınan goruntu1:",birlesik)
    cv2.imshow("Alınan goruntu1:",gosterilecekSekli)
    tus = cv2.waitKey(1)

    if tus == 97  or tus == ord('q'): break
video.release()
cv2.destroyAllWindows()