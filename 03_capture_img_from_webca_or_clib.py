import cv2

cap = cv2.VideoCapture(0)

frame_count = 0

cv2.namedWindow('RGB_image', cv2.WINDOW_NORMAL)

while cap.isOpened():
    ret, frame = cap.read()
    