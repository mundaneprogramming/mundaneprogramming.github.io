import argparse
import json
import os
import requests
import re
ACCESS_FILENAME = os.path.expanduser("~/Downloads/myinstagramcode.txt")
ACCESS_TOKEN = open(ACCESS_FILENAME).read().strip()
MEDIA_PATH = '/v1/media/shortcode/%s'
INSTAGRAM_DOMAIN = 'https://api.instagram.com'
TWEET_MAX_CHARS = 140
TWEET_URL_CHARS = 22 + 1 # for a newline
TWEET_PIC_CHARS = 23
TWEET_TEXT_CHARS = TWEET_MAX_CHARS - TWEET_URL_CHARS - TWEET_PIC_CHARS # e.g. 94

def extract_shortcode(weburl):
    # weburl is something like
    # https://instagram.com/p/4wwyYvQi1N/?taken-by=danwinny
    m = re.search('instagram.com/p/(\w+)', weburl)
    if m:
        return m.groups()[0]
    else: # just return whatever you got
        return weburl

def get_shortlink_photo(weburl):
    shortcode = extract_shortcode(weburl)
    path = MEDIA_PATH % shortcode
    url = INSTAGRAM_DOMAIN + path
    atts = {"access_token": ACCESS_TOKEN}
    resp = requests.get(url, params = atts).json()
    return resp['data']

def extract_photo_data(data):
    """
    data is a dict
    returns a dict with just a few fields
    """
    d = {
          'url': data['link'],
          'image_url': data['images']['standard_resolution']['url']
        }
    if data['caption']: # caption could be non existent
        d['caption'] = data['caption']['text']
    if data['location']:
        d['longitude'] = data['location']['longitude']
        d['latitude'] = data['location']['latitude']
        if data['location']['name']:
            d['location_name'] = data['location']['name']

    return d


def make_tweet_text_from_data(text, textlen = TWEET_TEXT_CHARS):
    # re.split('[.?!](?=\s|$)', 'hey! you? there are.')
    ttxt = ""
    for sentence in text.split('. '):
        if len(ttxt + sentence + '.')

parser = argparse.ArgumentParser()
parser.add_argument("shortcode", nargs = 1, help = "Instagram web URL/shortcode")
args = parser.parse_args()
shortcode = args.shortcode[0]

data = get_shortlink_photo(shortcode)
smalldata = extract_photo_data(data)
txt = json.dumps(smalldata, indent = 2)
print(txt)


