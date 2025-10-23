import cv2
from ultralytics import YOLO

model = YOLO('yolo11s.pt')

# read image
img = cv2.imread(r'F:\project_inewgen\elephent_hackathon\CODE_PART2\photo.webp')
res = img.copy()

#print model names
print(model.names)

#predict objects in image
conf = 0.45
results = model.predict(img, conf= conf)

# detected_frame = results[0].plot()
# cv2.namedWindow('detected frame', cv2.WINDOW_NORMAL)
# cv2.imshow('detected frame', detected_frame)
# cv2.waitKey(0)

boxes = results[0].boxes
objs = boxes.numpy()

obj_list = model.names
if objs.shape[0] != 0:
  for obj in objs:
    detected_obj = obj_list[int(obj.cls[0])]
    print(detected_obj)
    if detected_obj == 'person':
      x0, y0, x1, y1 =obj.xyxy[0].astype(int)
      res = cv2.rectangle(res, (int(x0), int(y0)), (int(x1), int(y1)), (255, 255, 255), 2)
      cv2.imshow('detected frame', res)
      cv2.waitKey(0)
