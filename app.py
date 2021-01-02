#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response,jsonify
import cv2
from camera import Camera
from predict import get_prediction
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')


def gen(camera):
    
    while True:
        frame = camera.get_frame()
        de = cv2.imdecode(frame,cv2.IMREAD_COLOR)
        frame=cv2.imwrite('/home/rmb571/Documents/flask-video-streaming/capture.jpeg',de)
        frame = camera.get_frame().tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
   
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/predict')
def result():
    score=get_prediction('/home/rmb571/Documents/flask-video-streaming/capture.jpeg').tolist()
    if score[1]>0.5:
        return jsonify({'Predict':'Tails'})
    else:
         return jsonify({'Predict':'Tails'})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
