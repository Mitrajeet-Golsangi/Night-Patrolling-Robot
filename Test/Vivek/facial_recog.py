#importing open cv 
import cv2
from random import randrange as r

#dataset load
# trainedDataset = cv2.CascadeClassifier(r'D:/VIT Projects/Second Year/2nd Semester/EDI/Test/Vivek/face.xml')
# trainedDataset = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

#* Best till now
trainedDataset = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt_tree.xml')


# Starting webcam
webcam = cv2.VideoCapture(0)
while webcam.isOpened():

  success, img = webcam.read()

  #Converting to black and white(grayscale)
  #BGR-BLUE-GREEN-RED
  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # #detecting faces in the image
  face_coordinates = trainedDataset.detectMultiScale(gray_img)
  data = trainedDataset.detectMultiScale3(gray_img, outputRejectLevels = True)
  for  x,y,w,h in face_coordinates:
    cv2.rectangle(
      img, 
      (x, y),
      (x + w, y + h),
      (r(0, 255), r(0, 255), r(0, 255)), 2
    )
    try : 
      cv2.putText(
        img,
        '{0:.2}'.format(data[2][0]),
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 0, 255),
        2
      )
    except IndexError:
      pass
   
  #Displaying the image 
  cv2.imshow('Window',img)
  
  key = cv2.waitKey(1) & 0xFF

  if(key==27):
      break

webcam.release()
