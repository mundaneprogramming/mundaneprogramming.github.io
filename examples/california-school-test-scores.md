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

e.g.

~~~
documents/sat13.xls
documents/sat12.xls
documents/sat11.xls
...
documents/ap01.xls
documents/ap00.xls
documents/ap99.xls
~~~

This reflects how the links exist in the raw HTML:

~~~html
<li><a href="documents/sat02.xls">SAT 2001–02</a> &nbsp;(XLS; Revised 04-Jun-2009)</li>
~~~

If you click that _relative_ link via a web browser, the browser correctly concatenates it to the URL of the current page:

`http://www.cde.ca.gov/ds/sp/ai/<strong>documents/sat02.xls</strong>`

However, since we're in Python-land, we have no such convenience. We have to manually join the two strings. It's an easy enough pattern. But I recommend looking up the __urljoin()__ function, which can handle this simple scenario as well as edge cases that you'll encounter in the wilder Web:


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


### Rename the files

~~~py
import re
import os
import glob
from os.path import splitext, dirname, basename
RAWDATA_PATH = './rawdata'
os.makedirs(RAWDATA_PATH, exist_ok = True)
for xlsname in glob('*.xls'):
  bname, ext = splitext(basename(xlsname)) # sat99, xls
  tname, yr = re.search('([a-z]+)(\d{2})', bname).groups() # 99
  year = ("19%s" % yr) if int(yr) > 90 else ("20%s" % yr)
  newname = os.path.join(RAWDATA_PATH, "%s-%s%s" % (tname, year, ext))
  os.rename(xlsname, newname)
  print(xlsname, 'to:', newname)
~~~





### Verify the row count

~~~py
from glob import glob
from xlrd import open_workbook
RAWDATA_PATH
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
  header_idx = next(i for i in range(10) 
    if all(j in str(sheet.row_values(i)) 
    for j in ['County', 'District', 'Name']))
  hdrs = sheet.row_values(header_idx)
  print('%s has %d headers on row %d:' %(xlsname, len(hdrs), header_idx))
~~~


## Reconciling the formats

This will be the hardest part of the show.

### Make new text files

~~~py
import csv
import re
from os.path import splitext
for xlsname in glob('*.xls'):
  bname = splitext(basename(xlsname))[0] # sat99
  yr = int(re.search('\d{2}', bname).group()) # 99
  f = open('result.csv', 'wb')
  cwriter = (fp, quoting=csv.QUOTE_ALL)

  book = open_workbook(xlsname)
  sheet = book.sheets()[0]
  header_idx = next(i for i in range(10) 
    if all(j in str(sheet.row_values(i)) 
    for j in ['County', 'District', 'Name']))
  hdrs = sheet.row_values(header_idx)
  print('%s has %d headers on row %d:' %(xlsname, len(hdrs), header_idx))

~~~












----------

~~~py
from collections import defaultdict
testheaders = defaultdict(lambda: defaultdict(list))
for t in ['sat', 'act', 'ap']: 
  d = testheaders[t] # e.g. {'ap': []}
  for xlsname in glob(t + '*.xls'):
    book = open_workbook(xlsname)
    sheet = book.sheets()[0]
    header_idx = next(i for i in range(10) if 
        all(j in str(sheet.row_values(i)) 
        for j in ['County', 'District', 'Name']))
    )]
    d[tuple(heads)].append(xlsname)
~~~



#### Clean up the headers

Change:

~~~py
['County\nNumber', 'District\nNumber', 'School\nNumber', 'County Name', 'District Name', 'School Name', 'Grade 12\nEnrollment', 'Number\nTested', 'Percent\nTested', 'Average\nScore', 'Number\n w/Score\n>=21', 'Percent\nw/Score\n>=21']
~~~

to:

~~~py
('County Number', 'District Number', 'School Number', 'County Name', 'District Name', 'School Name', 'Grade 12', 'Number Tested', 'Percent Tested', 'Average Score', 'Scor21Ct', 'PctScr21')
~~~



~~~py
import re
def fooey(tup):
  return tuple([re.sub('\s+', ' ', h).strip() for h in tup])

for d in testheaders.values():
  d = {fooey(k): v for k, v in d.items()}

# clean up the headers, remove internal newlines
~~~


#### Create JSON-friendly structure

(unnecessary)

And to get a feel for how that looks:

~~~py
import json
jheaders = {c: {str(k): v for k, v in d.items()} 
                    for c, d in testheaders.items()}
print(json.dumps(jheaders, indent = 2))
~~~






#### ACT data

Let's start with the easiest data; ACT test files have a uniform number of columns: 12. And over the 15 years, there's only two variations of how the columns are named.

~~~py
act_cols = [list(cols) for cols in testheaders['act'].keys()]
maxcols = max(len(cols) for cols in act_cols)
for i in range(maxcols):
  colnames = [cols[i] if len(cols) >= i else None for cols in act_cols]
  print(colnames)
~~~

~~~py
['County Number', 'County Number']
['District Number', 'District Number']
['School Number', 'School Number']
['County Name', 'County Name']
['District Name', 'District Name']
['School Name', 'School Name']
['Grade 12 Enrollment', 'Grade 12']
['Number Tested', 'Number Tested']
['Percent Tested', 'Percent Tested']
['Average Score', 'Average Score']
['Number w/Score >=21', 'Scor21Ct']
['Percent w/Score >=21', 'PctScr21']
~~~



### Generalize


~~~py
def fooheads(tname):
  tcols = [list(cols) for cols in testheaders[tname].keys()]
  maxcols = max(len(cols) for cols in tcols)
  for i in range(maxcols):
    colnames = [cols[i] if len(cols) > i else None for cols in tcols]
    print(colnames)
~~~



----------------



- Fetch the webpage
- Parse the webpage
- Extract the URLs
- Filter the URLs
- Rename the URLs
- Download each URL
- Save the URLs
- Rename the files
- Inspect the files
------------------- 
- Find the sheets
- Find the header rows for each sheet
- Verify that each row has the right pattern
- Clean up the headers
- Rewrite as CSV
- Compile the headers
- Compare the headers
- Write a lookup table
- Verify the values in each table
- Combine the three different tests
- Combine three tests into one file
--------------------
Audit time
"--" to NA
--------------------
Some Visualization time
--------------------
Table joins and more data downloading
-------------
More integrity checks
-------------
Data exporting
-------------
Data visualizing in R
--------------



