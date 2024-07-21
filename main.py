import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#XML file containing the pre trained model to detect frontal faces
def detect_faces(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert color to grayscale as face detection is better in grayscale
    faces=face_classifier.detectMultiScale(gray, 1.3, 5) #open notion file to understand more
    if len(faces)==0:
        return img
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # 255,0,0 is blue and 2 is thickness, baaki the variables means top left and bottom right
    return img

cap=cv2.VideoCapture(0)  #open the default (0 as in first camera) camera

while True:
    ret, frame=cap.read()  #ret is boolean to check if a frame is received or no
    frame=detect_faces(frame)

    cv2.imshow('Video face detection', frame) #shows the result in a vid titles Video face detection

    if cv2.waitKey(1) & 0xFF == ord('q'):  #waits for 1 millisecond to check if q is pressed or no
        break

cap.release()   #releases the camera
cv2.destroyAllWindows()  #close all openCV windows
