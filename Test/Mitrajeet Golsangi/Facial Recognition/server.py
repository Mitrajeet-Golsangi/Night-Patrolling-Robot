from flask import Flask, render_template, Response
from basics import get_frames

import imutils
import pyshine as ps

from flask_socketio import SocketIO, emit


app = Flask(__name__)

socketio = SocketIO( app )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@socketio.on('connect')
def connection_established():
    print("Client Connected !")

@socketio.on('vid_sock')
def handle_stream(vid):
    print("Client Connected !")
    socketio.send(get_frames())

if __name__ == '__main__':
    
    socketio.run(app, debug = True, host="192.168.29.155")