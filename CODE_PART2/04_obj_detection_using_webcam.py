import cv2
from ultralytics import YOLO

model = YOLO('yolo11s.pt')

cap = cv2.VideoCapture(r'F:\project_inewgen\elephent_hackathon\3 data sampling\น้ำฝน.MP4')

frame_count = 0

cv2.namedWindow('detected frame', cv2.WINDOW_NORMAL)

while cap.isOpened():

  ret, frame = cap.read()

  if ret:

    frame = cv2.resize(frame, None, fx=1.0, fy=1.0)

    frame_count += 1

    #predict objects in image
    conf = 0.45
    results = model.predict(frame, conf= conf)

    detected_frame = results[0].plot()
    cv2.imshow('detected frame', detected_frame)

    print(f"Frame count: {frame_count}")

    #put frame count on the image and display the image in a new window
    cv2.putText(frame, str(int(frame_count)), (7,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 2)
    cv2.imshow('RGB_image', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  else:
    print("Failed to capture image")
    break

cap.release()
cv2.destroyAllWindows()