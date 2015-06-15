---
title: California test scores
description: A mini-project to collect California school data, using a variety of mundane programming scripts and libraries.
---









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
- Write a lookup dictionary for the headers
- Verify the values in each table
- Combine the three different tests
- Combine three tests into one file
--------------------
Audit and cleanup time
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



