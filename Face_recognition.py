import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
id=0
names=['NHut','TOAN','Phat','3','4','5','6','7','8','9']
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
        scaleFactor=1.7,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )
    for (x, y, w, h) in faces:
     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
     id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
     if (confidence < 100):
        id=names[id]
        confidence=" {0}%".format(round(100-confidence))
     else:
        id='unknow'
        confidence="{0}%".format(round(100-confidence))
     cv2.putText(img, str(id), (x,y-5), font, 1, (255,255,255), 2)
     cv2.putText(img, str(confidence), (x,y-5), font, 1, (255,255,255), 2)
    cv2.imshow('img', img)
    k=cv2.waitKey(10) & 0xFF
    if k==27:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()



