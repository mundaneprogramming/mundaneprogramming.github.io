https://docs.google.com/spreadsheets/u/0/d/1RqfFUqsSlrYEVFzqEGUJeDO6LBLcKjmmlpBduQuTh0g/export?format=csv&gid=0


~~~py
import requests
import csv
url = "https://docs.google.com/spreadsheets/u/0/d/1RqfFUqsSlrYEVFzqEGUJeDO6LBLcKjmmlpBduQuTh0g/export?format=csv&gid=0"
LOCAL_FNAME = "./_data/mundane_todos.csv"
# save it first
with open(LOCAL_FNAME, 'w') as f:
  f.write(requests.get(url).text)
  


~~~
