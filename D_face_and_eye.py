# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:54:32 2020

@author: Arivazhagan G
"""
#importing libraries
import cv2

#casecade classifier for face
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")

video_capture=cv2.VideoCapture(0)
video_capture.set(4,680)
video_capture.set(4,780)

a=0
print("Camera loading look to the camera")
#find the face and eye
while True:
    a=a+1
    check,frame=video_capture.read()
    grey_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey_img,scaleFactor=1.05,minNeighbors=5)
    print(type(faces))
    print(faces)
    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        eyes=eye_cascade.detectMultiScale(grey_img,scaleFactor=1.05,minNeighbors=10)
        
        for ex,ey,ew,eh in eyes:
            frame=cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)
		    
    cv2.imshow("capture",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):#press q to terminate the program
        break
    
print(a)
video_capture.release()
cv2.destroyAllWindows()#destroy the all Winodows