import cv2
import numpy as np

# aşağıdaki [255,255,255] rakamlarını oynayarak ne olduğuna bakın
r1 = np.full((50, 170, 3), [255, 0, 255], dtype=np.uint8)
r2 = np.full((50, 170, 3), [0, 250, 0], dtype=np.uint8)

print(r1)

cv2.imshow("Olusan resim", r1)
cv2.imshow("Olusan resim2", r2)

birlesik = cv2.vconcat([r1, r2])
cv2.imshow("Olusan resim3", birlesik)

cevrilmis = cv2.rotate(birlesik, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Olusan resim4", cevrilmis)

cv2.waitKey(0)

cv2.destroyAllWindows()
