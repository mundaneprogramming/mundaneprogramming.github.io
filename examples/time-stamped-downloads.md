---
title: Timestamp and organize downloaded files
description: "Not quite as good as git, but better than hand-naming files yourself."
featured: true
the_routine:
  - Open the web browser.
  - Visit a URL.
  - Save/Download the URL to your `Downloads/` folder.
  - Move it to a subfolder so that `Downloads/` doesn't get cluttered.
  - Rename it to a time or a version number, e.g. `example.com.html (1)` and `example.com.html (2)`.
rank: 2
related_links:
  - title: Falsehoods programmers believe about time
    url: http://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time
---


# The problem with time

If you're new to programming, chances are, you are new to the concept of how damn complex time can be. Not just the complicated ways in how humans struggle with time, e.g. *"is 10:30PM too late to call someone on a weeknight"*, but the ways that computers from different parts of the world (or solar system) need to coordinate with each other to the millisecond, including the hashing out of different time zones, daylight savings time, time formats (e.g. European vs. American) and leap years/seconds.

Check out Noah Sussman's classic writeup, ["Falsehoods programmers believe about time"](http://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time) for more complexities.

I can say with only slight exaggeration that learning how a language deals with time is almost always the most painful part of learning a new language (or framework) for me. I haven't quite mastered the array of Python's time libraries and objects, including [time](https://docs.python.org/3/library/time.html), [datetime](https://docs.python.org/3/library/datetime.html), [calendar](https://docs.python.org/3.5/library/calendar.html), [tzinfo](https://docs.python.org/3.5/library/datetime.html#tzinfo-objects), [timezone](https://docs.python.org/3.5/library/datetime.html#timezone-objects), [timedelta](https://docs.python.org/3.5/library/datetime.html#timedelta-objects). And judging by the equally numerous third-party packages created to make time-handling easier &ndash; [pytz](https://pypi.python.org/pypi/pytz/), [arrow](http://crsmithdev.com/arrow/), [dateutil](https://labix.org/python-dateutil), [moment](https://github.com/zachwill/moment), [delorean](http://delorean.readthedocs.org/en/latest/index.html) &ndash; I'm guessing many users also find it difficult.

So the more you can practice working with time, _gradually_, the less insane you'll become when programming time functions on deadline.

# Python libraries and functions

For this example, we'll need the libraries and functions for downloading files, creating new directories and files, and keeping track of time.

## `os.makedirs()`  

Make a directory, including any intermediary subdirectories:

~~~py
import os
os.makedirs("/tmp/lah/dee/dah", exist_ok = True)
~~~


## `os.path.join()`

Given an array of strings, create a directory path. I know you're thinking, _duh, why do I need a function to do something as easy as_ `"some" + "/" + "path.html"`...trust me, you want to leave the details up to the Python library:

~~~py
import os
os.path.join("hey", "you", "index.html")
# 'hey/you/index.html'
os.path.join("hey/", "you/", "index.html")
# 'hey/you/index.html'
~~~

## `urllib.parse.urlparse`

We just need this to parse a given URL to get its host/domain, i.e. its `netloc`.

~~~py
from urllib.parse import urlparse
u = urlparse("http://www.example.com/some/path.html?hello=world&a=apples")
u.scheme
# 'http'
u.netloc
# 'www.example.com'
u.path
# '/some/path.html'
u.query
# 'hello=world&a=apples'
~~~

## `re`

~~~py
import re
re.sub("\W", '_', "http://www.example.com/some/path.html?hello=world&a=apples")
# 'http___www_example_com_some_path_html_hello_world_a_apples'
~~~


## The Requests package

This is the only external library we'll use; [Requests](http://docs.python-requests.org/en/latest/) is so popular that it's pretty much ubiquitous anyway.

~~~py
import requests
requests.get("http://www.example.com/some/path.html?hello=world&a=apples")
~~~



## `datetime` 

The [__datetime__ package](https://docs.python.org/3/library/datetime.html) is part of Python's standard library, and its [__datetime__ object](https://docs.python.org/3/library/datetime.html#datetime-objects) is all we need to make timestamps.

~~~py
from datetime import datetime
~~~

### `now()` versus `utcnow()`

OK, so if you read the list of [`datetime` class methods](https://docs.python.org/3/library/datetime.html#datetime-objects), you might be confused at the seemingly similar functions of `today()`, `now()`, and `utcnow()`. The differences essentially involve the concept of _time zones_, and whether or not you want a datetime object that is "aware" of its timezone.

Rather than get into that mess, let's just stick to using [__utcnow()__](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow), which works like this:

~~~py
d = datetime.utcnow()
print(d) 
# 2015-07-11 19:04:56.039051
d
# d is a datetime.datetime object:
# datetime.datetime(2015, 7, 11, 19, 4, 56, 39051)
~~~

The `utcnow()` function returns the current date and time as it is according to the standard of [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) (which is similar but not quite exactly the same as [Greenwich time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time)).

I ran the above function at around 12PM in California, i.e. [Pacific Standard Time](https://en.wikipedia.org/wiki/Pacific_Time_Zone), which is __7 hours__ behind UTC, hence, why the __hour__ part of the result is `19` instead of `12`.

In other words, if I had used the [__now()__ function](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow), I would've gotten this:

~~~py
datetime.now()
# datetime.datetime(2015, 7, 11, 12, 4, 56, 39051)
~~~

Since I'm saving files to my _own_ computer, wouldn't it make more sense to use its timezone, so that when glancing at a file list, I don't have to mentally offset the time to see when I actually downloaded the files?
