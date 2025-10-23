import cv2
from datetime import datetime

# save image on webcam or video clip

cap = cv2.VideoCapture(r'F:\project_inewgen\elephent_hackathon\3 data sampling\3 data sampling\น้ำฝน.MP4')

frame_count = 0
img_path = "./elephant_img/"
today = datetime.now().strftime("%d-%m-%Y")

cv2.namedWindow('RGB_image', cv2.WINDOW_NORMAL)

while cap.isOpened():

  ret, frame = cap.read()

  if ret:
    
    frame = cv2.resize(frame, None, fx=1.0, fy=1.0)
    
    frame_count += 1

    #wite image auto save
    # file_name = img_path + f"img_{today}_frame_" + str(frame_count) + ".png"
    # cv2.imwrite(file_name, frame)

    print(f"Frame count: {frame_count}")

    #put frame count on the image and display the image in a new window
    cv2.putText(frame, str(int(frame_count)), (7,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 2)
    cv2.imshow('RGB_image', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
      #write image
      file_name = img_path + f"img_{today}_frame_" + str(frame_count) + ".png"
      cv2.imwrite(file_name, frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  else:
    print("Failed to capture image")
    break

cap.release()
cv2.destroyAllWindows()
