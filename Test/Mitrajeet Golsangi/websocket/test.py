import cv2

cap = cv2.VideoCapture(1)

while cap.isOpened():
    _, f = cap.read()
    
    cv2.imshow("d", f)
    
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break;

cv2.destroyAllWindows()
cap.release()
