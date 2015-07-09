import cv2
import os
import sys
import numpy as np
DEFAULT_FACES_CASCADE_PATH = '/usr/local/Cellar/opencv/2.4.11_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
CVOPTS = {
    'scaleFactor' : 1.01,
    'minNeighbors' : 3,
    'minSize' : (30, 30),
    'flags': cv2.cv.CV_HAAR_SCALE_IMAGE
}

def detect_things(image, cascadepath):
    """ image is a numpy Array; Returns array of
        detected objects, each as (x, y, w, h) """
    cascade = cv2.CascadeClassifier(cascadepath)
    # begin detection
    return cascade.detectMultiScale(image, **CVOPTS)

def get_biggest(things):
    """
    things is an array of numpy Arrays, each as (x, y, w, h)
    returns: biggest array by w * h
    """
    # each thing is a numpy.ndarray arranged as [x, y, width, height]
    tx = list(things)
    if tx:
        return max(tx, key = lambda t: t[2] * t[3])
    else:
        return None

def padd(cropdims, image, padding = 0.1):
    pads = padding # alias for easier reading
    imageh, imagew = image.shape[0:2]
    # get coordinates of the current crop
    top_x, top_y, cw, ch = cropdims
    bot_x = top_x + cw
    bot_y = top_y + ch
    if pads == 0:
        return cropdims
    elif type(pads) is float:
        pt = pb = pl = pr = pads
    elif len(pads) == 1:
        pt = pb = pl = pr = pads[0]
    elif len(pads) == 2: # e.g. (top/bottom, left/right)
        pt = pb = pads[0]
        pl = pr = pads[1]
    else:              # e.g. top, right, bottom, left
        pt, pr, pb, pl = pads
    # Should be abstracted out but who cares, it works:
    x0 = max(0, top_x - int(pl * cw))  # pad left coordinate
    y0 = max(0, top_y - int(pt * ch)) # pad top coordinate
    x1 = min(imagew, bot_x + int(pr * cw) ) # pad right
    y1 = min(imageh, bot_y + int(pb * ch)) # pad bottom
    # convert x1 and y1 to w and h
    return np.array([x0, y0, x1 - x0, y1 - y0])



def slice_image(image, dims):
    """
    image is a numpy array
    dims is a list as (x,y,w,h)
    returns: a sub-array of image based off of dims
    """
    x, y, w, h = dims
    return image[y:y+h, x:x+w]


def facecrop(image = None, image_path = None, cascadepath = DEFAULT_FACES_CASCADE_PATH, padding = 0.1):
    """this is the main wrapper method
    Returns a cv2 image object (numpy array) of the cropped face

    If no face was found, returns None
    """
    if not image:
        image = cv2.imread(image_path)

    # detect biggest face
    facedims = get_biggest(detect_things(image, cascadepath))
    if facedims is not None:
        # padd the area around the face
        padded_facedims = padd(facedims, image, padding)
        # cut out the face from the main image
        faceimg = slice_image(image, padded_facedims)
        return faceimg
    else:
        return None
