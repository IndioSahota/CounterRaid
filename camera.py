import cv2

#test
webcam = cv2.VideoCapture(0)
check, frame = webcam.read()
cv2.imwrite(filename=r'images\image.jpg', img=frame)
webcam.release()
