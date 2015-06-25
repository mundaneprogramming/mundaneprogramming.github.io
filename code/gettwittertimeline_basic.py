# Crappy code meant to be pasted into iPython

import tweepy
import os
import json

DEFAULT_TWITTER_CREDS_PATH = '~/.creds/me.json'
MAX_COUNT = 200

screen_name = 'opennews'


# Get an API handler
fn = os.path.expanduser(DEFAULT_TWITTER_CREDS_PATH)
c = json.load(open(fn))
auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                           consumer_secret = c['consumer_secret'])
auth.set_access_token(c['access_token'], c['access_token_secret'])
# and now authenticate
api = tweepy.API(auth)


# Now use the user_timeline method
print("Downloading tweets for:", screen_name)
tweets = []
cursor = tweepy.Cursor(api.user_timeline, id = screen_name,
    trim_user = True, exclude_replies = False, include_rts = True)
for tweet in cursor.items(MAX_COUNT):
    tweets.append(tweet._json)

# Now save to file
fn = "%s.json" % screen_name
f = open(fn, 'w')
data = json.dumps(tweets, indent = 2)
f.write(data)
f.close()

