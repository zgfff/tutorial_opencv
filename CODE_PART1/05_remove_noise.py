import cv2
import numpy as np

img = cv2.imread(r'F:\project_inewgen\elephent_hackathon\image_1.jpg')

height, width = img.shape[:2]

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#remove noise using medin filter
m_blurred = cv2.medianBlur(img,7)
cv2.imshow('Blur_img_using_median_filter', m_blurred)

#remove noise using gaussian filter
g_blurred = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('Blur_img_using_gaussian_filter', g_blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()