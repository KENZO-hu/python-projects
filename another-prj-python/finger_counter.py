import cv2
import mediapipe as mp

# Initialize MediaPipe Hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the BGR frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand landmarks
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

            # Extract landmark positions for finger counting
            landmarks = hand_landmarks.landmark

            # Define finger tip landmarks and corresponding base landmarks
            finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
            finger_bases = [3, 6, 10, 14, 18]

            # Count fingers
            finger_count = 0

            for tip, base in zip(finger_tips, finger_bases):
                if landmarks[tip].y < landmarks[base].y:  # Check if the tip is above the base
                    finger_count += 1

            # For thumb, check horizontal distance
            if landmarks[4].x > landmarks[3].x:  # Adjust logic for thumb orientation
                finger_count += 1

            # Display the number of fingers
            cv2.putText(
                frame, f"Fingers: {finger_count}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2
            )

    # Show the frame
    cv2.imshow("Finger Counter", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
