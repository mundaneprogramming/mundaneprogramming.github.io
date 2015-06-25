import tweepy
import os

### ENTER YOUR FILE HERE
DEFAULT_TWITTER_CREDS_PATH = '~/.creds/me.json'
# It should consist of a single dictionary and at a
# minimum have these fields:
# {
#     "access_token": "BLABHALHSRF7rkEALn621F3DdR1wpo0Rbq1VP",
#     "access_token_secret": "BLABLAHtTwZHOK8WOJ5Ec2Cxl3O8Dd73iJUPuQRF1f",
#     "consumer_secret": "BLABHALHSOCxfqYwDSdhdO2AzQ2K24hrlzJ805",
#     "consumer_key": "BLAHBLAHBLAHBLAH"
# }
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
    fname = os.path.expanduser(credsfile)  # get the full path in case the ~ is used
    c = json.load(open(fname))
    # Get authentication token
    auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                               consumer_secret = c['consumer_secret'])
    auth.set_access_token(c['access_token'], c['access_token_secret'])
    # create an API handler
    return tweepy.API(auth)


if __name__ == '__main__':
    import json
    print("Using default creds file:", DEFAULT_TWITTER_CREDS_PATH)
    print("Logging in...")
    api = get_api()
    me = api.me()._json
    print("Success! Logged in for user:", me['screen_name'])
    print("Printing data...")
    # print out the profile of the authenticated user
    print(json.dumps(me, indent = 2))
