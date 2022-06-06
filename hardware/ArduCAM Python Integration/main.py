'''
jpgstream.py : display live ArduCAM JPEG images using OpenCV

Copyright (C) Simon D. Levy 2017

This file is part of BreezyArduCAM.

BreezyArduCAM is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

BreezyArduCAM is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with BreezyArduCAM.  If not, see <http://www.gnu.org/licenses/>.
'''

import numpy as np
import base64
import mediapipe as mp
import time
import serial
import cv2

from helpers import *

import cv2
import base64
import websockets
import asyncio


PORT = 'COM4'         # Windows

BAUD = 921600       # Change to 115200 for Due

server_port = 5000

print("Started server on port : ", server_port)


mp_face_detection = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.4)


def draw_bbox(res, frame):
    for id, det in enumerate(res.detections):
        # mp_draw.draw_detection(frame, det)  #? Direct Method for drawing bounding box and feature points

        coord = det.location_data.relative_bounding_box
        ih, iw, ic = frame.shape

        bbox = int(coord.xmin * iw), int(coord.ymin * ih), \
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


async def transmit(websocket, path):
    print("Client Connected !")
    # Open connection to Arduino with a timeout of two seconds
    port = serial.Serial(PORT, BAUD, timeout=2)

    # Report acknowledgment from camera
    getack(port)

    # Wait a spell
    time.sleep(0.2)

    # Send start flag
    sendbyte(port, 1)

    try:
        while True:

            # Open a temporary file that we'll write to and read from
            tmpfile = open("tmp.jpg", "wb")

            # Loop over bytes from Arduino for a single image
            # written = False
            # prevbyte = None
            while True:

                # Read a byte from Arduino
                currbyte = port.read(1)

                tmpfile.write(currbyte)
                # If we've already read one byte, we can check pairs of bytes
                # if prevbyte:

                #     # Start-of-image sentinel bytes: write previous byte to temp file
                #     if ord(currbyte) == 0xd8 and ord(prevbyte) == 0xff:
                #         try:
                #             tmpfile.write(prevbyte)
                #             written = True
                #         except:
                #             pass
                #     # Inside image, write current byte to file
                #     if written:
                #         try:
                #             tmpfile.write(currbyte)
                #         except:
                #             pass
                # End-of-image sentinel bytes: close temp file and display its contents
                # if ord(currbyte) == 0xd9 and ord(prevbyte) == 0xff:
                if ord(currbyte) == 0xd9:
                    tmpfile.close()
                    img = cv2.imread("tmp.jpg")

                    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    res = face_detection.process(rgb)

                    if res.detections:
                        draw_bbox(res, img)

                    encoded = cv2.imencode('.jpg', img)[1]

                    data = str(base64.b64encode(encoded))
                    data = data[2:len(data)-1]

                    await websocket.send(data)
                # Track previous byte
                prevbyte = currbyte

    except websockets.connection.ConnectionClosed as e:
        print("Client Disconnected !")

        # Send stop flag
        sendbyte(port, 0)
    # except:
    #     print("Someting went Wrong !")
start_server = websockets.serve(
    transmit, host="192.168.29.196", port=server_port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# Send stop flag
sendbyte(port, 0)
