import csv
import re

STOPWORDS = ""

username = 'andymboyle'
fname = 'tweets.csv'
f = open(fname)
tweets = csv.DictReader(f)

d = {'mentions': [], 'retweets': [] }

for tweet in tweets:
    txt = tweet['text'].lower()
    if username in txt:
        if re.search("rt @%s\\b" % username, txt):
            d['retweets'].append(tweet)
        else:
            d['mentions'].append(tweet)

print("Total tweets with %s: " % username, len(d['mentions']) + len(d['retweets']))
print("Total mentions:", len(d['mentions']))
print("Total retweets:", len(d['retweets']))

f.close()



def tokenize_tweet_text(txt):
