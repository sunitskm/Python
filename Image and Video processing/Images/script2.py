import cv2
import os
list_files = os.listdir()
print(list_files)
for f in list_files:
    if(f[-3:].lower() == 'jpg'):
        s = f[:-3]+"_resized.jpg"
        img = cv2.imread(f,1)
        resized_image = cv2.resize(img,(100,100))
        cv2.imwrite(s,resized_image)
