# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# # Load an color image in grayscale
# img = cv2.imread('rasm1.png',0)
# plt.imshow(img)
# plt.show()

# import cv2
# import numpy as np
# img1 = cv2.imread('rasm1.png')
# img2 = cv2.imread('rasm2.png')
# dest1 = cv2.bitwise_and(img2, img1, mask = None)
# dest2 = cv2.bitwise_or(img2, img1, mask = None)
# dest3 = cv2.bitwise_xor(img1, img2, mask = None)
# cv2.imshow('A', img1)
# cv2.imshow('B', img2)
# cv2.imshow('AND', dest1)
# cv2.imshow('OR', dest2)
# cv2.imshow('XOR', dest3)
# cv2.imshow('NOT A', cv2.bitwise_not(img1))
# cv2.imshow('NOT B', cv2.bitwise_not(img2))
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()

# import numpy as np
# import cv2
# img = cv2.imread('rasm2.png',1)
# cv2.line(img,(20,400),(400,20),(255,255,255),3)
# cv2.rectangle(img,(200,100),(400,400),(0,255,0),5)
# cv2.circle(img,(80,80), 55, (255,255,0), -1)
# cv2.ellipse(img, (300,425), (80, 20), 5, 0, 360, (0,0,255), -1)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def rasm
