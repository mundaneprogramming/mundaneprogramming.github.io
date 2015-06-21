import argparse
import cv2
import os
import sys
import numpy as np
DEFAULT_FACES_CASCADE_PATH = '/usr/local/Cellar/opencv/2.4.11_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
CVOPTS = {
    'scaleFactor' : 1.2,
    'minNeighbors' : 3,
    'minSize' : (30, 30),
    'flags': cv2.cv.CV_HAAR_SCALE_IMAGE
}

def open_image(imagepath):
    return cv2.imread(imagepath)


def get_image_dims(image):
    return image.shape[0:2]

def detect_things(image, cascadepath):
    """ image is a numpy Array; Returns array of
        detected objects, each as (x, y, w, h) """
    cascade = cv2.CascadeClassifier(cascadepath)
    # begin detection
    return cascade.detectMultiScale(image, **CVOPTS)

def get_big(things):
    # each thing is a numpy.ndarray arranged as [x, y, width, height]
    return max(list(things), key = lambda t: t[2] * t[3])


def padd(imagew, imageh, cropdims, pads = (0.1, 0.1, 0.1, 0.1)):
    # get coordinates of the current crop
    top_x, top_y, cw, ch = cropdims
    bot_x, bot_y = top_x + cw, top_y + ch
    if len(pads) == 2: # e.g. (top/bottom, left/right)
        pt = pb = pads[0]
        pl = pr = pads[1]
    else:              # e.g. top, right, bottom, left
        pt, pr, pb, pl = pads
    # Should be abstracted out but who cares, it works:
    pt = int(pt * ch) # top pixels to pad
    pb = int(pb * ch) # bottom pixels to pad
    pl = int(pl * cw) # left pixels to pad
    pr = int(pr * cw) # right pixels to add
    x0 = max(0, top_x - pl)  # pad left coordinate
    y0 = max(0, top_y - pt) # pad top coordinate
    x1 = min(imagew, bot_x + pr) # pad right
    y1 = min(imageh, bot_y + pb) # pad bottom
    # convert x1 and y1 to w and h
    return np.array([x0, y0, x1 - x0, y1 - y0])



def resize_to_fill_with_aspect_ratio(image, w = None, h = None):
    iw, ih = get_image_dims(image)
    if not w and not h:
        return image
    elif w and h:
        nfactor = w / float(iw) if w > h else h / float(ih)
    else:
        nfactor = #TODO


    return cv2.resize(image, (nw, nh))


def crop_image(image, dims):
    x, y, w, h = dims
    return image[y:y+h, x:x+w]

def crop_to_fit(image, w, h):
    iw, ih = get_image_dims(image)
    if iw >= w and ih >= h:
        return image
    else:
        TODO



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("imagepath", nargs = 1,
        help = "Path to image file")
    parser.add_argument('--cascadepath', '-c',
        default = DEFAULT_FACES_CASCADE_PATH,
        help ='Path to haar cascades file' )

    # set up args
    args = parser.parse_args()
    imgpath = os.path.expanduser(args.imagepath[0])
    cascadepath = os.path.expanduser(args.cascadepath)
    # open image and detect
    img = open_image(imgpath)
    dims = get_biggest(detect_things(imgpath, cascadepath))
    # crop and resize
    new_img = crop_image(img, dims)
    new_img = resize_to_fill_with_aspect_ratio(new_img, NEWWIDTH, NEWHEIGHT)
    new_img = croptofit(new_img, NEWWIDTH, NEWHEIGHT)
    # save the file
    fn, ext = os.path.splitext(imgpath)
    outpath = fn + '.crop' + ext
    cv2.imwrite(outpath, new_img)




