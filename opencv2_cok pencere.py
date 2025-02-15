import cv2 #openCV renk sıralması blue , green , red
import numpy as np

# aşağıdaki [255, 255, 255] rakamlarını oynayarak ne olduğuna bakın
r1= np.full((200, 150, 3), [25, 150, 150], dtype=np.uint8)
r2= np.full((200, 150, 3), [50, 50, 50], dtype=np.uint8)

cv2.imshow("Olusan resim1", r1)
cv2.imshow("Olusan resim2", r2)

cv2.waitKey(0)
 
cv2.destroyAllWindows()