from PIL import Image
from PIL import ImageDraw
# from PIL import ImageFont
import argparse
import re
TEXT_COLOR = 'black'
FILL_COLOR = 'white'
CAPTION_AREA_HEIGHT = 30
CAPTION_LEFT_PADDING = 10
CAPTION_TOP_PADDING = 10


def caption_image(img, text):
    # Create new image instance and set fill color to FILL_COLOR
    img_width, img_height = img.size
    capimg = Image.new("RGB",
        (img_width, img_height + CAPTION_AREA_HEIGHT),
        FILL_COLOR)
    # Create a Draw instance
    capdraw = ImageDraw.Draw(capimg)
    # Add text onto the Draw
    capdraw.text(
        (CAPTION_LEFT_PADDING, img_height + CAPTION_TOP_PADDING),
        text, TEXT_COLOR)
    # Paste the original image onto the capimg instance
    capimg.paste(img, (0, 0))
    return capimg


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_filename", nargs = 1,
        help = "Image filename to caption")
    parser.add_argument("caption", nargs = 1,
       help = "Caption for the image")
    # parse the args
    args = parser.parse_args()
    img_fname = args.image_filename[0]
    caption_txt = args.caption[0]
    ## caption it
    img = caption_image(Image.open(img_fname), caption_txt)
    # sloppiest, most error-prone way to turn
    # filename.jpg to filename.captioned.jpg
    oname = re.sub(r'(\.?\w{3,4}$)', r'.captioned\1', img_fname)
    img.save(oname)
    print("Saved captioned image as", oname)
