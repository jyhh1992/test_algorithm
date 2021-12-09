from flask import Flask
import cv2 as cv

app = Flask(__name__)

@app.route("/")
def helloworld():
    str = "Hello World!"
    return str
# /dev/video0
if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        ret , frame = cap.read()
        cv.imshow("webcam",frame)
        cv.waitKey(1)
        pass
    app.run(host='0.0.0.0', port='8000')