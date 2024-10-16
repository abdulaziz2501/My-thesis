import numpy as np
import cv2
import matplotlib.pyplot as plt
# Load an color image in grayscale
img = cv2.imread('rasm1.png',0)
plt.imshow(img)
plt.show()