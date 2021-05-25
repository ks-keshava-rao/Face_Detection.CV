# To try out  install sequentially
# pip3 install --find-links https://download.pytorch.org/whl/torch_stable.html torch==1.3.1 torchvision==0.4.2
# pip install facial-emotion-recognition
from facial_emotion_recognition import EmotionRecognition
import cv2

er = EmotionRecognition(device='cpu')
cam = cv2.VideoCapture(0)
while True:
    sucess, frame = cam.read()
    frame1 = er.recognise_emotion(frame, return_type='BGR')
    cv2.imshow('frame', frame1)
    key = cv2.waitKey(1)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()
