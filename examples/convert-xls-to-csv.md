---
title: Convert Excel to CSV
description: Working with data that comes from an Excel spreadsheet.
rank: 1
todos:
  - simple version
  - get spreadsheet with multiple sheets
  - screenshot the spreadsheet
  - write the code
  - show pandas
---

## Prep


http://www.cde.ca.gov/ds/sp/ai/


### public schools database
layout: http://www.cde.ca.gov/ds/si/ds/fspubschls.asp

landing: http://www.cde.ca.gov/ds/si/ds/pubschls.asp

direct link: ftp://ftp.cde.ca.gov/demo/schlname/pubschls.xls
tsv: ftp://ftp.cde.ca.gov/demo/schlname/pubschls.txt


### Downloading the Public Schools database

Good time to practice __curl__:

~~~sh
curl ftp://ftp.cde.ca.gov/demo/schlname/pubschls.xls \
     -o /tmp/pubschls.xls

curl http://www.cde.ca.gov/ds/si/ps/documents/privateschools1415.xls \
      -o /tmp/privateschools1415.xls
~~~


### About xlrd

### Data files


- [pubschls-excerpt.xls](/files/datadumps/cde/pubschls-excerpt.xls)
- [pubschls.xls](/files/datadumps/cde/pubschls.xls)
- [sat13.xls](/files/datadumps/cde/sat13.xls)
- [Zip of private schools directories](/files/datadumps/cde/cdeprivateschools.zip)


## Basic operations


### Open an Excel workbook with xlrd

~~~py
from xlrd import open_workbook
book = open_workbook("/tmp/pubschls.xls")
~~~


### Count the number of sheets

~~~py
len(book.sheets())
# 1
~~~

### Counting rows

~~~py
sheet = book.sheets()[0]
sheet.nrows
# 17518
~~~

### Accessing values by row


#### Using `rows()`

~~~py
sheet.rows(0)
~~~

#### Using `row_values()`

~~~py
sheet.row_values(0)
~~~


#### Displaying cells and columns

Printing school names

~~~py
for i in range(sheet.nrows):
    cols = sheet.row_values(i)
    print(cols[6])
~~~



## Data cleaning




Private school files:


~~~sh
wget --recursive --level 1 --no-directories --accept xls
  http://www.cde.ca.gov/ds/si/ps/
~~~




~~~
privat00.xls    privat06.xls    privateschools1112.xls
privat01.xls    privat07.xls    privateschools1213.xls
privat02.xls    privat08.xls    privateschools1314.xls
privat03.xls    privat09.xls    privateschools1415.xls
privat04.xls    privat99.xls    robots.txt
privat05.xls    privateschools1011.xls
~~~


## Converting to CSV


## Making an image and other batch work





