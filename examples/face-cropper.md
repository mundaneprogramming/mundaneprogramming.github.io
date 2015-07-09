---
title: Auto face cropper
authors:
  - dannguyen
featured: true
rank: 42
files:
  - name: code/face_cropper.py
    description: Find and crop all faces in an image.
  - name: code/face_cropper_big.py
    description: Crop just the biggest face from an image.
  - name: code/face_cropper_cli.py
    description: A command-line interface for cropping a face from an image.
---

Even if you're not able to achieve Facebook-level face-detection, it's still useful to be able to write tailored detection code that can meet your needs.

For example, if you're creating a data site based off the U.S. Congress membership, you probably want to show the face of each congressmember, because [faces add visual impact to a page](http://designshack.net/articles/graphics/a-practical-guide-to-designing-with-faces/), and especially since those images are free-to-use and [conveniently collected by the Sunlight Foundation](https://sunlightlabs.github.io/congress/#legislator-photos).

You can [clone their Github repo](https://github.com/unitedstates/images), but be warned, it's quite massive. You can practice with my sample of 30 photos here:

[http://www.mundaneprogramming.com.s3.amazonaws.com/zips/unitedstates-images-sample.zip](http://www.mundaneprogramming.com.s3.amazonaws.com/zips/unitedstates-images-sample.zip)

The photos themselves are nice and clear. But if you put them into an array, you'll see a visual inconsistency: some images include just the heads and shoulders, and other images are from the waist up:

![image](/files/images/photos/congress-sample-inconsistencies.jpg)

With 500+ sitting members of Congress, it will be painful to pick out the photos that need to be cropped and than manually crop them. However, we just need a pretty basic implementation of face-detection for a Python script, because in this case, every Congressmember's photo has a relatively obvious face, and so we can set the `detectMultiScale()` parameters to be very loose in finding candidates, and then just pick the biggest detected face...on the assumption that the biggest detected face is the _actual_ face.


## Demo

Download the sample files:

~~~sh
mkdir -p /tmp/testpeople
cd /tmp/testpeople
url=http://www.mundaneprogramming.com.s3.amazonaws.com/zips/unitedstates-images-sample.zip
# download the file
curl -O $url
# unzip the zip
unzip unitedstates-images-sample.zip
~~~

Run the script:

~~~sh
mkdir -p /tmp/testfaces # a new directory to save the faces
cd /tmp/testpeople # just in case you aren't there already...
for f in unitedstates-images-originals/*.jpg; do 
  python facecrop_cli.py $f -d /tmp/testfaces
done
~~~

Pre-Crop (e.g. `/tmp/testpeople`):

![image](/files/images/photos/congress-originals-excerpt-finder.jpg)

Post-Crop (e.g. `/tmp/testfaces`):

![image](/files/images/photos/congress-mugs-excerpt-finder.jpg)









## Random stuff

These are scripts to prepare the data for this lesson. No context is given.

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

Make an excerpt file of the images

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

