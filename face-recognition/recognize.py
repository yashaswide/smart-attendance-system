import cv2

label_map = {
    0:"YASHASWI DE"
}

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

face_cascade=cv2.CascadeClassifier(
    cv2.data.haarcascades+
    "haarcascade_frontalface_default.xml"
)

cam=cv2.VideoCapture(0)

while True:

    ret,frame=cam.read()

    gray=cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces=face_cascade.detectMultiScale(
        gray,
        1.3,
        5
    )

    for (x,y,w,h) in faces:

        id_, confidence = recognizer.predict(
            gray[y:y+h,x:x+w]
        )

        name=label_map.get(
            id_,
            "Unknown"
        )

        print(
            f"{name} recognized"
        )

        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (255,0,0),
            2
        )

        cv2.putText(
            frame,
            name,
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,0,0),
            2
        )

    cv2.imshow(
        "Attendance System",
        frame
    )

    if cv2.waitKey(1)==27:
        break


cam.release()
cv2.destroyAllWindows()