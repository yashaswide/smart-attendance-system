import cv2
import os
import numpy as np

faces=[]
labels=[]

label_map={}
label_id=0

dataset="dataset"

for person in os.listdir(dataset):

    label_map[label_id]=person

    person_path=os.path.join(
        dataset,
        person
    )

    for person in os.listdir(dataset):
        person_path = os.path.join(
            dataset,
            person
    )

    if not os.path.isdir(person_path):
        continue

    label_map[label_id] = person

    for img in os.listdir(person_path):

        path = os.path.join(
            person_path,
            img
        )

        gray = cv2.imread(path,0)

        if gray is not None:
            faces.append(gray)
            labels.append(label_id)

    label_id += 1

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(
    faces,
    np.array(labels)
)

recognizer.save("trainer.yml")

print("Model trained successfully")