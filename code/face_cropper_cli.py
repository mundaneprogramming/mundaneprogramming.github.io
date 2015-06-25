import argparse
import cv2
import os
import sys
import numpy as np
from fillcrop import fillcrop
DEFAULT_FACES_CASCADE_PATH = '/usr/local/Cellar/opencv/2.4.11_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
CVOPTS = {
    'scaleFactor' : 1.2,
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
    return max(list(things), key = lambda t: t[2] * t[3])


def padd(cropdims, image, pads = 0.1):
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



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("imagepath", nargs = 1,
        help = "Path to image file")
    parser.add_argument('--cascadepath', '-c',
        default = DEFAULT_FACES_CASCADE_PATH,
        help ='Path to haar cascades file' )
    parser.add_argument('--output', '-o',
        help ='Path to output file, default is: imagepath.crop.jpg' )
    parser.add_argument('--dim', '-d',
        help = "[width]x[height]. Either is optional, e.g. [width]x or x[height]")
    parser.add_argument('--padding', '-p',
        default = 0,
        type = float,
        nargs = '*',
        help = """
            [top] [right] [bottom] [left]
            [topbottom] [leftright]
            [all sides]""")


    # set up args
    args = parser.parse_args()
    imgpath = os.path.expanduser(args.imagepath[0])
    cascadepath = os.path.expanduser(args.cascadepath)
    padding = args.padding
    if not args.output:
        fn, ext = os.path.splitext(imgpath)
        outpath = '%s.crop%s' % (fn, ext)
    else:
        outpath = os.path.expanduser(args.output)
    # open image
    img = cv2.imread(imgpath)
    # set up variables for the biggest crop
    cw, _o, ch = args.dim.partition('x') if args.dim else (None, None, None)
    crop_width = int(cw) if cw else None
    crop_height = int(ch) if ch else None
    # detect biggest thing
    thingdims = get_biggest(detect_things(img, cascadepath))
    # padd the image
    thingdims = padd(thingdims, img, padding)
    # cut out the thing from the main image
    thingimg = slice_image(img, thingdims)
    # fill and crop the thingimg by desired proportions
    thingimg = fillcrop(thingimg, crop_width, crop_height)
    # save the file
    fn, ext = os.path.splitext(imgpath)
    # save the file
    cv2.imwrite(outpath, thingimg)




