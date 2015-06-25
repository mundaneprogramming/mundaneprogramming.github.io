---
title: Archive tweets 
authors:
  - geoffhing
description: |
  Archive tweets with a certain hashtag to a database  
files:
  - name: code/archive_tweets.py
    description: |
      Hits the Twitter search endpoint and returns
---

## Introduction

I was asked for a quick and dirty solution to archiving tweets for a [conference](http://amc2015.alliedmedia.org/) hashtag.

## Do it yourself

I quickly explored a number of opensource solutions for archiving tweets and found them to either be complicated to configure or set up the environment, make assumptions that didn't fit my use case, seemed broken.

To decide if it was worth investigating these solutions further, or just rolling my own thing quickly, I tried to break the problem into its parts to see if I could wrap my head around it:

* Get tweets for a hashtag from Twitter's API
* Filter to only tweets I hadn't seen before
* Write the new tweets to a database

This seemed doable, so onward!

## Explore the API

I had a vague sense that there was some kind of API endpoint for getting tweets with a particular hashtag. After poking around the [API docs](https://dev.twitter.com/rest/), I found the [search endpoint](https://dev.twitter.com/rest/public/search) was probably what I wanted.

I also learned that the second aspect of my problem, only retrieving tweets I hadn't seen before,  was [handled by setting a since_id parameter when making a request](https://dev.twitter.com/rest/public/timelines).

You can retrieve tweets for a particular hashtag by requesting a URL like:

~~~
https://api.twitter.com/1.1/search/tweets.json?q=%23amc2015
~~~

I tried to take a look at this URL in my browser, but got a JSON response with a "Bad Authentication data." 

Luckily, Twitter has an [API console](https://dev.twitter.com/rest/tools/console) that handles the authnetication pieces for you and lets you quickly examine response data. This process also reminded me that I would have to consider authentication and maybe generate some kind of credentials as part of my solution.

## A little help from my friends

I had previously used the awesome [dataset](https://dataset.readthedocs.org/) package for database interactions and knew that would probably work well for saving data for tweets.

I figured there were a number of Python packages for interacting with Twitter's API, and it turns out that [there are many](https://dev.twitter.com/overview/api/twitter-libraries).

It's easy to get analysis paralysis when picking libraries.  Don't.  Just pick one and go with it.  Even if it's a little rocky, you'll learn something about how the library author designs software and be able to make a different choice next time.  Or you an ask a friend what they've used successfully.

## RTFD

[@aepton](http://twitter.com/aepton) told me to use [tweepy](http://tweepy.org/), so I dove into the [documentation](http://docs.tweepy.org/) and discovered the [search method](http://docs.tweepy.org/en/v3.2.0/api.html#API.search) wrapped the endpoint I needed and handle only getting unseen tweets. It also provided a clean interface for paging when there were a large number of tweets.

## Putting it all together

With my newfound knowledge of the API and code snippets from the tweepy docs, I was able to write a simple script that hit the API and wrote the responses to a SQLite database.
