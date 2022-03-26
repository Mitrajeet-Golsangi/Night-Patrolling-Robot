import cv2, socket, pickle, struct
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.7)

def draw_bbox(res, frame):
    for id, det in enumerate(res.detections):
        # mp_draw.draw_detection(frame, det)  #? Direct Method for drawing bounding box and feature points

        coord = det.location_data.relative_bounding_box
        ih, iw, ic = frame.shape
        
        bbox =  int(coord.xmin * iw), int(coord.ymin * ih), \
                int(coord.width * iw), int(coord.height * ih)
        
        cv2.rectangle(frame, bbox, (255, 0, 255), 2)
        cv2.putText(
            frame,
            f'{int(det.score[0]*100)}%',
            (bbox[0], bbox[1] - 20),
            cv2.FONT_HERSHEY_PLAIN,
            2,
            (0, 255, 0),
            2
        )

# create socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip  = socket.gethostname()
port = 5000
print(host_ip, port)

client_socket.connect((host_ip, port))

data = b""
payload_size = struct.calcsize("Q")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(8*1024)
        
        if not packet: break
        data += packet
    
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    
    msg_size = struct.unpack("Q", packed_msg_size)[0]
    
    while len(data) < msg_size:
        data += client_socket.recv(8*1024)
    
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
    res = face_detection.process(rgb)
    
    if res.detections:
        draw_bbox(res, frame)
    
    cv2.imshow("Received", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

client_socket.close()