---
title: Get data about an Instagram photo
featured: true
rank: 7
description: Another example of doing something you've already done -- finding the information about a photo -- but doing it via API
authors:
    - dannguyen
files:
  - name: code/instagram_shortcode_basic.py
    description: |
        Contains a function that, when given a URL of an Instagram photo, returns its data as JSON from Instagram's API.
  - name: code/instagram_shortcode_cli.py
    description: |
        Same functionality as before, except wrapped up as a slightly more convenient command-line script.
---

## Shortlink docs



[Get media by shortcode](https://instagram.com/developer/endpoints/media/#get_media_by_shortcode)

This is what we want to do:

~~~py
https://api.instagram.com/v1/media/shortcode/THESHORTCODE?access_token=ACCESS-TOKEN
~~~

> This endpoint returns the same response as GET `/media/media-id.`
> A media object's shortcode can be found in its shortcode URL.
> An example shortcode is `http://instagram.com/p/D/``
> Its corresponding shortcode is `D`.

## Find a photo

Find a photo:

        https://instagram.com/p/3eFma3IaPc/


### Get the short id

        3eFma3IaPc


### Reconstruct the URL

- the domain: `https://api.instagram.com`
- the path: `/v1/media/shortcode/3eFma3IaPc`
- the query string: `?access_token=ACCESS-TOKEN`

Copy the URL below, replace `ACCESS-TOKEN` with __your own access token__, and then paste it into your browser:

https://api.instagram.com/v1/media/shortcode/3eFma3IaPc?access_token=ACCESS-TOKEN


You should see something that looks like this:

![image](/files/images/nasainstagrambrowser.png)

Here's what it looks like properly formatted:

{% include snippets/codepiece.html relpath="snippets/instagram.nasa.photo.json" parentdir="examples/"%}


## Do it in code

~~~python
import requests
url = "https://api.instagram.com/v1/media/shortcode/3eFma3IaPc?access_token=ACCESS-TOKEN"
resp = requests.get(url).json()
data = resp['data']
print(data['caption']['text'])
~~~


## Break it up

~~~py
ACCESS_TOKEN = "YOUR-ACCESS-TOKEN"
INSTAGRAM_DOMAIN = 'https://api.instagram.com'
MEDIA_PATH = '/v1/media/shortcode/%s'

shortcode = '3eFma3IaPc'
path = MEDIA_PATH % shortcode
url = INSTAGRAM_DOMAIN + path
atts = {"access_token": ACCESS_TOKEN}
resp = requests.get(url, params = atts).json()
data = resp['data']
print(data['caption']['text'])
~~~





## Make it a function


~~~py
import os
import requests
ACCESS_FILENAME = os.path.expanduser("~/Downloads/myinstagramcode.txt")
ACCESS_TOKEN = open(ACCESS_FILENAME).read().strip()
MEDIA_PATH = '/v1/media/shortcode/%s'
INSTAGRAM_DOMAIN = 'https://api.instagram.com'

def get_shortcode_photo(shortcode):
    path = MEDIA_PATH % shortcode
    url = INSTAGRAM_DOMAIN + path
    atts = {"access_token": ACCESS_TOKEN}
    resp = requests.get(url, params = atts).json()
    
    return resp['data']
~~~


### Look for more inconveniences

    https://instagram.com/p/3y8KeoIaN3/?taken-by=nasa

    3y8KeoIaN3

How long did it take you to identify, highlight, and copy that shortcode? Was it a few seconds? Half a second? It doesn't matter; even a _tenth of a second_ is too slow for an action that petty.

~~~py
url = "https://instagram.com/p/3y8KeoIaN3/?taken-by=nasa"
extract_shortcode(url)
# 3y8KeoIaN3
~~~


### Naive solution

~~~py
def extract_shortcode(weburl):
    x = weburl.split('instagram.com/p/')[1]
    y = x.split('/')[0]
    return y

extract_shortcode(weburl)
~~~


#### Compatibility concerns

However, what if a user expects to still be able to use the shortcode?

~~~
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-74-df769bc53035> in <module>()
----> 1 extract_shortcode('3y8KeoIaN3')

<ipython-input-64-623589064a65> in extract_shortcode(weburl)
      1 def extract_shortcode(weburl):
----> 2     x = weburl.split('instagram.com/p/')[1]
      3     y = x.split('/')[0]
      4     return y

IndexError: list index out of range
~~~


~~~py
def extract_shortcode(weburl):
    u = weburl.split('instagram.com/p/')
    if len(u) > 1:
        x = u[1]
        return x.split('/')[0]
    else: # just return whatever you got
        return weburl

extract_shortcode('https://instagram.com/p/3y8KeoIaN3/?taken-by=nasa')
# 3y8KeoIaN3
extract_shortcode('https://instagram.com/p/3y8KeoIaN3/')
# 3y8KeoIaN3
extract_shortcode('3y8KeoIaN3')
# 3y8KeoIaN3
~~~


The full code can be found here: {% include snippets/github_raw_links.html filename="code/instagram_shortcode_basic.py" %}
