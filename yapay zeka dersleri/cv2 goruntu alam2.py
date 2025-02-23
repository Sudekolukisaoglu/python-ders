import cv2, numpy as np

video = cv2.VideoCapture(0)

while video.isOpened():
    aa, bb = video.read()
    print(bb)
    yenisi = np.array_split(bb, 4)
    cv2.imshow("Alınan goruntu1:",yenisi[0])
    cv2.imshow("Alınan goruntu2:",yenisi[1])
    cv2.imshow("Alınan goruntu3:",yenisi[2])
    cv2.imshow("Alınan goruntu4:",yenisi[3])

    tus = cv2.waitKey(1)

    if tus == 97  or tus == ord('q'): break
video.release()
cv2.destroyAllWindows()