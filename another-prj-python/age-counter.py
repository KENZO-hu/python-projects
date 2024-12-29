import cv2
import numpy as np

# Chemins vers les modèles
age_model_path = "deploy_age.prototxt"
age_weights_path = "age_net.caffemodel"
face_model_path = "deploy.prototxt"
face_weights_path = "res10_300x300_ssd_iter_140000.caffemodel"

# Vérification de l'existence des fichiers
import os
if not all(os.path.exists(f) for f in [age_model_path, age_weights_path, face_model_path, face_weights_path]):
    raise FileNotFoundError("Un ou plusieurs fichiers modèles sont manquants ! Assurez-vous qu'ils sont correctement téléchargés.")

# Définir les groupes d'âge
age_groups = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)", "(38-43)", "(48-53)", "(60-100)"]

# Charger les modèles
age_net = cv2.dnn.readNetFromCaffe(age_model_path, age_weights_path)
face_net = cv2.dnn.readNetFromCaffe(face_model_path, face_weights_path)

# Initialiser la webcam
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    raise RuntimeError("Impossible d'ouvrir la webcam. Vérifiez si elle est correctement connectée.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Erreur lors de la capture de la vidéo. Arrêt.")
        break

    # Préparation pour la détection de visage
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
    face_net.setInput(blob)
    detections = face_net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:  # Si la confiance est > 50%
            # Obtenir la boîte englobante
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x_start, y_start, x_end, y_end) = box.astype("int")

            # S'assurer que la boîte est dans les limites
            if x_start < 0 or y_start < 0 or x_end > w or y_end > h:
                continue

            # Extraire le visage
            face = frame[y_start:y_end, x_start:x_end]
            if face.size == 0:  # S'assurer que le visage n'est pas vide
                continue

            # Préparation pour la détection de l'âge
            blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746))
            age_net.setInput(blob)
            age_preds = age_net.forward()
            age_group = age_groups[age_preds[0].argmax()]

            # Afficher la boîte englobante et l'âge estimé
            label = f"Age: {age_group}"
            cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
            cv2.putText(frame, label, (x_start, y_start - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Afficher la sortie
    cv2.imshow("Age Estimation", frame)

    # Sortie en appuyant sur 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
video_capture.release()
cv2.destroyAllWindows()
