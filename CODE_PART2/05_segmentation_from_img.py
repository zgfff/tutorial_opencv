import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO('yolo11n-seg.pt')

# read image
img = cv2.imread(r'F:\project_inewgen\elephent_hackathon\CODE_PART2\photo.webp',cv2.COLOR_RGB2BGR)
res = model.predict(img)

# iterate detection results
for r in res:
  # iterate each object contour
  for c in (r):
    
    label = c.names[c.boxes.cls.tolist().pop()]
    print('label: ', label)

    # create binary mask
    b_mask = np.zeros(img.shape[:2], np.uint8)

    # create binary mask
    contour = c.masks.xy.pop().astype(np.int32).reshape(-1, 1, 2)
    cv2.drawContours(b_mask, [contour], -1, (255, 255 ,255), cv2.FILLED)
    #cv2.drawContours(img, [contour], 0, (0, 0, 255), 3) #draw an contour line

    # Isolate object with black background
    mask3ch = cv2.cvtColor(b_mask, cv2.COLOR_GRAY2BGR)
    isolated = cv2.bitwise_and(mask3ch, img)

    # detection crop
    x1, y1, x2, y2 = c.boxes.xyxy.cpu().numpy().squeeze().astype(np.int32)
    iso_crop = isolated[y1:y2, x1:x2]

    # TODO your actions go here
    #cv2.imshow('img', img)
    cv2.imshow('resoult segmentation', isolated)
    cv2.waitKey(0)
