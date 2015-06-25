# just fetches the spreadsheets from the California site
import re
import os.path
import requests
from urllib.parse import urljoin
from lxml import html
from os import makedirs

XLS_DIR = "./data-hold/xls/immunization"
INDEX_URL = "http://www.cdph.ca.gov/programs/immunize/pages/immunizationlevels.aspx"
makedirs(XLS_DIR, exist_ok = True)
# Download the HTML listing
response = requests.get(INDEX_URL)
doc = html.fromstring(response.text)
all_urls = doc.xpath('//a[contains(@href, "Kinder") and contains(@href, "xls")]/@href')
for url in all_urls:
    y1, y2 = re.search('(\d{2})-(?:\d{2})?(\d{2})', url).groups()
    # y1 and y2 are the 2 digit years
    ext = os.path.splitext(url)[1]

    # Now rename to a proper year
    # e.g. ./data-hold/xls/K--2005-2006.xls
    oname = os.path.join(XLS_DIR, "K--20{0}-20{1}{2}".format(y1, y2, ext))
    full_url = urljoin(INDEX_URL, url)
    print("Downloading:\n {0}\n into: {1}".format(full_url, oname))

    # Sample output:
    # Downloading:
    #  http://www.cdph.ca.gov/programs/immunize/Documents/2007-2008%20CA%20Kindergarten%20Data.xls
    #  into: ./data-hold/xls/K--2007-2008.xls
    xlsfile = requests.get(full_url)
    with open(oname, 'wb') as ofile:
         ofile.write(xlsfile.content)
