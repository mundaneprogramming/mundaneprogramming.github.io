# make an app here:
# https://www.flickr.com/services/apps/create/noncommercial/?
# also, via wikipedia
# https://github.com/wikimedia/pywikibot-core/blob/master/scripts/flickrripper.py
from colorama import Fore, Style, Back, init as initcolorama
from datetime import datetime
from os import environ
import argparse
import re
import requests
import json

BASE_URL = 'https://api.flickr.com/services/rest/'
MAX_DISPLAYABLE_PHOTO_DIMENSION = 1600 # i.e. a photo with width and height <= 1600

def get_photo_info(photo_id, api_key):
    """
    This calls the Flickr endpoint to get a photo's metadata
    https://www.flickr.com/services/api/flickr.photos.getInfo.html
        photo_id: a number or string
        return: a dict containing the Flickr response
    """

    atts = {'api_key': api_key,
            'format': 'json',
            'method': 'flickr.photos.getInfo',
            'nojsoncallback': 1
            }
    atts['photo_id'] = photo_id
    photo = requests.get(BASE_URL, params = atts).json()['photo']
    return photo


def get_photo_sizes(photo_id, api_key):
    """
    This calls the Flickr endpoint to get a list of available photosizes
    https://www.flickr.com/services/api/flickr.photos.getSizes.html
        photo_id: a number or string
        return: a dict containing the Flickr response
    """
    atts = {'api_key': api_key,
        'format': 'json',
        'method': 'flickr.photos.getSizes',
        'nojsoncallback': 1,
        'photo_id': photo_id
        }
    # assuming that :size attribute is always sorted, smallest to biggest
    data = requests.get(BASE_URL, params = atts).json()
    return data

def get_biggest_photo_url(sizeinfo):
    """
    returns the URL of the biggest available version of a Flickr photo
    sizeinfo: a dict containing the Flickr API response for photos.getSizes
    """
    # assuming that :size attribute is always sorted, smallest to biggest
    biggest = sizeinfo['sizes']['size'][-1]
    return biggest['source']


def get_displayable_photo_url(sizeinfo, max_dim = MAX_DISPLAYABLE_PHOTO_DIMENSION):
    """
    returns the URL of the first photo to have width and height less-than-or-equal to
        a specified number of pixels
    sizeinfo: a dict containing the Flickr API response for photos.getSizes
    maxdim: the max number of pixels
    """
    sizes = reversed(sizeinfo['sizes']['size']) # since sizes are smallest to biggest
    url =  next(s['source'] for s in sizes if (
                int(s['width']) <= max_dim and int(s['height']) <= max_dim ))
    return url


def extract_photo_id(url):
    """
    Extracts the numerical photo ID from a Flickr photo page URL
    e.g. https://www.flickr.com/photos/statelibraryofnsw/4944459226/
    or already a photo ID, e.g. 4944459226
    """
    m = re.search("flickr.com/photos/\w+/(\d+)", url)
    if m:
        return m.groups()[0]
    else:
        # a
        return url

def extract_canonical_url(photo_info):
    """
    Returns the dict that contains canonical photopage URL and dimensions
    photo_info is a dict:
        "urls": {
          "url": [
            {
              "type": "photopage",
              "_content": "https://www.flickr.com/photos/statelibraryofnsw/4944459226/"
            }
          ]
        },
    """
    return next(url['_content'] for url in photo_info['urls']['url'] if url['type'] == 'photopage')


if __name__ == '__main__':
    # get some colors
    initcolorama()
    def cprint(*txt):
        t = ' '.join([str(x) for x in txt])
        print(Back.BLACK + Fore.CYAN + Style.BRIGHT + t + Style.RESET_ALL)
    # set API key
    api_key = environ['FLICKR_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument("url", nargs = 1, help = "Flickr photo URL or ID")
    args = parser.parse_args()
    url = args.url[0]
    photo_id = extract_photo_id(url)
    photo_info = get_photo_info(photo_id, api_key)
    sizes_info = get_photo_sizes(photo_id, api_key)
    # extract some variables
    title = photo_info['title']['_content']
    canonurl = extract_canonical_url(photo_info)
    owner_name = photo_info['owner']['realname']
    display_url = get_displayable_photo_url(sizes_info)
    biggest_url = get_biggest_photo_url(sizes_info)
    # We need to sanitize quotemarks before inserting it into HTML
    title_owner = (title + " by: " + owner_name).replace('"', "''")
    # print copyable HTML
    htmllink = """<a href="{page_url}" title="Go to Flickr page for: {title}"><img src="{src_url}" alt="{title}"></a>""".format(
                page_url = canonurl, src_url = display_url, title = title_owner
            )
    cprint("HTML image link")
    print(htmllink)
    # print title
    cprint("Title")
    print(title)
    # print canonical url
    cprint("Photo page")
    print(canonurl)
    # owner name
    cprint("Owner name")
    print(owner_name)
    # print direct url to photo
    cprint("Biggest image URL")
    print(biggest_url)
    # dates
    if photo_info['dates'].get('taken'):
        cprint("Date taken")
        print(photo_info['dates']['taken'])
    if photo_info['dates'].get('posted'):
        cprint("Date posted")
        d = datetime.fromtimestamp(int(photo_info['dates'].get('posted'))).isoformat()
        print(d)
    # description
    cprint("Description")
    print(photo_info['description']['_content'])
    cprint("Available photo sizes")
    # print meta of photo url
    for size in sizes_info['sizes']['size']:
        print(size['label'], "%sx%s" % (size['width'], size['height']))
        print(size['source'])

