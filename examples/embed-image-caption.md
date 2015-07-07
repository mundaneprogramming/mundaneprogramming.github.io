---
title: Embed a photo caption
files:
  - name: code/imagecreditor_basic.py
    description: Simple commmand-line tool to add a single-line caption to an image
todo:
  - Use imagedraw.draw.textsize to calculate line width
  - look up other font width things
  - create imagecreditor_mutliline.py
  - create imagecreditor_customfont.py
  - create the wikicommons version
related_links:
  - title: textwrap module documentation
    url: https://docs.python.org/3/library/textwrap.html#module-textwrap
  - title: "python PIL draw multiline text on image - Stack Overflow (stackoverflow.com)"
    url: http://stackoverflow.com/questions/7698231/python-pil-draw-multiline-text-on-image
  - title: Wikipedia images in the United States public domain
    url: https://en.wikipedia.org/wiki/Category:Images_in_the_public_domain_in_the_United_States
  - title: Draw.textsize documentation
    url: http://pillow.readthedocs.org/en/latest/reference/ImageDraw.html#PIL.ImageDraw.PIL.ImageDraw.Draw.textsize
---


## The importance of captions and branding


## Installing Pillow

http://pillow.readthedocs.org/en/latest/installation.html

Need version 2.9 to get the `multiline_text` feature.


## Simple demonstration

Using the [invasion drawing by Captain Creekmore from D-day invasion of France.](https://en.wikipedia.org/wiki/File:Creekmore-gliders.jpg):


~~~sh
curl -s \
  https://upload.wikimedia.org/wikipedia/en/thumb/c/ca/Creekmore-gliders.jpg/640px-Creekmore-gliders.jpg \
  -o /tmp/gliders.jpg
python imagecreditor_basic.py /tmp/gliders.jpg "A depiction of D-Day by Captain Raymond Creekmore"
~~~

The resulting image:

![Creekmore Gliders](/files/images/gliders.captioned.jpg)

### Dealing with overflow

~~~sh
python imagecreditor_basic.py /tmp/gliders.jpg \
"A depiction of D-Day by Captain Raymond Creekmore
 Source: National Archives:Black and White and Color Photographs 
    of U.S. Air Force and Predecessor Agencies Activities,
    Facilities, and Personnel - World War II"
~~~

![Creekmore Gliders overflow caption](/files/images/gliders.overflow.captioned.jpg)


## Using `multiline_text`


Replace:

~~~py
    capdraw.text(
        (CAPTION_LEFT_PADDING, img_height + CAPTION_TOP_PADDING),
        text, TEXT_COLOR)
~~~

with:

~~~py
    capdraw.multiline_text(
        (CAPTION_LEFT_PADDING, img_height + CAPTION_TOP_PADDING),
        text, TEXT_COLOR)
~~~


![cutoff image](/files/images/gliders.cutoff.captioned.jpg)


## Finding text size

~~~py
from PIL import Image
from PIL import ImageDraw
draw = ImageDraw.Draw(Image.new('RGB', (0,0)))
txt = "A depiction of D-Day by Captain Raymond Creekmore\nSource: National Archives:Black and White and Color Photographs\nof U.S. Air Force and Predecessor Agencies Activities,\nFacilities, and Personnel - World War II"
draw.multiline_textsize(txt)
# (378, 44)
~~~
