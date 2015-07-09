import argparse
import facecrop
import os
import cv2

DEFAULT_CASCADES_PATH = facecrop.DEFAULT_FACES_CASCADE_PATH

parser = argparse.ArgumentParser()
parser.add_argument("imagepath", nargs = 1,
    help = "Path to image file")
parser.add_argument('--cascadepath', '-c',
    default = DEFAULT_CASCADES_PATH,
    help ='Path to haar cascades file; Default is ' + DEFAULT_CASCADES_PATH )
parser.add_argument('--output', '-o',
    help ='Specific path to output file, overrides --dir. Default is: imagepath.crop.jpg')
parser.add_argument('--dir', '-d',
    help ='Directory for output file, which will have basename of: imagepath.crop.jpg. Default is original directory of file')

parser.add_argument('--padding', '-p',
    default = 0,
    type = float,
    nargs = '*',
    help = """ Specify the padding around the detected object. Default is 0
        [top] [right] [bottom] [left]
        [topbottom] [leftright]
        [all sides]""")


# set up args
args = parser.parse_args()
imgpath = os.path.expanduser(args.imagepath[0])
cascadepath = os.path.expanduser(args.cascadepath)
padding = args.padding
if not args.output:
    # make no dirname path
    fn, ext = os.path.splitext(imgpath)
    if args.dir:
        fn = os.path.join(args.dir, os.path.basename(fn))
    outpath = '%s.crop%s' % (fn, ext)
else:
    outpath = os.path.expanduser(args.output)
# open image

faceimg = facecrop.facecrop(image_path = imgpath,
    cascadepath = cascadepath,
    padding = padding,
    )

if faceimg is not None:
    # save the file
    cv2.imwrite(outpath, faceimg)
    print("Saved to: %s " % outpath)
else:
    print("Warning; no object found in: %s" % imgpath)
