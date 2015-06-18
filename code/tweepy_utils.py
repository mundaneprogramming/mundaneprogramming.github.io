from datetime import datetime
import time
import tweepy
import os
import json
from math import ceil

DEFAULT_TWITTER_CREDS_PATH = '~/.creds/me.json'

def get_api(credsfile = DEFAULT_TWITTER_CREDS_PATH):
    """
    Takes care of the Twitter OAuth authentication process and
    creates an API-handler to execute commands on Twitter

    Arguments:
      - credsfile (str): the full path of the filename that contains a JSON
        file with credentials for Twitter

    Returns:
      A tweepy.api.API object

    """
    fn = os.path.expanduser(credsfile)  # get the full path in case the ~ is used
    c = json.load(open(fn))
    # Get authentication token
    auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                               consumer_secret = c['consumer_secret'])
    auth.set_access_token(c['access_token'], c['access_token_secret'])
    # create an API handler
    return tweepy.API(auth)




def convert_twitter_timestamp(t):
    """
    t is something like 'Sat Jan 30 03:36:19 +0000 2010'
    return: a datetime object
    """

    return datetime.fromtimestamp(time.mktime(time.strptime(t, '%a %b %d %H:%M:%S +0000 %Y')))


def get_user_recent_tweets(screen_name):
    options = {}
    options['count'] = 200
    options['since_id'] = 1
    options['trim_user'] = True
    options['exclude_replies'] = False
    options['include_rts'] = True
    api = get_api()
    tweets = api.user_timeline(**options)
    return [t._json for t in tweets]



def get_user_profile(screen_name):
    api = get_api()
    users = api.lookup_users(screen_names = [screen_name])
    # lookup_users always returns array
    profile = users[0]
    return profile._json


def get_user_followers_sample(screen_name):
    api = get_api()
    ids = api.followers_ids(screen_name, count = 5000)
    users = api.lookup_users(user_ids = ids[-101:-1])

    return [user._json for user in users]



def get_user_friends_sample(screen_name):
    api = get_api()
    ids = api.friends_ids(screen_name, count = 5000)
    users = api.lookup_users(user_ids = ids[-101:-1])

    return [user._json for user in users]


def get_user(screen_name):
    """
    A convenience method
    Returns a dictionary:
    {
        'profile': the result of get_user_profile(screen_name),
        'tweets': the result of get_user_recent_tweets(screen_name),
        'followers': the result of get_user_followers_sample(screen_name),
        'friends': the result of get_user_friends_sample(screen_name)
    }
    """
    api = get_api()
    user = {}
    user['profile'] = get_user_profile(screen_name)
    user['tweets'] = get_user_recent_tweets(screen_name)
    user['followers'] = get_user_followers_sample(screen_name)
    user['friends'] = get_user_friends_sample(screen_name)
    # todo: get friend_ids, follower_ids

    return user


def package_user(screen_name, output_path = './'):
    bname = "%s-package-%s.json" % (screen_name.lower(), str(datetime.now().date()))
    fn = os.path.expanduser(os.path.join(output_path, bname))
    data = get_user(screen_name)
    with open(fn, 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(data, indent = 2))
    return bname


# gets a whole bunch of tweets
def get_full_user_timeline(screen_name, api = None, count = 3300):
    if api is None:
        api = get_api()
    tweets = []
    cursor = tweepy.Cursor(api.user_timeline, id = screen_name,
      trim_user = True, exclude_replies = False, include_rts = True)
    for tweet in cursor.items(count):
        tweets.append(tweet._json)

    return tweets

# gets a whole bunch of profile information from a batch of user IDs
# or screen names
def get_profiles_from_ids(user_ids = [], screen_names = []):
    if screen_names:
        data = screen_names
        darg = 'screen_names'
    else:
        data = user_ids
        darg = 'user_ids'

    api = get_api()
    batch_size = 100
    profiles = []

    for i in range(ceil(len(data) / batch_size)):
        s = i * batch_size
        uids = data[s:(s + batch_size)]
        _args = {darg: uids}
        for user in api.lookup_users(**_args):
            profiles.append(user._json)

    return profiles
