from datetime import datetime
import argparse
import tweepy
import os
import json

DEFAULT_TWITTER_CREDS_PATH = '~/.creds/me.json'
MAX_COUNT_PER_BATCH = 200

def get_api(credsfile = DEFAULT_TWITTER_CREDS_PATH):
    fn = os.path.expanduser(credsfile)  # get the full path in case the ~ is used
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
    for tweet in cursor.items(MAX_COUNT_PER_BATCH):
        tweets.append(tweet._json)
    return tweets


def save_to_file(screen_name, tweets, path):
    # create a timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    basefn = "%s.tweets.%s.json" % (screen_name, timestamp)
    fn = os.path.join(path, basefn)
    # e.g. Saving to: dan.tweets.2015-06-20_2301.json
    print("Saving to:", fn)
    with open(fn, 'w') as f:
        data = json.dumps(tweets, indent = 2)
        f.write(data)



# command line time
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("screen_name", nargs = 1,
        help = "Screen name of user to get tweets from")
    parser.add_argument("--path", '-p',
        default = ".", help = "Path to save to")
    # Get screen name from commandline
    args = parser.parse_args()
    screen_name = args.screen_name[0]
    # Start the downloading process
    tweets = get_timeline(screen_name)
    # save the file
    save_to_file(screen_name, tweets, path = args.path)


