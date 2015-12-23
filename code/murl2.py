from collections import OrderedDict
from datetime import datetime
from lxml.html import fromstring as html_fromstring
import re
import requests
import rtyaml
from argparse import ArgumentParser
import yaml

def get_page(url):
    response = requests.get(url)
    doc =  {'original_url': url,
            'final_url': response.url,
            'status_code': response.status_code,
            'text': response.text}
    if doc['text']:
        doc['html'] = html_fromstring(doc['text'])
    return doc

SELECTORS_CANONICAL_URL = OrderedDict()
SELECTORS_CANONICAL_URL['canonical_link'] = """link[@rel="canonical"]/@href"""
SELECTORS_CANONICAL_URL['og_url'] = """meta[@property="og:url"]/@content"""
SELECTORS_CANONICAL_URL['twitter_url'] = """meta[@property="twitter:url"]/@content"""

# expects dict containing {'html': lxml.html.HtmlElement}
# returns array of strings, each string a URL
def extract_canonical_urls(doc):
    html = doc['html']
    candidates = []
    candidates = OrderedDict()
    for key, sel in SELECTORS_CANONICAL_URL.items():
        selstring = "//head/%s" % sel
        selval = html.xpath(selstring)
        if selval:
            candidates[key] = str(selval[0])
    return candidates

SELECTORS_TITLE = OrderedDict()
SELECTORS_TITLE['og_title'] = """head/meta[@property="og:title"]/@content"""
SELECTORS_TITLE['twitter_title'] = """head/meta[@property="twitter:title"]/@content"""
SELECTORS_TITLE['itemprop_name'] = """head/meta[@itemprop="name"]/@content"""
SELECTORS_TITLE['head_title'] = """head/title/text()"""
SELECTORS_TITLE['h1#title'] = """body/h1[contains(@id, "title")]/text()"""
SELECTORS_TITLE['h1.title'] = """body/h1[contains(@class, "title")]/text()"""
SELECTORS_TITLE['first_h1'] = """body/h1[1]/text()"""


# expects dict containing {'html': lxml.html.HtmlElement}
def extract_titles(doc):
    html = doc['html']
    candidates = OrderedDict()
    for key, sel in SELECTORS_TITLE.items():
        selstring = "//%s" % sel
        selval = html.xpath(selstring)
        if selval:
            candidates[key] = str(selval[0])
    return candidates


SELECTORS_DESCRIPTION = OrderedDict()
SELECTORS_DESCRIPTION['og_description'] = """head/meta[@property="og:description"]/@content"""
SELECTORS_DESCRIPTION['meta_description'] = """head/meta[@name="description"]/@content"""
SELECTORS_DESCRIPTION['twitter_description'] = """head/meta[@property="twitter:description"]/@content"""
SELECTORS_DESCRIPTION['itemprop_description'] = """head/meta[@itemprop="description"]/@content"""
SELECTORS_DESCRIPTION['first.description'] = """body/*[contains(@class, "description")][0]/text()"""

def extract_descriptions(doc):
    print("hello")
    html = doc['html']
    candidates = OrderedDict()
    for key, sel in SELECTORS_DESCRIPTION.items():
        selstring = "//%s" % sel
        selval = html.xpath(selstring)
        if selval:
            candidates[key] = re.sub(r'\s+', ' ', str(selval[0])).strip()
    return candidates





SELECTORS_IMAGE_URL = OrderedDict()
SELECTORS_IMAGE_URL['og_image'] = """head/meta[@property="og:image"]/@content"""
SELECTORS_IMAGE_URL['twitter_image'] = """head/meta[@property="twitter:image"]/@content"""
SELECTORS_IMAGE_URL['itemprop_image'] = """head/meta[@itemprop="image"]/@content"""
# TODO: Get biggest first image from body
def extract_image_urls(doc):
    html = doc['html']
    candidates = OrderedDict()
    for key, sel in SELECTORS_IMAGE_URL.items():
        selstring = "//%s" % sel
        selval = html.xpath(selstring)
        if selval:
            candidates[key] = str(selval[0])
    return candidates


SELECTORS_PUBLISHED_AT = OrderedDict()
SELECTORS_PUBLISHED_AT['og_article_published_time'] = """head/meta[@property="article:published_time"]/@content"""
SELECTORS_PUBLISHED_AT['meta_article_published'] = """head/meta[@property="article:published"]/@content"""
SELECTORS_PUBLISHED_AT['item_prop_date_published'] = """head/meta[@itemprop="datePublished"]/@content"""
SELECTORS_PUBLISHED_AT['publish_date_or_time_class'] = """body/*[contains(@class, "publish") and (contains(@class, "date") or contains(@class, "time"))]/text()"""
SELECTORS_PUBLISHED_AT['time_tag'] = """body/time[0]/@content"""
SELECTORS_PUBLISHED_AT['time_or_date_class'] = """body/*[contains(@class, "time") or contains(@class, "date")][0]/text()"""

def extract_published_ats(doc):
    html = doc['html']
    candidates = OrderedDict()
    for key, sel in SELECTORS_PUBLISHED_AT.items():
        selstring = "//%s" % sel
        selval = html.xpath(selstring)
        if selval:
            candidates[key] = str(selval[0])
    # TODO extract from URL
    return candidates





def page_extractor(url):
    d = OrderedDict()
    doc = get_page(url)
    # attempt to find title
    candidate_titles = list(extract_titles(doc).values())
    if candidate_titles:
        d['title'] = candidate_titles[0]
    # attempt to get canonical URL
    d['url'] = doc['final_url']
    # attempt to find canonical URL
    candidate_urls = list(extract_canonical_urls(doc).values())
    if candidate_urls:
        d['url'] = candidate_urls[0]
    # attempt to find description
    candidate_descs = list(extract_descriptions(doc).values())
    if candidate_descs:
        d['description'] = candidate_descs[0]

    candidate_image_urls = list(extract_image_urls(doc).values())
    if candidate_image_urls:
        d['image_url'] = candidate_image_urls[0]


    candidate_published_ats = list(extract_published_ats(doc).values())
    if candidate_published_ats:
        d['published_at'] = candidate_published_ats[0]


    return d


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("url", help="The URL to fetch from")
    parser.add_argument("-f", "--format", default="yaml",
                        help="The file format: yaml, json, tsv, csv")

    args = parser.parse_args()
    url = args.url;
    # result_str = "Downloading " + args.url
    # if args.format:
    #     result_str += '\n\t--format: ' + args.format
    # print(result_str)
    d = page_extractor(url)
    # add retrieved_at
    d['retrieved_at'] = datetime.now().isoformat()
    print(rtyaml.dump(d))




"""
Attempts to extract the best versions of:

url:
title:
description:
image_url:
published_at:
modified_at:
publisher_name:
publisher_url:
domain:
authors:


murl --tsv tuda  # title author description url


"""
