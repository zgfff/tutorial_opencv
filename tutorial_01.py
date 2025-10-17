import cv2

img = cv2.imread('image_1.jpg')

# print(type(img))
# print(img.shape)
# print(img.dtype)
# print(img.min())
# print(img.max())

# print(img[2159,100])

#loop over the image,pixel by pixel
# for y in range(0, img.shape[0]):
#   for x in range(0, img.shape[1]):
#     print(img[y,x])

cv2.imshow('image_1.jpg', img)
#print(img.shape)
cv2.waitKey(0)

# convert to gray scale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(grayImg.shape)
cv2.imshow('gray_image', grayImg)
cv2.waitKey(0)

# resize image
resized_img = cv2.resize(img, None , fx=0.4, fy=0.4)
cv2.imshow('resize_image', resized_img)
cv2.waitKey(0)

# crop image img[y1:y2, x1:x2] y = rows (top to botton), x = columns(Left to right)
cropped_image = img[0:1000, 90:300]
cv2.imshow('Cropped_image', cropped_image)
cv2.waitKey(0)

