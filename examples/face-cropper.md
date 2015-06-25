---
title: Auto face cropper
authors:
  - dannguyen
featured: true
rank: 42
---


http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html

[Photograph of a Bride and Her Attendants in New Ulm, Minnesota; Art Hanson, 1974](https://www.flickr.com/photos/usnationalarchives/4727529322/)

via Archives: [DOCUMERICA: The Environmental Protection Agency's Program to Photographically Document Subjects of Environmental Concern, 1972 - 1977](https://catalog.archives.gov/id/542493)


https://docs.python.org/3.5/library/__main__.html




### Refactoring

~~~py
def pad_image(image, dims, top = 0.0, right = 0.0, left = 0.0, bottom = 0.0):
    # http://stackoverflow.com/questions/19098104/python-opencv2-cv2-wrapper-get-image-size
    x0, y0, w, h = dims
    x1, y1 = dims[0:1] + dims[2:3]
    height, width, channels = image.shape
~~~


~~~py
# test it out
def resize_to_fit(image, w, h):
    return cv2.resize(image, (w, h)) 

~~~




## Bash

~~~sh
curl -o congressimages.zip https://github.com/unitedstates/images/archive/gh-pages.zip
unzip congressimages.zip
mkdir -p unitedstates-images-originals
# copy over the original images
cp -r images-gh-pages/congress/original/ unitedstates-images-originals
# copy over necessary text files
cp images-gh-pages/{LICENSE,*.md} unitedstates-images-originals
zip -r unitedstates-images-originals.zip unitedstates-images-originals/
# copy using AWS S3
# http://docs.aws.amazon.com/cli/latest/reference/s3/index.html
aws s3 cp unitedstates-images-originals.zip s3://YOURBUCKETNAME --acl public-read
~~~

Make an excerpt file

~~~sh
# http://stackoverflow.com/questions/17578873/randomly-shuffling-files-in-bash
# gshuf shuffles things and is part of OS X homebrew coreutils
zip -r unitedstates-images-sample.zip \
  unitedstates-images-originals/{LICENSE,*.md} \
  $(ls unitedstates-images-originals/*.jpg | 
    gshuf | head -n 30) # don't normally do this... 
aws s3 cp unitedstates-images-sample.zip s3://YOURBUCKETNAME --acl public-read
~~~


To use:

~~~
url=http://www.mundaneprogramming.com.s3.amazonaws.com/zips/unitedstates-images-sample.zip
curl -O $url
unzip unitedstates-images-sample.zip
~~~

