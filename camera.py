import cv2
import pyimgur
from constants import IMGUR_KEY


def use_camera():
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    cv2.imwrite(filename=r'images\image.jpg', img=frame)
    webcam.release()

    im = pyimgur.Imgur(IMGUR_KEY)
    upload = im.upload_image("images\image.jpg", title="name_any")

    return upload.link_big_square
