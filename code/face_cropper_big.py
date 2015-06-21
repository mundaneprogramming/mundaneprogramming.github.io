import cv2
import os
import sys
DEFAULT_FACES_CASCADE_PATH = '/usr/local/Cellar/opencv/2.4.11_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
CVOPTS = {
    'scaleFactor' : 1.2,
    'minNeighbors' : 3,
    'minSize' : (30, 30),
    'flags': cv2.cv.CV_HAAR_SCALE_IMAGE
}

def bigcrop(imagepath):
    """ imagepath is a str; Returns biggest object as numpy.ndarray
        or None if nothing found"""
    imgpath = os.path.expanduser(imagepath)
    image   = cv2.imread(imgpath)
    cascade = cv2.CascadeClassifier(DEFAULT_FACES_CASCADE_PATH)
    # begin detection
    faces = cascade.detectMultiScale(image, **CVOPTS)
    if len(faces) is 0: # i.e. empty
        return None
    else:
        # each thing is a numpy.ndarray arranged as [x, y, width, height]
        x, y, w, h = max(list(faces), key = lambda t: t[2] * t[3])
        return image[y:y+h, x:x+w]



if __name__ == "__main__":
    imgname = sys.argv[1]
    img = bigcrop(imgname)
    fn, ext = os.path.splitext(imgname)
    o = fn + '.crop' + ext
    cv2.imwrite(o, img)

