import cv2
from playsound import playsound

# Load OpenCV's pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start webcam
cap = cv2.VideoCapture(0)

doorbell_rang = False
no_face_counter = 0
face_leave_threshold = 15  # number of frames without face to reset

print("[INFO] Smart Doorbell is running... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) > 0:
        no_face_counter = 0
        if not doorbell_rang:
            print("[INFO] Face detected! Ringing doorbell...")
            playsound("Smart Doorbell\doorbell-223669.mp3")  # Make sure doorbell.mp3 is in the same folder
            doorbell_rang = True
    else:
        no_face_counter += 1
        if no_face_counter > face_leave_threshold:
            doorbell_rang = False

    # Optional: Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show video feed
    cv2.imshow("Smart Doorbell", frame)

    # Quit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
