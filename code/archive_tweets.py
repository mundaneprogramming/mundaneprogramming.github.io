#!/usr/bin/env python

import os

import tweepy
import dataset

class InsertBuffer(object):
    def __init__(self, table, size=1000):
        self._table = table
        self._size = size
        self._buffer = []

    def flush(self):
        self._table.insert_many(self._buffer)
        self._buffer = []

    def insert(self, d):
        self._buffer.append(d)
        if len(self._buffer) >= self._size:
            self.flush()


if __name__ == "__main__":
    auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'],
        os.environ['TWITTER_CONSUMER_SECRET'])
    auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'],
        os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    db = dataset.connect('sqlite:///amc2015_tweets.db')

    table = db['tweets']
    insert_buffer = InsertBuffer(table, 1000)

    result = db.query('SELECT MAX(id) as max_id FROM tweets')
    row = result.next()
    max_id = row['max_id']

    search_query = "#amc2015"
    search_kwargs = {
        'q': search_query,
        'rpp': 100,
    }
    if max_id is not None:
        search_kwargs['since_id'] = max_id
    cursor = tweepy.Cursor(api.search, **search_kwargs)

    for status in cursor.items():
        record = dict(
            id=status.id,
            user__screen_name=status.user.screen_name,
            user__name=status.user.name,
            text=status.text,
            created_at=status.created_at)
        print(status.id, status.text)
        insert_buffer.insert(record)
    
    insert_buffer.flush()
