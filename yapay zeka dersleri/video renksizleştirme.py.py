# Dosyadan okuma ve renksizleştirme
import cv2,numpy as np

videoDosyasi = cv2.VideoCapture('videos/wildlife.mp4')

if videoDosyasi.isOpened() == False: print("video açılamadı")

while videoDosyasi.isOpened():
    ret, frame = cap.read()
    newarr = np.array_split(frame, 3)
    print("\nBölünmedeki parçaları alma")
    cv2.imshow("1.parça :",newarr[0])
    cv2.imshow("2.parça :",newarr[1])
    cv2.imshow("3.parça :",newarr[2])
    durum, okunan = videoDosyasi.read()
    okunanSB = cv2.cvtColor(okunan, cv2.COLOR_BGR2GRAY)

    if durum == True:
        cv2.imshow('okunan goruntu',okunan)
        cv2.imshow('okunan renksiz',okunanSB)
        tus = cv2.waitKey(20) # 1000/30 = 33
        if tus == ord('q'): exit()
    else: break

videoDosyasi.release()
cv2.destroyAllWindows()

