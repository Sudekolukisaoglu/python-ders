import cv2, numpy as np

video = cv2.VideoCapture(0)

while video.isOpened():
    aa, bb = video.read()
    print(bb)
    yenisi = np.array_split(bb, 2)
    cv2.imshow("Alınan goruntu1:",yenisi[0])
    cv2.imshow("Alınan goruntu2:",yenisi[1])

    tus = cv2.waitKey(0)

    if tus == 97 : break
video.release()
cv2.destroyAllWindows()