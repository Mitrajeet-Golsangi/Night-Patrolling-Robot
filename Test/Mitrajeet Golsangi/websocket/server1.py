import websockets
import asyncio

import mediapipe as mp
import cv2, struct, pickle, base64

import numpy as np

mp_face_detection = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.7)

port = 5000

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

print("Started server on port : ", port)

async def transmit(websocket, path):
    print("Client Connected !")
    try :
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            _, frame = cap.read()
            
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            res = face_detection.process(rgb)
            
            if res.detections:
                draw_bbox(res, frame)
            
            encoded = cv2.imencode('.jpg', frame)[1]

            data = str(base64.b64encode(encoded))
            data = data[2:len(data)-1]
            
            await websocket.send(data)
            
            # cv2.imshow("Transimission", frame)
            
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
        
    except websockets.connection.ConnectionClosed as e:
        print("Client Disconnected !")
        cap.release()
    # except:
    #     print("Someting went Wrong !")
start_server = websockets.serve(transmit, port=port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

cap.release()