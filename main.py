import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=5.5, minNeighbors=1)

    for (x, y, w, h) in faces:
        # Step A: slice out the face region from the COLOR frame (not gray!)
        face_region = frame[y:y+h, x:x+w]

        # Step B: blur that slice
        blurred_face = cv2.blur(face_region, (15, 15), 0)

        # Step C: put the blurred slice back into the frame
        frame[y:y+h, x:x+w] = blurred_face

    cv2.imshow("Anonymized", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()