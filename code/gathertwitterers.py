import requests
import re

NOT_USERNAMES = ['share', 'i']
# pic.twitter.com/bNPEaYYJaE
# platform.twitter.com/widgets.js
#
def regex_twitter_accounts_from_page(url):
    txt = requests.get(url).text
#    return re.findall('twitter.com/(\w+)', txt)
    usernames = re.findall(r'https?://(?:www\.)?twitter.com/@?(\w+)/?["\']', txt)
    usernames.extend(re.findall(r'https?://(?:www\.)?twitter.com/intent/user\?screen_name=(\w+)', txt))
    usernames = set(u.lower() for u in usernames)
    return [u for u in usernames if u not in NOT_USERNAMES]

# fatally flawed
def css_select_twitter_accounts_from_page(url):
    doc = html.fromstring(requests.get(url).text)
    usernames = []
    hrefs = [a.attrib['href'] for a in doc.cssselect('a') if a.attrib.get('href')]
    for href in hrefs:
        if 'twitter.com/' in href:
            if 'screen_name=' in href:
                u = href.split('screen_name=')[1]
            else:
                x = href.split('twitter.com/')
                if len(x) < 2: # e.g. https://twitter.com/
                    continue
                else:
                    u = x[1].split('/')[0].replace('@', '')
            usernames.append(u)
    usernames = set(u.lower() for u in usernames)
    return [u for u in usernames if u not in NOT_USERNAMES]


def xpath_select_twitter_accounts_from_page(url):
    doc = html.fromstring(requests.get(url).text)
    usernames = []
    hrefs = doc.xpath('//a[contains(@href, "twitter.com/")]/@href')
    for href in hrefs:
        if 'screen_name=' in href:
            u = href.split('screen_name=')[1]
        else:
            x = href.split('twitter.com/')
            if len(x) < 2: # e.g. https://twitter.com/
                continue
            else:
                u = x[1].split('/')[0].replace('@', '')
        usernames.append(u)
    usernames = set(u.lower() for u in usernames)
    return [u for u in usernames if u not in NOT_USERNAMES]



def regex_xpath_twitter_accounts_from_page(url):
    doc = html.fromstring(requests.get(url).text)
    usernames = []
    hrefs = doc.xpath('//a[contains(@href, "twitter.com/")]/@href')

    for h in hrefs:
        if 'screen_name=' in h:
            u = re.search('(?<=screen_name=)\w+', h).group()
        else:
            m = re.search(r'https?://(?:www\.)?twitter.com/@?(\w+)/?$', h)
            if m:
                u = m.groups()[0]
            else:
                continue
        usernames.append(u)
    usernames = set(u.lower() for u in usernames)
    return [u for u in usernames if u not in NOT_USERNAMES]


for url in ['http://www.washingtonpost.com', 'http://srccon.org/sessions', 'http://www.propublica.org', 'http://mashable.com', 'http://twitter.com']:
    print(url)
    print(len(regex_twitter_accounts_from_page(url)))
    print(len(css_select_twitter_accounts_from_page(url)))
    print(len(xpath_select_twitter_accounts_from_page(url)))
    print(len(regex_xpath_twitter_accounts_from_page(url)))
