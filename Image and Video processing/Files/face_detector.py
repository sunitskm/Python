import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("news.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.05,minNeighbors = 10)
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
print(type(faces))
print(faces)
resized = cv2.resize(img,(img.shape[1],img.shape[0]))
cv2.imshow("Grey",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
