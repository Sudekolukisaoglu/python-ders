# Video açma
import cv2,numpy as np

video = cv2.VideoCapture('videos/wildlife.mp4')

while video.isOpened():
    ret, yakalananResim = video.read()
    yeniDizi = np.hsplit(yakalananResim,2)
    # print(yakalananResim)
    # yakalananResim[10,10]=[0,0,255]
    # yakalananResim[10,11]=[0,0,255]
    # yakalananResim[10,12]=[0,0,255]
    # yakalananResim[11,10]=[0,0,255]
    # yakalananResim[11,11]=[0,0,255]
    # yakalananResim[11,12]=[0,0,255]
    # yakalananResim[12,10]=[0,0,255]
    # yakalananResim[12,11]=[0,0,255]
    # yakalananResim[12,12]=[0,0,255]

    
    # cv2.waitKey(0)
    qtus = cv2.waitKey(1)
    if ret == True:
        cv2.imshow('parca1',yeniDizi[0])
        cv2.imshow('parca2',yeniDizi[1])
        if tus == ord('q'): break
    else: break
video.release()
cv2.destroyAllWindows()