import cv2

#cap = cv2.VideoCapture(0) # use 0 for webcam
cap = cv2.VideoCapture(r'F:\project_inewgen\elephent_hackathon\3 data sampling\3 data sampling\น้ำฝน.MP4')

frame_count = 0

cv2.namedWindow('RGB_image', cv2.WINDOW_NORMAL)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, None, fx=1.0, fy=1.0)
        frame_count += 1
        print(f"Frame count: {frame_count}")

        cv2.putText(frame, str(int(frame_count)), (7,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 2)
        cv2.imshow('RGB_image', frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    
    else:
        print("Failed to capture image")
        break

cap.release()
cv2.destroyAllWindows()