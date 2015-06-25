from datetime import datetime
import tweepy
import os
import json

DEFAULT_TWITTER_CREDS_PATH = '~/.creds/me.json'
MAX_COUNT = 200

THE_SCREEN_NAME = 'opennews'

def get_api(credsfile = DEFAULT_TWITTER_CREDS_PATH):
    fn = os.path.expanduser(credsfile)
    c = json.load(open(fn))
    auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                               consumer_secret = c['consumer_secret'])
    auth.set_access_token(c['access_token'], c['access_token_secret'])
    return tweepy.API(auth)


def get_timeline(screen_name):
    print("Downloading tweets for:", screen_name)
    api = get_api()
    tweets = []
    cursor = tweepy.Cursor(api.user_timeline, id = screen_name,
        trim_user = True, exclude_replies = False, include_rts = True)
    for tweet in cursor.items(MAX_COUNT):
        tweets.append(tweet._json)
    return tweets


def save_to_file(screen_name, tweets):
    fn = "%s.json" % screen_name
    f = open(fn, 'w')
    data = json.dumps(tweets, indent = 2)
    f.write(data)
    f.close()



## Now run script
tweets = get_timeline(THE_SCREEN_NAME)
save_to_file(THE_SCREEN_NAME, tweets)
