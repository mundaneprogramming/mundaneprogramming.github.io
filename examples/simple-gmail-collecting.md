---
title: Count up your GMails with Python
authors:
  - dannguyen
description: |
  Gather up and filter your emails programmatically.
---

This only works with Python 2.x. However, it's easier than trying to figure out Google's currently scattered and inconsistent documentation of the [google-api-python-client](https://github.com/google/google-api-python-client).

### Step 1: Manually download charliergo/gmail

__Important:__ Don't confuse [charliegro/gmail](https://github.com/charlierguo/gmail) with the [gmail package currently on pypy](https://pypi.python.org/pypi/gmail/0.1). If you follow the instructions on [charliegro's repo](https://github.com/charlierguo/gmail), you can just manually `git clone` his repo into your working folder:

~~~sh
mkdir -p /tmp/hey
cd /tmp/hey
git clone git://github.com/charlierguo/gmail.git
~~~

### Step 2: Create an application-specific one-time GMail passkey

Go here to make an __App password__: [https://security.google.com/settings/security/apppasswords](https://security.google.com/settings/security/apppasswords)

The above URL will walk you through the steps to generate (for your logged in Google account) a one-time all-powerful password that you can supply to the Python Gmail client (and then easily revoke, because more all-powerful passwords mean more chances for all-powerful-screwups). 

The password generation looks something like this:

![image](files/images/googleapppassword.png)




Quoting from the instructions:

> Go to the settings for your Google Account in the application or device you are trying to set up. Replace your password with the 16-character password shown above. Just like your normal password, this app password grants complete access to your Google Account. You won't need to remember it, so don't write it down or share it with anyone


__Important:__ After playing around with the GMail python client, I recommend __revoking the App password__ that you just created. It's not ideal to have all-powerful passwords lying around.


### Step 3: Enter iPython land

To authenticate:

~~~py
import gmail
g = gmail.login('you@gmail.com', 'karcdcarzzzaexxx')
~~~

To collect messages across all your mailboxes (i.e. inbox, archive, spam, etc):

~~~py
import datetime
# all messages from a user, within the last 2 years
msgs = g.all_mail().mail(fr = "mybestfriend@gmail.com", 
                          after=datetime.date(2013, 7, 1))

# msgs is a list
print(len(msgs))
# 42                          
~~~

The `mail()` function only retrieves message IDs. You have to manually fetch them to get access to the `body`, `to`, `fr`, etc. attributes:

~~~py
for i, m in enumerate(msgs):
    print("Getting message: ", i)
    m.fetch()
    print(m.body)
~~~


Check the [official docs for more ways to filter emails](https://github.com/charlierguo/gmail#filtering-emails):
