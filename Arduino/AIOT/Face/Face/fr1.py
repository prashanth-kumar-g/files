import face_recognition
from cvzone.SerialModule import SerialObject
from time import sleep
import numpy as np
import cv2
import sys
import telepot
bot = telepot.Bot(token="8516134409:AAH7cbhJ816w9osZlIsE9Jq-TyV0t16ckFw")
chat_id=5102989677
#arduino = SerialObject("COM3")
video_capture = cv2.VideoCapture(0)

def load_and_encode(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        print(f"{image_path} not found")
        sys.exit()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = np.ascontiguousarray(image, dtype=np.uint8)

    encodings = face_recognition.face_encodings(image)
    if len(encodings) == 0:
        print(f"No face found in {image_path}")
        sys.exit()

    return encodings[0]

Manju_face_encoding  = load_and_encode("Photo/Manju.jpeg")
Manju1_face_encoding = load_and_encode("Photo/Manju1.jpeg")
Prash_face_encoding  = load_and_encode("Photo/Prash.jpg")
Prash1_face_encoding = load_and_encode("Photo/Prash1.jpg")

known_face_encodings = [Manju_face_encoding,Manju1_face_encoding,Prash_face_encoding,Prash1_face_encoding]
known_face_names = ["Dr. Manjunath", "Dr. Manjunath", "Prashanth Kumar G", "Prashanth Kumar G"]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
#arduino.sendData([0])

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if face_distances[best_match_index] < 0.25:
                name = known_face_names[best_match_index]
            else:
                name = "Unknown"

            face_names.append(name)
            if name=="Unknown":
                #arduino.sendData([0])
                bot.sendMessage(chat_id=chat_id, text="Attention!!!, Some one in the Room")
            else:
                #arduino.sendData([1])
                cv2.waitKey(10)

               

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
