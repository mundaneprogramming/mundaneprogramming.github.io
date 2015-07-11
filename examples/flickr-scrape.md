---
title: Extract data about a Flickr photo
description: A command-line tool for getting the URL and metadata given a Flickr URL.
rank: 50
authors:
  - dannguyen
files:
  - name: code/flickurl.py
    description: A command-line script that contacts Flickr's API and pretty-prints photo info and URLs 
the_usecase: |
  Because Flickr has so many great, free images in its [vast Commons gallery](https://www.flickr.com/commons), I often find myself wanting to copy and embed stock images from the Flickr website, and to include attribution and link-backs for their creators.

  However, besides the tediousness of copying the title and author information, the direct URLs to the image files require two clicks to get to. So I've written a script that, given a Flickr photo page URL, extracts the important metadata, including the URL of the biggest available photo size. 

  In this example, I've chosen to output the data in a non-structured, human-readable way. However, I've also included boilerplate HTML for embedding the photo and metadata that I can paste into a blog post.
the_routine:
  - Visit Flickr photo URL in browser
  - Copy-paste title
  - Copy-paste author name
  - Click the "Download this photo" link
  - Click "Original size" link
  - Right-click photo to get its direct URL
related_links:
  - title: "Flickr: The Commons"
    url: https://www.flickr.com/commons
  - title: 'API docs for flickr.photos.getInfo'
    url: https://www.flickr.com/services/api/flickr.photos.getInfo.html
  - title: 'API docs for flickr.photos.getSizes'
    url: https://www.flickr.com/services/api/flickr.photos.getSizes.html
  - title: colorama Python package
    url: https://github.com/tartley/colorama


---


# Demo

Given a Flickr photo page URL:

[https://www.flickr.com/photos/zokuga/14392889220/](https://www.flickr.com/photos/zokuga/14392889220/)

![image](/files/images/screenshots/flickr.brooklyn4th.jpg){:.bord}


Run {% include github-link.html filename="code/flickurl.py" %} like so:

~~~sh
python flickurl.py https://www.flickr.com/photos/zokuga/14392889220/
~~~

This is what the output looks like:

![image](/files/images/screenshots/flickrscrapeoutput.png){:.bord}

### Boilerplate HTML image link

The boilerplate HTML image link is pretty basic, consisting only of hot-linking the Flickr image file, wrapped inside a clickable-link back to the Flickr photo page, and `alt` text. I've also chosen by default to pick the _first_ photo size that has both __width__ and __height__ under 1600 pixels, so that we don't hot-link to the URL of a 8000x6000-pixel wide photo:

~~~html
<a href="https://www.flickr.com/photos/zokuga/14392889220/" title="Go to Flickr page for: July 4th Fireworks, Brooklyn Bridge, 2014 by: Dan Nguyen"><img src="https://farm4.staticflickr.com/3917/14392889220_518de64af0_h.jpg" alt="July 4th Fireworks, Brooklyn Bridge, 2014 by: Dan Nguyen"></a>
~~~

And here's the result of that HTML, note that the image is clickable, and that this site's __CSS__ keeps it from being displayed at its full width on the page.

<a href="https://www.flickr.com/photos/zokuga/14392889220/" title="Go to Flickr page for: July 4th Fireworks, Brooklyn Bridge, 2014 by: Dan Nguyen"><img src="https://farm4.staticflickr.com/3917/14392889220_518de64af0_h.jpg" alt="July 4th Fireworks, Brooklyn Bridge, 2014 by: Dan Nguyen"></a>

You could further alter this script to print the HTML tags for displaying a caption.



# Code explanation

The {% include github-link.html filename="code/flickurl.py" %} is pretty straightforward. Its verbosity is due to the verbose nature of Flickr's JSON responses. For example, this is what the `title` attribute looks like in the `photos.getInfo` response:

~~~json
{
  "title": {
    "_content": "July 4th Fireworks, Brooklyn Bridge, 2014"
  }
}
~~~

So the Python needed to extract that value is:

~~~py
title = photo_info['title']['_content']
~~~


## Colorful output

To make the program's output easier to read, I used the [colorama package](https://github.com/tartley/colorama) and created my own function for printing out the headers to the output:

~~~py
from colorama import Fore, Style, Back, init as initcolorama
initcolorama()
# ...
def cprint(*txt):
    t = ' '.join([str(x) for x in txt])
    print(Back.BLACK + Fore.CYAN + Style.BRIGHT + t + Style.RESET_ALL)
~~~

![image](/files/images/screenshots/coloramaexample.png)


[colorama](https://github.com/tartley/colorama) is a pretty cool library, here's a screenshot [from the docs](https://github.com/tartley/colorama) showing all the different ways it can color text:

![Github image of colorama output](https://raw.githubusercontent.com/tartley/colorama/master/screenshots/ubuntu-demo.png)



## Flickr APIs

This script uses two endpoints:

- [flickr.photos.getInfo](https://www.flickr.com/services/api/explore/flickr.photos.getInfo) - to get the metadata, including title, description, and posting date.
- [flickr.photos.getSizes](https://www.flickr.com/services/api/flickr.photos.getSizes.html) - to return the biggest available size of the photo.


## Sample flickr.photos.getInfo JSON

{% include snippets/codepiece.html relpath="snippets/flickr.brooklyn4th.getInfo.json" parentdir="examples/"%}


## Sample flickr.photos.getSizes JSON

{% include snippets/codepiece.html relpath="snippets/flickr.brooklyn4th.getSizes.json" parentdir="examples/"%}
