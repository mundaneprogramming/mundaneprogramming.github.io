---
title: Extract data about a Flickr photo
description: A command-line tool for getting the URL and metadata given a Flickr URL.
files:
  - name: code/flickurl.py
    description: A command-line script that contacts Flickr's API and pretty-prints photo info and URLs 
the_need: |
  This is a useful script for the many times that I pull content from [Flickr's vast Commons gallery](https://www.flickr.com/commons). The direct image URLs require another click to get to. In this example, I've chosen to output the data in a readable way, as I don't have just one use-case (i.e. copy-paste pattern) for a Flickr photo and its metadata.
the_routine:
  - Visit Flickr photo URL in browser
  - Copy-paste title
  - Copy-paste author name
  - Click the "Download this photo" link
  - Click "Original size" link
  - Right-click photo to get its direct URL
---


# Demo

Given a Flickr photo page URL:

[https://www.flickr.com/photos/zokuga/14392889220/](https://www.flickr.com/photos/zokuga/14392889220/)

![image](/files/images/screenshots/flickr.brooklyn4th.jpg){:.bord}


Run {% include github-link.html filename="code/flickurl.js" %} like so:

~~~sh
python flickurl https://www.flickr.com/photos/zokuga/14392889220/
~~~

This is what the output looks like:

![image](/files/images/screenshots/flickrscrapeoutput.png)



# Flickr APIs

This script uses two endpoints:

- [flickr.photos.getInfo](https://www.flickr.com/services/api/explore/flickr.photos.getInfo) - to get the metadata, including title, description, and posting date.
- [flickr.photos.getSizes](https://www.flickr.com/services/api/flickr.photos.getSizes.html) - to return the biggest available size of the photo.


## Sample flickr.photos.getInfo JSON

{% include snippets/codepiece.html relpath="snippets/flickr.brooklyn4th.getInfo.json" parentdir="examples/"%}
