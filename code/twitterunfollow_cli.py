import argparse
import tweepy
import os
import json

DEFAULT_TWITTER_CREDS_PATH = '~/.creds/me.json'

def get_api(credsfile = DEFAULT_TWITTER_CREDS_PATH):
    fn = os.path.expanduser(credsfile)  # get the full path in case the ~ is used
    c = json.load(open(fn))
    auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                               consumer_secret = c['consumer_secret'])
    auth.set_access_token(c['access_token'], c['access_token_secret'])
    return tweepy.API(auth)

# GREEN = '\033[92m'
# RED = '\033[91m'
# YELLOW = '\033[93m'
# END = '\033[0m'

TEMPLATE_TXT = """
\033[95m{name}, aka @{screen_name}\033[0m
{followers_count} followers, {friends_count} friends, {statuses_count} tweets
{description}
{last_tweet}
"""

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("filename", nargs = 1,
#         help = "Filename of friends.json to go through")
#     args = parser.parse_args()
#     filename = args.filename[0]
#     with open(filename) as f:
#         friends = json.loads(f.read())
#         print(len(friends), "friends found")
#         for friend in friends:
#             lasttwttxt = friend['status']['text'] if friend.get('status') else ""
#             friend_info = TEMPLATE_TXT.format(
#                 name = friend['name'], screen_name = friend['screen_name'],
#                 followers_count = friend['followers_count'],
#                 friends_count = friend['friends_count'],
#                 statuses_count = friend['statuses_count'],
#                 description = friend['description'],
#                 last_tweet = lasttwttxt)
#             print(friend_info)
#             # ask question
#             yn = input('\033[91m(Y/N)?:\033[0m ').strip().upper()
#             if yn[0] is 'Y':
#                 print('\033[91m', friend['screen_name'], 'unfollowed\033[0m')
#                 print("\n\n")
#                 # NOT IMPLEMENTED YET


if __name__ == "__main__":
    # No need to open a file
    api = get_api()
    cursor = tweepy.Cursor(api.friends, count = 100)
    for friends in cursor.pages():
        print("Getting batch of friends...")
        relations = api.lookup_friendships(user_ids = [f.id for f in friends])
        for idx, r in enumerate(relations):
            if not r.is_followed_by:
                friend = friends[idx]._json # get friend object

                lasttwttxt = friend['status']['text'] if friend.get('status') else ""
                friend_info = TEMPLATE_TXT.format(
                    name = friend['name'], screen_name = friend['screen_name'],
                    followers_count = friend['followers_count'],
                    friends_count = friend['friends_count'],
                    statuses_count = friend['statuses_count'],
                    description = friend['description'],
                    last_tweet = lasttwttxt)
                print(friend_info)
                # ask question
                yn = input('\033[91mDestroy friendship? (Y/N):\033[0m ').strip().upper()
                if yn and yn[0] is 'Y':
                    api.destroy_friendship(screen_name = friend['screen_name'])
                    print('\033[91m', friend['screen_name'], 'friendship DESTROYED\033[0m')
                    print("------------------")
                    # NOT IMPLEMENTED YET
