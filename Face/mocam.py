import cv2
import os
cap = cv2.VideoCapture(0)

while True:
     _, image=cap.read()
     cv2.imshow('image', image)

     if cv2.waitKey(1) & 0xFF == ord('q'):
         break