import cv2
import pygame
import time

data = cv2.CascadeClassifier('half body.xml')
data2 = cv2.CascadeClassifier('full body.xml')
webcam = cv2.VideoCapture(0)


while True:
  succsesful, frame = webcam.read()
  
  greyimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  faces = data.detectMultiScale(greyimg)
  
  if len(faces) > 0.5:
    pygame.mixer.init() #Initialzing pyamge mixer
    pygame.mixer.music.load('music.mp3') #Loading Music File\
    pygame.mixer.music.play(1)
    print("started")

  else:
   pygame.mixer.init() #Initialzing pyamge mixer
   pygame.mixer.music.load('music.mp3') #Loading Music File\
   pygame.mixer.stop()
   print("stoped")


  
  for(x, y, w, h) in faces:
   cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2) 

  cv2.imshow("rask",frame)
  cv2.waitKey(2000)

webcam.release()

cv2.destroyAllWindows()


