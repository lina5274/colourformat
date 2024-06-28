import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/photo.png')
black_bg = np.zeros_like(img, dtype='uint8')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5),8)
img = cv2.Canny(img, 20, 30)
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
upper_contours = []
middle_contours = []
lower_contours = []
for contour in con:
    x, y, w, h = cv2.boundingRect(contour)
    if y < img.shape[0] / 3.5:
        upper_contours.append(contour)
    elif y < 2 * img.shape[0] / 3.5:
        middle_contours.append(contour)
    else:
        lower_contours.append(contour)

cv2.drawContours(black_bg, upper_contours, -1, (0, 255, 0))
cv2.drawContours(black_bg, middle_contours, -1, (0, 0, 255))
cv2.drawContours(black_bg, lower_contours, -1, (255, 0, 255))
cv2.imshow('photo.png', black_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.figure(figsize=(10, 10))
plt.imshow(black_bg_rgb)
plt.title('photo.png')
plt.axis('off')
plt.show()
print(img.shape)
