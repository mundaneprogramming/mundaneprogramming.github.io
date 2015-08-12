# Download friends or followers
from datetime import datetime
import argparse
import tweepy
import os
import json

DEFAULT_TWITTER_CREDS_PATH = '~/.creds/me.json'
BATCH_SIZE = 100

def get_api(creds_path):
    fn = creds_path
    c = json.load(open(fn))
    auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                               consumer_secret = c['consumer_secret'])
    auth.set_access_token(c['access_token'], c['access_token_secret'])
    # The wait_on_rate_limit parameters let the API handler sleep
    #   upon hitting a wait limit, and then to automatically continue
    api = tweepy.API(auth,
            wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    return api


# This program gets: ids of the given user's friends or followers
#    then: it uses users/lookup to look up those names in batches
# We use followers/ids and friends/ids instead of
#    followers/list or friends/list because of the stricter API limits
#    in the latter API calls
# https://dev.twitter.com/rest/reference/get/followers/list
# https://dev.twitter.com/rest/reference/get/followers/ids
# https://dev.twitter.com/rest/reference/get/users/lookup



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("screen_name", nargs = 1,
        help = "Screen name of user to get tweets from")
    parser.add_argument("users_type", nargs = 1,
        help = "'friends' or 'followers' to collect")
    parser.add_argument("--output-path", '-o', help = "Path to save to")
    parser.add_argument("--creds-path", '-c', help = "Path to a JSON file that has Twitter creds",
            default = DEFAULT_TWITTER_CREDS_PATH
        )
    # Get screen name from commandline
    args = parser.parse_args()
    screen_name = args.screen_name[0]
    users_type = args.users_type[0]
    creds_path = os.path.expanduser(args.creds_path)
    # talk to the API
    api = get_api(creds_path)
    # Start the downloading process
    if users_type == 'friends':
        foo = api.friends_ids
    elif users_type == 'followers':
        foo = api.followers_ids
    else:
        raise Exception("users_type must be `friends` or `followers`")
    user_ids = []
    cursor = tweepy.Cursor(foo, screen_name = screen_name).pages()
    while True:
        try:
            page = cursor.next()
            user_ids.extend(page)
        except StopIteration:
            break
        except tweepy.error.TweepError as e:
            print(e)
            break
        else:
            print("Collected", len(user_ids), " IDs")

    # too lazy to catch invalid input here, meh
    # now get the profiles
    profiles = []
    for x in range(0, len(user_ids), BATCH_SIZE):
        batch_uids = user_ids[x:x+BATCH_SIZE]
        try:
            results = api.lookup_users(batch_uids)

        # catch situation in which none of the names in the batch are found
        # or else Tweepy will error out
        except tweepy.error.TweepError as e:
            if e.response.status_code == 404:
                pass
            else:
                # some other error, print the exception and
                # save what we can
                print(e)

        else:
            profiles.extend([user._json for user in results])
            print("User profiles collected:", len(profiles))

    # Now save the file
    fn = args.output_path if args.output_path else "%s.%s.json" % (screen_name, peeps_type)
    with open(fn, "w") as f:
        print("Writing to:", fn)
        data = json.dumps(profiles, indent = 2)
        f.write(data)
