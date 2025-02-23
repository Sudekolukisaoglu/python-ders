import cv2, numpy as np

video = cv2.VideoCapture(0)

while video.isOpened():
    aa, alınanGoruntu = video.read()
    print(alınanGoruntu)
    yenisi = np.array_split(alınanGoruntu, 2)
    dparça1 = np.hsplit(yenisi[0],2)
    dparça2 = np.hsplit(yenisi[1],2)
    # cv2.imshow("Alınan goruntu1:",yenisi[0])
    # cv2.imshow("Alınan goruntu2:",yenisi[1])
    # cv2.imshow("Alınan goruntu3:",yenisi[2])
    # cv2.imshow("Alınan goruntu4:",yenisi[3])
    birlesik = np.concatenate((dparça1[0],dparça2[1],dparça2[0]), axis=1)
    cv2.imshow("Alınan goruntu1:",birlesik)

    tus = cv2.waitKey(1)

    if tus == 97  or tus == ord('q'): break
video.release()
cv2.destroyAllWindows()