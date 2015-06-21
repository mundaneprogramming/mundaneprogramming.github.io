import argparse
import cv2
import os
import sys
import numpy as np


def get_width_height(image):
    h, w = image.shape[0:2]
    return (w, h)




def resize_to_fill_with_aspect_ratio(image, w = None, h = None):
    iw, ih = get_width_height(image)
    if not w and not h:
        return image
    else:
        # TODO appropriate scale for smaller/bigger
        nfactor = w / float(iw) if h is None or w > h else h / float(ih)

    return cv2.resize(image, (int(iw * nfactor), int(ih * nfactor)))


def crop_to_fit(image, width = None, height = None):
    ow, oh = get_width_height(image)
    nw = width if width else ow
    nh = height if height else oh
    xoff = max((ow - nw) / 2, 0)
    yoff = max((oh - nh) / 2, 0)

    return image[yoff:nh+yoff, xoff:nw+xoff]

def fillcrop(image, width = None, height = None):
    new_img = resize_to_fill_with_aspect_ratio(image, crop_width, crop_height)
    return crop_to_fit(new_img, crop_width, crop_height)






if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("imagepath", nargs = 1,
        help = "Path to image file")
    parser.add_argument('dim', nargs = 1,
        help = "[width]x[height]. Either is optional, e.g. [width]x or x[height]"
    )
    parser.add_argument('--output', '-o',
        help ='Path to output file, default is: input.crop.jpg' )


    # set up args
    args = parser.parse_args()
    imgpath = os.path.expanduser(args.imagepath[0])


    # open image
    img = cv2.imread(imgpath)
    imgw, imgh = get_width_height(img)
    # set up variables for the biggest crop
    cw, _o, ch = args.dim[0].partition('x')
    crop_width = int(cw) if cw else None
    crop_height = int(ch) if ch else None
    new_img = fillcrop(img, crop_width, crop_height)
    # save the file
    if not args.output:
       fn, ext = os.path.splitext(imgpath)
       nw, nh = get_width_height(new_img)
       outpath = '%s.crop.%sx%s%s' % (fn, nw, nh, ext)
    else:
        outpath = os.path.expanduser(args.output)

    cv2.imwrite(outpath, new_img)




