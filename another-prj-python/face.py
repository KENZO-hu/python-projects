import cv2
import face_recognition
import os

# Load known faces and names
def load_known_faces(known_faces_dir):
    known_encodings = []
    known_names = []
    for filename in os.listdir(known_faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Load the image and encode it
            image_path = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]

            # Extract name from filename
            name = os.path.splitext(filename)[0]
            known_encodings.append(encoding)
            known_names.append(name)

    return known_encodings, known_names

# Directory containing known faces (add your images here)
known_faces_dir = "known_faces"
known_encodings, known_names = load_known_faces(known_faces_dir)

# Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture a frame
    ret, frame = video_capture.read()
    if not ret:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]  # Convert BGR to RGB

    # Find all face locations and encodings in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Loop through each face found
    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare face with known faces
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        # Use the known face with the smallest distance
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = face_distances.argmin() if len(face_distances) > 0 else None
        if best_match_index is not None and matches[best_match_index]:
            name = known_names[best_match_index]

        # Scale back face locations to original frame size
        top, right, bottom, left = [int(v * 4) for v in face_location]

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Label the face
        cv2.putText(
            frame, name, (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2
        )

    # Display the frame
    cv2.imshow("Face Recognition", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
video_capture.release()
cv2.destroyAllWindows()
