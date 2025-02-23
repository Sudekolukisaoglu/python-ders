# Dosyadan okuma ve renksizleştirme
import cv2

video = cv2.VideoCapture(0)
while video.isOpened():
 ret, yakalananResim = video.read()
 yeniDizi = np.hsplit(yakalananResim,2)

if ret == True:
    cv2.imshow('Parca1',yeniDizi[0])
    yeniDizi[1] = cv2.cvtColor(yeniDizi[1],cv2.COLOR_BGR2GRAY)
    cv2.imshow('Parca2',yeniDizi[1])
    tus = cv2.waitKey(1)
    if tus == ord('q'): break
    else: break
cap.release()
cv2.destroyAllWindows()

