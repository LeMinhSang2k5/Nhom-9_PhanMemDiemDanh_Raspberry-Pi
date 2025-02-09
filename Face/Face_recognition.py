import cv2
import numpy as np
import pandas as pd
import datetime
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

student_info = {
    1: "Nhut",
    2: "Toan",
    3: "Phat"
}

excel_file = "diem_danh.xlsx"

def ghi_diem_danh(student_id):
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    name = student_info.get(student_id, "Không xác định")

    if os.path.exists(excel_file):
        df = pd.read_excel(excel_file)
    else:
        df = pd.DataFrame(columns=["ID", "Họ tên", "Ngày", "Thời gian"])

    if not ((df["ID"] == student_id) & (df["Ngày"] == date_str)).any():
        new_data = pd.DataFrame([[student_id, name, date_str, time_str]], 
                                columns=["ID", "Họ tên", "Ngày", "Thời gian"])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel(excel_file, index=False)
        print(f"✔ Điểm danh: {name} ({student_id}) lúc {time_str}")
    else:
        print(f"⚠ {name} đã điểm danh hôm nay!")

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        id, confidence = recognizer.predict(face_roi)

        if confidence < 70:
            ghi_diem_danh(id)
            name = student_info.get(id, "Không xác định")
            color = (0, 255, 0)
        else:
            name = "Không nhận diện"
            color = (0, 0, 255)

        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, name, (x, y - 10), font, 0.8, color, 2)

    cv2.imshow("Face Recognition", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


