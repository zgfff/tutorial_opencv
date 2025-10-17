import cv2

img = cv2.imread('image_1.jpg')
cv2.imshow('image', img)

# convert to gray scale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_image', grayImg)

# resize image
resized_img = cv2.resize(img, None , fx=0.4, fy=0.4)
cv2.imshow('resize_image', resized_img)

# crop image img[y1:y2, x1:x2] y = rows (top to botton), x = columns(Left to right)
cropped_image = img[0:1000, 90:300]
cv2.imshow('Cropped_image', cropped_image)

# draw rectangle on image
x0, y0, x1, y1 = 80, 90, 300, 300
thickness = 5
rect_img = cv2.rectangle(img, (x0, y0), (x1, y1), color=(0, 0, 0), thickness= thickness)
cv2.imshow('Draw_rectangle_on_image', rect_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
