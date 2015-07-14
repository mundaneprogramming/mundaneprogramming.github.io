#!/usr/bin/env python3
from datetime import datetime
import requests
import sys
import newspaper
from collections import defaultdict
from colorama import Fore, Style, Back, init as initcolorama
from urllib.parse import urljoin

TEMPLATE ="""
{a}title{b}: {title}
{a}site_name{b}: {site_name}
{a}url{b}: {url}
{a}retrieved_at{b}: {retrieved_at}
{a}description{b}: |
{a}{description}
{a}date{b}: {date}
{a}type{b}: {type}
{a}authors{b}: {authors}
{a}image{b}: {image}
{a}icon{b}: {icon}
"""
initcolorama()
url = sys.argv[1]

article = newspaper.Article(url)
article.download()
article.parse()
# prioritize og first
og = defaultdict(str, article.meta_data['og'])
mdata = defaultdict(str, article.meta_data)
d = defaultdict(str)
for att in ["title", "description",  "type", "site_name", "url"]:
    if og[att]:
        d[att] = og[att]
    elif hasattr(article, att):
       d[att] = article.__getattribute__(att)


d["image"] = article.meta_img
d["authors"] =  next((x for x in [mdata['authors'], mdata['author'], article.authors] if x), "")


article.authors if article.authors else ""
d["date"] = article.publish_date
d["description"] = "\n".join(["\t" + line for line in d["description"].splitlines()])

# if no site_name
if not d["site_name"]:
    try:
        _xart = newspaper.Article(article.source_url)
        _xart.download()
        _xart.parse()
        d["site_name"] = _xart.title
    except Exception as e:
        d['site_name'] = article.source_url



# get the favicon
if article.meta_favicon:
    d["icon"] = urljoin(d["url"], article.meta_favicon)
else:
    # attempt site level icon
    icourl = article.source_url + "/favicon.ico"
    try:
        resp = requests.head(icourl)
        if resp.status_code == 200:
            d['icon'] = urljoin(d["url"], icourl)
    except requests.exceptions.RequestException as e:
        pass # fail silently



# meta data
d['retrieved_at'] = datetime.utcnow().isoformat()
d['a'] = Fore.RED + Style.BRIGHT
d['b'] = Style.RESET_ALL



print(TEMPLATE.format(**d))
