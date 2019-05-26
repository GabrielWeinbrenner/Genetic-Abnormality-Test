from classifier import *
import time


RED = (0, 0, 255)

GREEN = (0, 255, 0)

BLUE = (255, 0, 0)

BORDER_COLOR = RED

BORDER_WIDTH = 5

RECTANGLE_BUFFER = 3


def show(image, caption=''):

    cv2.imshow(caption, image)


def get_image(webcam=0, delay=1):

    video_capture = cv2.VideoCapture(webcam)

    time.sleep(delay)

    image = video_capture.read()[1]

    video_capture.release()

    return image


def load_image(directory, flags=1):

    return cv2.imread(directory, flags)


def end():

    cv2.destroyAllWindows()
