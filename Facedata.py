import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

face_detrctor= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


face_id = input("Enter face id : ")
print(face_id)
count = 0
while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detrctor.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:

       cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
       count += 1
       cv2.imwrite("dataset/User."+str(face_id)+'.' + str(count)+ ".jpg", gray[y:y+h,x:x+w])
       cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif count >=30:
        break
print('\n Out')
cam.release()
cv2.destroyAllWindows()



