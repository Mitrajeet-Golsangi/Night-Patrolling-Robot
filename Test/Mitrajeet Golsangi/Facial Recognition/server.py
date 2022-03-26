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

@socket.on('vid_sock')
def handle_stream(vid):
    socket.send(Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame'))    

if __name__ == '__main__':
    
    socketio.run(app, debug = True)
