"""
Get all Twitter handles listed on a page, add them to a list
"""

import tweepy
import requests
import re
import json
from os.path import expanduser
TWITTER_CREDS_FILE = expanduser('~/.creds/me.json')
SOURCE_URL = 'http://srccon.org/sessions/'
LIST_NAME = 'srccon-2015-peeps'
BATCH_COUNT = 50

###
### Downloading the page and getting names
html = requests.get(SOURCE_URL).text
names = set([n.lower() for n in re.findall('twitter.com/@?(\w+)', html)])
# whatever, good enough for me
print("%s Twitter accounts found" %len(names))

###
### Fire up Tweepy and get an api handler
c = json.load(open(TWITTER_CREDS_FILE))
auth = tweepy.OAuthHandler(c['consumer_key'], c['consumer_secret'])
auth.set_access_token(c['access_token'], c['access_token_secret'])
api = tweepy.API(auth)
myname = api.me().screen_name

###
### Create and add to the list
print("Creating list %s/%s" % (myname, LIST_NAME))
api.create_list(LIST_NAME)
# apparently it needs to be broken up
for i in range(0, (len(names) // BATCH_COUNT) + 1):
    k = (i * 50), ((i+1) * 50)
    somenames = list(names)[k[0]:k[1]]
    print("Adding members %s - %s" % (k[0], k[0] + len(somenames)))
    api.add_list_members(somenames, slug = LIST_NAME, owner_screen_name = myname)
