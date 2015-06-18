from time import sleep
from urllib.parse import urljoin
import os
import requests

BASE_DOMAIN = 'https://api.instagram.com/'
BATCH_ITEM_COUNT = 50
DEFAULT_ACCESS_TOKEN = os.environ.get('INSTAGRAM_TOKEN')


# returns a list of users
def search_users_by_name(username, access_token = DEFAULT_ACCESS_TOKEN):
    atts = {'q': username, 'access_token': access_token}
    path = '/v1/users/search'
    url = urljoin(BASE_DOMAIN, path)
    resp = requests.get(url, params = atts).json()
    return resp['data']

# a convenience method so that other methods can be invoked by username
# returns a user_id String based on an exact match of username
def get_user_id_from_username(username, access_token = DEFAULT_ACCESS_TOKEN):
    users = search_users_by_name(username)
    uid = [u['id'] for u in users if u['username'].lower() == username.lower()]
    return uid[0] if uid else None

# returns a Dictionary: a single user profile
def get_user_profile(username = None, user_id = None, access_token = DEFAULT_ACCESS_TOKEN):
    user_id = user_id if user_id else get_user_id_from_username(username, access_token)
    # https://instagram.com/developer/endpoints/users/#get_users
    if user_id is None:
        return None
    atts = {'access_token': access_token}
    path = '/v1/users/%s/' % user_id
    url = urljoin(BASE_DOMAIN, path)
    resp = requests.get(url, params = atts).json()
    return resp['data']

# returns a list of media no greater than max_count
def get_user_media(username = None, user_id = None, max_count = 100000, sleep_sec = 2, access_token = DEFAULT_ACCESS_TOKEN):
    user_id = user_id if user_id else get_user_id_from_username(username, access_token)
    # http://instagram.com/developer/endpoints/users/#get_users_media_recent
    if user_id is None:
        return None
    atts = {'access_token': access_token, 'count': BATCH_ITEM_COUNT}
    path = '/v1/users/%s/media/recent' % user_id
    url = urljoin(BASE_DOMAIN, path)
    items = []
    # begin the data requests
    while len(items) < max_count:
        resp = requests.get(url, params = atts).json()
        data = resp['data']
        if len(data) > 0:
            items.extend(data)
            maxid = data[-1]['id']
            atts['max_id'] = maxid
            # tell the user what's going on
            print("Item count:", len(items), "  max_id:", maxid)
            sleep(sleep_sec)
        else:
            break
    return items





