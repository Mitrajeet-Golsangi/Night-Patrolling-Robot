import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, f = cap.read()
    
    cv2.imshow("t", f)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
