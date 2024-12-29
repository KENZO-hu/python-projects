import face_recognition
import cv2
import numpy as np

# Load the known image and create its face encoding
known_image_path = "user_image.jpg"
known_image = face_recognition.load_image_file(known_image_path)
known_encoding = face_recognition.face_encodings(known_image)[0]  # Assuming only one face in the image

# Store known encodings and their associated names (optional for multi-user support)
known_encodings = [known_encoding]
known_names = ["User"]  # Replace "User" with the person's name or ID
