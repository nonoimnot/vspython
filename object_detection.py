import cv2

cap = cv2.VideoCapture('http://192.168.1.101:64616/videostream.cgi?user=admin&pwd=alPHa1234')

while True:
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
