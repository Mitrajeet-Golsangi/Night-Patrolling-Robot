import websockets
import asyncio

import cv2, struct, pickle, base64
import numpy as np
import io

import socket

async def listen():
    url = f'ws://{socket.gethostname()}:5000'
    
    data = b""
    payload_size = struct.calcsize("Q")
    
    async with websockets.connect(url) as ws:
        try:
            while True:
                while len(data) < payload_size:
                    packet = await ws.recv()
                
                    if not packet: break
                    data += packet
                
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                
                msg_size = struct.unpack("Q", packed_msg_size)[0]
                
                while len(data) < msg_size:
                    data += await ws.recv()
                
                frame_data = data[:msg_size]
                data = data[msg_size:]
                frame = pickle.loads(base64.b64decode(frame_data))
                    
                cv2.imshow("Received", frame)            
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except websockets.connection.ConnectionClosed:
            print("Connection Closed !")
        
asyncio.get_event_loop().run_until_complete(listen())

cv2.destroyAllWindows()