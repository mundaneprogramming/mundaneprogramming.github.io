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


### Verify the row count

~~~py
from glob import glob
from xlrd import open_workbook
for xlsname in glob('*.xls'):
  book = open_workbook(xlsname)
  sheet = book.sheets()[0]
  print(xlsname, 'has', sheet.nrows, 'rows')  
~~~

Looks good. Sometimes agencies have the annoying practice of using the first spreadsheet as a sort of coversheet, which would require doing a for-loop within a for-loop to iterate through each sheet of `book.sheets()`. 

However, the CDE does something pretty annoying: the header rows are not always on the top row.

Coming from Ruby, the way Python does list/array operations is absolutely baffling to me. [So this is good practice](http://stackoverflow.com/questions/9868653/find-first-list-item-that-matches-criteria):

~~~py
for xlsname in glob('*.xls'):
  book = open_workbook(xlsname)
  sheet = book.sheets()[0]
  header_idx = next(i for i in range(10) if all(j in str(sheet.row_values(i)) for j in ['County', 'District', 'Score', 'Name']))
  
  print(xlsname, 'has headers at:', header_idx) 
~~~

Bad guess; there's something wrong with `sat08.xls`

~~~
sat06.xls has headers at: 2
sat07.xls has headers at: 2
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-56-cf67c3a843f1> in <module>()
      2   book = open_workbook(xlsname)
      3   sheet = book.sheets()[0]
----> 4   header_idx = next(i for i in range(10) if all(j in str(sheet.row_values(i)) for j in ['County', 'District', 'Score', 'Name']))
      5 
      6   print(xlsname, 'has headers at:', header_idx)

StopIteration: 
~~~


Its headers:

~~~
"County
Number" "District
Number" "School
Number" County Name District Name School Name "Grade 12
Enrollment" "Number
Tested" "Percent
Tested" "
Critical Reading
Average"  "
Math
Average"  "
Writing
Average"  "
Total
Average"  "Total
>=1500 Number"  "Total
>=1500 Percent"
~~~


OK, try again:

~~~py
for xlsname in glob('*.xls'):
  book = open_workbook(xlsname)
  sheet = book.sheets()[0]
  header_idx = next(i for i in range(10) if all(j in str(sheet.row_values(i)) for j in ['County', 'District', 'Name']))
  
  print(xlsname, 'has headers at:', header_idx) 
~~~


### Reconciling the formats

This will be the hardest part of the show.












