import websockets
import asyncio

import mediapipe as mp
import cv2, struct, pickle, base64

import numpy as np

port = 5000

print("Started server on port : ", port)

async def transmit(websocket, path):
    print("Client Connected !")
    try :
        frame = cv2.imread('./face_op.jpg', -1)
        
        encoded = cv2.imencode('.jpg', frame)[1]

        data = str(base64.b64encode(encoded))
        data = data[2:len(data)-1]

        await websocket.send(data)        
    except websockets.connection.ConnectionClosed as e:
        print("Client Disconnected !")
    # except:
    #     print("Someting went Wrong !")
start_server = websockets.serve(transmit, port=port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
