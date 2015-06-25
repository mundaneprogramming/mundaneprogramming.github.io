# Download friends or followers
from datetime import datetime
import argparse
import tweepy
import os
import json

DEFAULT_TWITTER_CREDS_PATH = '~/.creds/me.json'
BATCH_SIZE = 100

def get_api():
    fn = os.path.expanduser(DEFAULT_TWITTER_CREDS_PATH)
    c = json.load(open(fn))
    auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                               consumer_secret = c['consumer_secret'])
    auth.set_access_token(c['access_token'], c['access_token_secret'])
    return tweepy.API(auth)

def get_5000_friends_ids(screen_name):
    api = get_api()
    return api.friends_ids(screen_name, count = 5000)

# breaking the DRY rule
def get_5000_followers_ids(screen_name):
    api = get_api()
    return api.followers_ids(screen_name, count = 5000)

# gets a whole bunch of profile information from a batch of user IDs
# We don't use followers/list or friends/list because of the stricter API limits
# https://dev.twitter.com/rest/reference/get/followers/list
# compared to followers/ids and users/lookup
# https://dev.twitter.com/rest/reference/get/followers/ids
# https://dev.twitter.com/rest/reference/get/users/lookup
def get_profiles_from_ids(user_ids):
    api = get_api()
    batch_size = 100
    profiles = []
    for x in range(0, len(user_ids), BATCH_SIZE):
        print("Batch:", x)
        batch_uids = user_ids[x:x+BATCH_SIZE]
        for user in api.lookup_users(batch_uids):
            profiles.append(user._json)

    return profiles



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("screen_name", nargs = 1,
        help = "Screen name of user to get tweets from")
    parser.add_argument("peeps_type", nargs = 1,
        help = "'friends' or 'followers' to collect")
    parser.add_argument("--path", '-p',
        default = ".", help = "Path to save to")
    # Get screen name from commandline
    args = parser.parse_args()
    screen_name = args.screen_name[0]
    peeps_type = args.peeps_type[0]

    # Start the downloading process
    if peeps_type == 'friends':
        userids = get_5000_friends_ids(screen_name)
    elif peeps_type == 'followers':
        userids = get_5000_followers_ids(screen_name)
    # too lazy to catch invalid input here, meh
    # now get the profiles
    profiles = get_profiles_from_ids(userids)
    fn = "%s.%s.json" % (screen_name, peeps_type)
    with open(fn, "w") as f:
        print("Writing to:", fn)
        data = json.dumps(profiles, indent = 2)
        f.write(data)
