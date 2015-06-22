import tweepy
import json
from os import makedirs
from os.path import expanduser, exists, dirname
print("Welcome to this Twitter authorization convenience script")
print("--------------------------------------------------------")
print("If you haven't already, you need to create an app by visiting:")
print("    https://apps.twitter.com", "\n")
# Ask the user for a consumer token and secret
consumer_key = input("Consumer token: ").strip()
consumer_secret = input("Consumer secret: ").strip()
# start the authentication process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
print("1. Please visit the following URL in a browser:", "\n")
print(auth.get_authorization_url(), "\n")
print("2. Authorize the app.")
print("3. Leave the browser and come back here.")
pin = input('4. Copy and paste the 7-digit PIN here: ').strip()
token = auth.get_access_token(verifier = pin)
# Authentication is now successful
screen_name = auth.get_username()
# Let's remind the user who they authenticated as
print("Credentials successfully obtained for the user named:", screen_name)
# creating the creds object
d = {
    'consumer_key' : consumer_key,
    'consumer_secret' : consumer_secret,
    'access_token': token[0],
    'access_token_secret': token[1],
    'screen_name': screen_name
}
jdata = json.dumps(d, indent = 4)
# And then printing to screen, which is a little insecure
print(jdata)
# Now ask if user wants to write this to a file
print("Write to a file?")
yn = input('(Y/N)?: ').strip().upper()
if yn[0] is 'Y':
    defname = expanduser("~/.creds/%s.json" % screen_name.lower())
    print("Default filename is %s" % defname)
    # Get actual filename path
    fname = input("Filename (Leave blank for default): ").strip()
    if fname is '':
        fname = defname

    fname = expanduser(fname)
    if exists(fname):
        print("%s exists, file NOT saved" % fname)
    else:
        print("Writing creds to:", fname)
        makedirs(dirname(fname), exist_ok = True)
        with open(fname, 'w') as f:
            f.write(jdata)
