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
    url: http://effbot.org/imagingbook/imagedraw.htm#tag-ImageDraw.Draw.textsize
---





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





## Setting text size

