import os
import requests
ACCESS_FILENAME = os.path.expanduser("~/Downloads/myinstagramcode.txt")
ACCESS_TOKEN = open(ACCESS_FILENAME).read().strip()
MEDIA_PATH = '/v1/media/shortcode/%s'
INSTAGRAM_DOMAIN = 'https://api.instagram.com'

def extract_shortcode(weburl):
    u = weburl.split('instagram.com/p/')
    if len(u) > 1:
        x = u[0]
        return x.split('/')[0]
    else: # just return whatever you got
        return weburl

def get_shortlink_photo(weburl):
    shortcode = extract_shortcode(weburl)
    path = MEDIA_PATH % shortcode
    url = INSTAGRAM_DOMAIN + path
    atts = {"access_token": ACCESS_TOKEN}
    resp = requests.get(url, params = atts).json()

    return resp['data']
