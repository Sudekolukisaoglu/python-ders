# Video açma
import cv2

video = cv2.VideoCapture('videos/wildlife.mp4')

while video.isOpened():
    ret, yakalananResim = video.read()
    print(yakalananResim)
    yakalananResim[10,10]=[0,0,255]
    yakalananResim[10,11]=[0,0,255]
    yakalananResim[10,12]=[0,0,255]
    yakalananResim[11,10]=[0,0,255]
    yakalananResim[11,11]=[0,0,255]
    yakalananResim[11,12]=[0,0,255]
    yakalananResim[12,10]=[0,0,255]
    yakalananResim[12,11]=[0,0,255]
    yakalananResim[12,12]=[0,0,255]

    
    # cv2.waitKey(0)
    if ret == True:
        cv2.imshow('yakalananResim',yakalananResim)
        tus = cv2.waitKey(1)
        if tus == ord('q'): break
    else: break
video.release()
cv2.destroyAllWindows()