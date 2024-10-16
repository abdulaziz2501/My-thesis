import numpy as np
import cv2
# Load a color image in grayscale
img = cv2.imread('/pictures/rasm1.png',1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()