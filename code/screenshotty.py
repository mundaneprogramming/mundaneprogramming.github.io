#!/usr/bin/env python3
import argparse
from datetime import datetime
from os.path import splitext, expanduser, relpath
from PIL import Image
from subprocess import call
from tempfile import NamedTemporaryFile
from time import sleep

# http://stackoverflow.com/questions/89228/calling-an-external-command-in-python
APPROVED_FORMAT_ALIASES = ['jpg', 'jpeg', 'gif', 'png']
GIF_FORMAT = 'gif'
JPEG_FORMAT = 'jpeg'
PNG_FORMAT = 'png'
JPG_QUALITY_MAX = 95
JPG_QUALITY_DEFAULT = 75
PNG_COMPRESS_LEVEL_MAX = 9
PNG_COMPRESS_LEVEL_MIN = 0
PNG_COMPRESS_LEVEL_DEFAULT = 6

## DEFINE PARSER
parser = argparse.ArgumentParser()
parser.add_argument("output_path", nargs = 1, help = "Path to save file to")


parser.add_argument('--best', '-b',
    action = "store_true",
    help ="Do not do any optimization or compression" )

parser.add_argument('--format', '-f',
    help ='Specify a format, such as jpg, png, gif' )

parser.add_argument('--pause', '-p',
    default = 2,
    help ='Number of seconds to wait before taking the screenshot')

parser.add_argument('--quality', '-q',
    help ='Set a quality level from 0 to 100' )



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
        oopsmsg = "Image output format or file extension was: %s\n It must be: %s" % (ofmt, ', '.join(APPROVED_FORMAT_ALIASES))
        raise Exception(oopsmsg)

def save_image(img, filename, output_format, **kwargs):
    add_meta_screenshot_timestamp(img)
    img.save(filename, output_format, **kwargs)
    return filename

#######################
# BEGIN ARGUMENT PARSING

### CLI
args = parser.parse_args()
output_path = expanduser(args.output_path[0])
pause_sec = int(args.pause)

## determine optimization level
if args.best:
    do_optimization_pass = False
    qlevel = None

else:
    do_optimization_pass = True
    qlevel =  str(args.quality).lower() if args.quality else None

## choose a format; either it's explicitly set via --format
if args.format:
    _ofmt = args.format.lower()
else:  # or it is implicit in output_path's extension
    _ofmt = splitext(output_path)[1].split('.')[-1].lower()
    # by default, make it a PNG if there is no extension
    _ofmt = _ofmt if _ofmt else 'png'

output_format = get_canonical_format_name(_ofmt)


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

### Begin process
## Sleep
sleep(pause_sec)

### Start the screencapture process
## create a temp filename
tempscreengrab_file = NamedTemporaryFile(suffix = '.png')
# yield to user control and take the screenshot
call(["screencapture", "-i", "-o", "-s", tempscreengrab_file.name])

# reopen the saved screenshot file
img = Image.open(tempscreengrab_file.name).convert('RGBA')
save_image(img, output_path, output_format, **output_args)
# remove the temp screen grab file from memory
tempscreengrab_file.close()


print("\n######\nSaving to %s,\nas format %s,\nwith parameters %s\n########\n" % (output_path, output_format, output_args ))

# print markdown version
print("![image](%s)" % relpath(output_path))
print("\n")
