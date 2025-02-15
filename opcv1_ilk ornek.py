import cv2 #openCV renk sıralması blue , green , red
import numpy as np

# aşağıdaki [255, 255, 255] rakamlarını oynayarak ne olduğuna bakın
r= np.full((200, 150, 3), [25, 150, 150], dtype=np.uint8)

cv2.imshow("Olusan resim1", r)

cv2.waitKey(0)
 
cv2.destroyAllWindows()
