#!/usr/bin/env python3

import os.path
from os.path import splitext
import argparse
from datetime import datetime
from PIL import Image
from time import sleep
from subprocess import call
from tempfile import NamedTemporaryFile
# http://stackoverflow.com/questions/89228/calling-an-external-command-in-python

JPEG_FORMAT = 'jpeg'
GIF_FORMAT = 'gif'
PNG_FORMAT = 'png'

APPROVED_FORMAT_ALIASES = ['jpg', 'jpeg', 'gif', 'png']
PNG_COMPRESS_LEVEL_MAX = 9
PNG_COMPRESS_LEVEL_MIN = 0
PNG_COMPRESS_LEVEL_DEFAULT = 6
JPG_QUALITY_MAX = 95
JPG_QUALITY_DEFAULT = 75

"""
--pause SEC, -p SEC   Pause w seconds before activating the screengrab functionality
# --w [W]x[H], -d [W]x[H]    resize image to specifications. Leave a dimension blank for scale to fit
--format FORMAT, -f FORMAT   manually specify a format. Otherwise, it's inferred from save path
--optimization, -o  Number from 1-100 for quality for lossy compression
--raw, -r Full quality, overrides optimize
--color, -c   [RGB/BW/16]
"""

## DEFINE PARSER
parser = argparse.ArgumentParser()
parser.add_argument("output_path", nargs = 1, help = "Path to save file to")

parser.add_argument('--pause', '-p',
    default = 2,
    help ='Number of seconds to wait before taking the screenshot')

parser.add_argument('--format', '-f',
    help ='Specify a format, such as jpg, png, gif' )

parser.add_argument('--best', '-b',
    action = "store_true",
    help ="Do not do any optimization or compression" )


parser.add_argument('--optimization', '-o',
    help ='Do optimization' )



################ HELPER FUNCTIONS

def add_meta_screenshot_timestamp(img):
    """
    modifies img to have info['screenshot-timestamp'] = isoformat timestamp
    """
    img.info['screenshot-timestamp'] = datetime.now().isoformat()
    return img.info['screenshot-timestamp']



def get_canonical_format_name(ofmt):
    o = ofmt.lower().strip()
    # "jpg" must be "JPEG"
    if o == "jpg" or o == 'jpeg':
        return JPEG_FORMAT
    elif o == 'gif':
        return GIF_FORMAT
    elif o == 'png':
        return PNG_FORMAT
    else:
        raise FormatError()


def save_as(img, filename, output_format, **kwargs):
    add_meta_screenshot_timestamp(img)
    img.save(filename, output_format, **kwargs)
    return filename

class FormatError(Exception):
    """Exception raised for not having the correct format

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self):
        msg = "Image output format must be: %s" % ', '.join(APPROVED_FORMAT_ALIASES)
        super(Exception, self).__init__(msg)

# def save_as_gif(img, filename):
#     img.save(filename, format = 'gif')
#     return filename

# def save_as_jpg(img, filename, quality = JPG_QUALITY_DEFAULT, optimize = True):
#     """
#     saves to disk, returns path of file
#     """
#     img.save(filename, format = 'jpg', quality = quality)
#     return outfn

# def save_as_png(img, filename, compress_level = PNG_COMPRESS_LEVEL_DEFAULT, optimize = False):
#     """
#     saves to disk, returns path of file
#     """
#     img.save(filename, format = 'png', compress_level = compress_level, optimize = optimize)
#     return filename


#######################
# BEGIN ARGUMENT PARSING




### CLI
args = parser.parse_args()
output_path = os.path.expanduser(args.output_path[0])
pause_sec = int(args.pause)


## determine optimization level
if args.best:
    do_optimization_pass = False
    qlevel = None

else:
    do_optimization_pass = True
    qlevel =  str(args.optimization).lower() if args.optimization else None



## choose a format; either it's explicitly set via --format
if args.format:
    _ofmt = args.format.lower()
else:  # or it is implicit in output_path's extension
    _ofmt = splitext(output_path)[1].split('.')[-1].lower()
    # by default, make it a PNG if there is no extension
    _ofmt = _ofmt if _ofmt else 'png'

output_format = get_canonical_format_name(_ofmt)





### Begin process

## Sleep
sleep(pause_sec)

### Start the screencapture process
## create a temp filename
tempscreengrab_file = NamedTemporaryFile(suffix = '.png')
# yield to user control and take the screenshot
call(["screencapture", "-i", "-o", "-s", tempscreengrab_file.name])





# Save the file depending on output_format

##############
# if output_format is jpg
# http://pillow.readthedocs.org/en/latest/handbook/image-file-formats.html#jpg
output_args = {}
if output_format == JPEG_FORMAT:
    if do_optimization_pass:
        if qlevel == 'max':
            qlevel = JPG_QUALITY_MAX
        else:
            qlevel = int(qlevel) if qlevel else JPG_QUALITY_DEFAULT
    else:
        qlevel = JPG_QUALITY_MAX

    output_args.update({'optimize':do_optimization_pass, 'quality': qlevel})



##############
# if format is png
#
# http://pillow.readthedocs.org/en/latest/handbook/image-file-formats.html#png
# in the case of PNG files
#  (optimize = True) overrides compress_level
#    i.e. it will cause Image#save to automatically set
#    compress_level to MAX_PNG_COMPRESS_LEVEL
#    so instead, we set compress_level to the default and set optimize to False
#    since we don't want that optimize parameter to override compress_level
#
#  if user specifies --best-quality, then compress_level is set to MIN_PNG_COMPRESS_LEVEL
#    and optimize is set to False
elif output_format == PNG_FORMAT:
    if do_optimization_pass:
        if qlevel == 'max':
            qlevel = PNG_COMPRESS_LEVEL_MAX
        else:
            if qlevel:
                qlevel = round((int(qlevel) / 100) * PNG_COMPRESS_LEVEL_MAX)
            else:
                qlevel = PNG_COMPRESS_LEVEL_DEFAULT
    else:
        qlevel = PNG_COMPRESS_LEVEL_MIN

    output_args.update({'optimize': False, 'compress_level': qlevel})


# if format is GIF
# there are no special parameters for GIF
elif output_format == GIF_FORMAT:
    pass



# reopen the saved screenshot file
print("\n######\nSaving to %s,\nas format %s,\nwith parameters %s\n########\n" % (output_path, output_format, output_args ))
img = Image.open(tempscreengrab_file.name).convert('RGBA')
save_as(img, output_path, output_format, **output_args)






# remove the temp screen grab file from memory
tempscreengrab_file.close()
