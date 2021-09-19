import cv2

<<<<<<< Updated upstream
def use_camera(self):
=======
def use_camera():
>>>>>>> Stashed changes
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    cv2.imwrite(filename=r'images\image.jpg', img=frame)
    webcam.release()
