from flask import Flask, render_template, Response
from basics import get_frames

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.debug = True
    app.run(host="192.168.29.155")