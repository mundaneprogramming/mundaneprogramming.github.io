---
title: Quickly crop and create image previews and thumbnails.
description: Use Python's Pillow library to calculate the proper dimensions for a resized image.
authors:
  - dannguyen
files:
  - name: code/fillcrop.py
  - name: code/fillcrop_cv2.py
    description: |
      A clunky implementation using the __cv2__ library. Functionally, no different than `fillcrop.py`

todos:
  - describe fillcrop.py
  - quick rundown of the ImageOps library
the_routine:
  - Open the image in Photoshop.
  - Crop the image to the desired dimensions.
  - Save the image.
---


## Using `ImageOps.fit()`

Sample image:

Margaret Barr's "Strange Children" [ballet], 1955 / photographer unknown
https://www.flickr.com/photos/statelibraryofnsw/4944459226/
https://farm5.staticflickr.com/4118/4944459226_dfc7414a3b_o.jpg
mirror: [/files/images/photos/mbarr-strange-children.jpg](/files/images/photos/mbarr-strange-children.jpg)
Original 800x582

### Setup

![original mbarr](/files/images/photos/mbarr-strange-children.jpg)

~~~py
from PIL import ImageOps
from PIL import Image
img = Image.open("mbarr.jpg")
w, h = img.size
~~~

### Half size

~~~py
fimg = ImageOps.fit(img, (w // 2, h // 2))
fimg.save("mbarr.half.jpg")
~~~

![barr half](/files/images/photos/mbarr.half.jpg)



### Square

~~~py
fimg = ImageOps.fit(img, (300, 300))
fimg.save("mbarr.square.jpg")
~~~

![barr square](/files/images/photos/mbarr.square.jpg)

### Much wider

~~~py
fimg = ImageOps.fit(img, (w, h // 2))
fimg.save("mbarr.wider.jpg")
~~~

![barr wider](/files/images/photos/mbarr.wider.jpg)

### Much taller

~~~py
ximg = ImageOps.fit(img, (w // 2, h))
ximg.save("mbarr.taller.jpg")
~~~

![barr taller](/files/images/photos/mbarr.taller.jpg)


### Fixed at 300x200
~~~py
ximg = ImageOps.fit(img, (300, 200))
ximg.save("mbarr.300x200.jpg")
~~~

![barr 300x200](/files/images/photos/mbarr.300x200.jpg)
