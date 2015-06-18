# make an app here:
# https://www.flickr.com/services/apps/create/noncommercial/?
from os import environ
import requests
baseurl = 'https://api.flickr.com/services/rest/'
atts = {'api_key': environ['FLICKR_KEY'],
        'format': 'json',
        'method': 'flickr.photos.getInfo',
        'nojsoncallback': 1
        }
PHOTOID = '16762167456'
atts['photo_id'] = PHOTOID

photo = requests.get(baseurl, params = atts).json()['photo']

# now construct the photo URL
# https://www.flickr.com/services/api/misc.urls.html
#
# Example construction:
# https://farm1.staticflickr.com/2/1418878_1e92283336_o.jpg
# farm-id: 1
# server-id: 2
# photo-id: 1418878
# secret: 1e92283336
# size: o

domain = "https://farm{farm}.staticflickr.com"
path = "/{server}/{photo_id}_{secret}_{size}.{originalformat}"
photo_url = (domain + path).format(
    farm = photo['farm'],
    originalformat = photo['originalformat'],
    photo_id = photo['id'],
    secret = photo['originalsecret'],
    server = photo['server'],
    size = 'o'
)


### or just use get_sizes
# https://www.flickr.com/services/api/flickr.photos.getSizes.html
atts = {'api_key': environ['FLICKR_KEY'],
        'format': 'json',
        'method': 'flickr.photos.getSizes',
        'nojsoncallback': 1,
        'photo_id': PHOTOID
        }

resp = requests.get(baseurl, params = atts).json()
sizes = resp['sizes']
# assuming that :size attribute is always sorted, smallest to biggest
biggestsize = sizes['size'][-1]
