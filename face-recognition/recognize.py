import face_recognition
import os

known_encodings=[]
known_names=[]

dataset="dataset"

for person in os.listdir(dataset):
    person_folder=os.path.join(dataset, person)

    for image_name in os.listdir(person_folder):
        img_path=os.path.join(person_folder,image_name)

        image=face_recognition.load_image_file(img_path)
        encoding=face_recognition.face_encodings(image)[0]

        known_encodings.append(encoding)
        known_names.append(person)

print("Training loaded successfully")

import cv2
import face_recognition

video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()

    rgb=frame[:,:,::-1]

    locations=face_recognition.face_locations(rgb)
    encodings=face_recognition.face_encodings(rgb,locations)

    for face_encoding in encodings:

        matches=face_recognition.compare_faces(
            known_encodings,
            face_encoding
        )

        if True in matches:
            index=matches.index(True)
            print("Recognized:",known_names[index])

    cv2.imshow("Attendance",frame)

    if cv2.waitKey(1)==27:
        break
