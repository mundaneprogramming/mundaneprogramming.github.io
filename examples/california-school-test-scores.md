---
title: California test scores
description: A mini-project to collect California school data, using a variety of mundane programming scripts and libraries.
---

### Step 1. Download the webpage


~~~py
import requests
CDE_URL = 'http://www.cde.ca.gov/ds/sp/ai/'
rawhtml = requests.get(CDE_URL).text
~~~


### Step 2. Extract the links

~~~py
from lxml import html
doc = html.fromstring(rawhtml)
links = doc.cssselect('a')
~~~

### Step 3. Extract only the Excel links

~~~py
xlslinks = [link for link in links if 'xls' in str(link.attrib.get('href'))]
~~~


There are 45 links

~~~py
len(xlslinks)
# 45
~~~


### Step 4. Create absolute from relative links

All of the links are relative:

~~~py
for x in xlslinks:
  print(x.attrib['href'])
~~~

~~~
documents/sat13.xls
documents/sat12.xls
documents/sat11.xls
...
documents/ap01.xls
documents/ap00.xls
documents/ap99.xls
~~~

~~~py
from urllib.parse import urljoin
urls = [urljoin(CDE_URL, x.attrib['href']) for x in xlslinks]
~~~

### Step 5. Downloading the links

~~~py
from os.path import basename
for url in urls:
  with open(basename(url), "wb") as f:
    print("Downloading", url)
    f.write(requests.get(url).content)
~~~


## Organizing the files

~~~py
from glob import glob
from xlrd import open_workbook
for xlsname in glob('*.xls'):
  book = open_workbook(xlsname)
  sheet = book.sheets()[0]
  print(xlsname, 'has', sheet.nrows, 'rows')
  print(sheet.row_values(2))
  
~~~



















