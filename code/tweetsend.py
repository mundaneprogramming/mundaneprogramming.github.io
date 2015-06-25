from io import BytesIO
from os.path import basename, expanduser
from urllib.parse import urlsplit
import tweepy
import argparse
import json
import requests


DEFAULT_TWITTER_CREDS_PATH = '~/.creds/twit.json'

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
    fn = expanduser(credsfile)  # get the full path in case the ~ is used
    c = json.load(open(fn))
    # Get authentication token
    auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                               consumer_secret = c['consumer_secret'])
    auth.set_access_token(c['access_token'], c['access_token_secret'])
    # create an API handler
    return tweepy.API(auth)



def tweet(txt, in_reply_to_status_id = None,
                filename = None, credsfile = DEFAULT_TWITTER_CREDS_PATH):
    api = get_api(credsfile)
    if in_reply_to_status_id:
       in_reply_to_status_id = extract_tweet_id(in_reply_to_status_id)

    if filename:
        # We pass parameters to api.update_with_media()
        if is_http_url(filename):
            atts = get_remote_image(filename)
        else:
            atts = {"filename": filename, "file": None}
        ### now we send to twitter
        resp = api.update_with_media(status = txt,
            filename = atts['filename'],
            file = atts['file'],
            in_reply_to_status_id = in_reply_to_status_id)
    else:
        # do a normal
        resp = api.update_status(status = txt,
                        in_reply_to_status_id = in_reply_to_status_id)
    ######
    # return the response from Twitter
    return resp._json


def get_remote_image(imageurl):
    # returns a {filename: filename, file: bytes}
    d = {"filename": basename(imageurl)}
    resp = requests.get(imageurl)
    d['file'] = BytesIO(resp.content)
    return d


# http://stackoverflow.com/a/15713991/160863
def is_http_url(url):
    d = urlsplit(url)
    return 'http' in d.scheme


def extract_tweet_id(url):
    s = url.split('/status/')
    return s[1] if len(s) > 1 else url


parser = argparse.ArgumentParser()
parser.add_argument("text", nargs = 1, help = "Text to tweet")

parser.add_argument('--filename', '-f',
    help ='Specify a local filename or URL pointing to an image file')

parser.add_argument('--credsfile', '-c',
    default = DEFAULT_TWITTER_CREDS_PATH,
    help ='Specify a local filename containing Twitter credentials')

parser.add_argument('--reply-to', '-r',
    help ='ID or URL of Tweet in response to')


args = parser.parse_args()
text = args.text[0]
fname = args.filename if args.filename else None
creds = args.credsfile
r_id = args.reply_to
resp = tweet(text, filename = fname, credsfile = creds,
        in_reply_to_status_id = r_id)
j = json.dumps(resp, indent = 2)
print(j)




