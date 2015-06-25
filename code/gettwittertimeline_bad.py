# An example of a bad attempt at using Twitter API
# to get a user's tweets, including hardcoding your own
# credentials into the file.
#
# ... but you have to start somewhere
# Crappy code meant to be pasted into iPython

import tweepy
import os
import json

# Get an API handler
fn = os.path.expanduser(DEFAULT_TWITTER_CREDS_PATH)
c = json.load(open(fn))
auth = tweepy.OAuthHandler(
            consumer_key = "MYCONSUMERKEY_BADBAD",
            consumer_secret = "MYCONSUMERSECRET_BADBAD")
auth.set_access_token("MYACCESSTOKENBADBAD", "MY_ACCESSOTKEN_SECRET_BADBAD!")
# and now authenticate
api = tweepy.API(auth)

# Now use the user_timeline method
print("Downloading tweets for:", "opennews") # look how much we repeat "opennews"
tweets = []
cursor = tweepy.Cursor(api.user_timeline, id = "opennews",
    trim_user = True, exclude_replies = False, include_rts = True)
for tweet in cursor.items(200):
    tweets.append(tweet._json)

# Now save to file
fn = "opennews" + '.json'
f = open(fn, 'w')
data = json.dumps(tweets, indent = 2)
f.write(data)
f.close()

