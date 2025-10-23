import cv2
from ultralytics import YOLO

model = YOLO('yolo11s.pt')

# read image
img = cv2.imread(r'F:\project_inewgen\elephent_hackathon\CODE_PART2\photo.webp')
source = img

#print model names
print(model.names)

#predict objects in image
results = model.predict(source, conf=0.45)

detected_frame = results[0].plot()

cv2.namedWindow('detected frame', cv2.WINDOW_NORMAL)
cv2.imshow('detected frame', detected_frame)
cv2.waitKey(0)
