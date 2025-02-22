#  Video açma
import cv2,numpy as np
 
cap = cv2.VideoCapture('videos/wildlife.mp4')


while cap.isOpened():
    ret, frame = cap.read()
    newarr = np.array_split(frame, 3)
    print("\nBölünmedeki parçaları alma")
    cv2.imshow("1.parça :",newarr[0])
    cv2.imshow("2.parça :",newarr[1])
    cv2.imshow("3.parça :",newarr[2])
    if ret == True:
        cv2.imshow('frame',frame)
        tus = cv2.waitKey(1)
        if tus == ord('q'): break
    else: break
cap.release()
cv2.destroyAllWindows()
