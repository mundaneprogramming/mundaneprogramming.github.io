from urllib.parse import urljoin
import os
import requests
INSTAGRAM_DOMAIN = 'https://api.instagram.com/'
DEFAULT_ACCESS_TOKEN = os.environ.get('INSTAGRAM_TOKEN')


def get_user_media(media_id, access_token = DEFAULT_ACCESS_TOKEN):
    """
    docs:
    https://instagram.com/developer/endpoints/media/#get_media
    example:
    https://api.instagram.com/v1/media/{media-id}?access_token=ACCESS-TOKEN
    """
    atts = {'media-id': media_id, 'access_token': DEFAULT_ACCESS_TOKEN}
    path = '/v1/media/%s' % media_id
    url = urljoin(INSTAGRAM_DOMAIN, path)
    resp = requests.get(url, atts).json()
