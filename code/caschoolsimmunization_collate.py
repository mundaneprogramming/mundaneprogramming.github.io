## This expects the fetching script to have run
## it compiles all the spreadsheets:
##   - k-immune.csv
##   - k-immune.json

import csv
import json
import os.path
import re
from glob import glob
from os import makedirs
from xlrd import open_workbook
XLS_DIR = "./data-hold/xls/immunization"
FINISHED_DIR = './data-hold/finished'


pre_2012_headers = ['school_code', 'county', 'school_type', 'district_code', 'school_name',
'enrollment', 'uptodate_num', 'uptodate_pct', 'conditional_num', 'conditional_pct',
'pme_num', 'pme_pct', 'pbe_num', 'pbe_pct', 'dtp_num', 'dtp_pct', 'polio_num',
'polio_pct', 'mmr1_num', 'mmr1_pct', 'mmr2_num', 'mmr2_pct', 'hepb_num', 'hepb_pct',
'vari_num', 'vari_pct']
pre_2014_headers = ['school_code', 'county', 'school_type', 'district_name', 'city',
'school_name', 'enrollment', 'uptodate_num', 'uptodate_pct', 'conditional_num', 'conditional_pct',
'pme_num', 'pme_pct', 'pbe_num', 'pbe_pct', 'dtp_num', 'dtp_pct', 'polio_num',
'polio_pct', 'mmr2_num', 'mmr2_pct', 'hepb_num', 'hepb_pct', 'vari_num', 'vari_pct', 'reported']
# differences between pre/post 2012:
#  post-2012 only records 2-dose MMR, e.g. `mmr2_num` and `mmr2_pct`
post_2014_headers = ['school_code', 'county', 'school_type', 'district_name', 'city',
    'school_name', 'enrollment', 'uptodate_num', 'uptodate_pct', 'conditional_num', 'conditional_pct',
    'pme_num', 'pme_pct', 'pbe_num', 'pbe_pct',
    # special fields to 2014
    'pre_jan_pbe_num','pre_jan_pbe_pct',
    'hcp_counseled_pbe_num', 'hcp_counseled_pbe_pct',
    'religous_pbe_num', 'religous_pbe_pct',
    # same ol fields as before
    'dtp_num', 'dtp_pct', 'polio_num',
    'polio_pct', 'mmr2_num', 'mmr2_pct', 'hepb_num', 'hepb_pct', 'vari_num', 'vari_pct', 'reported']



common_headers = ['year',
    'school_code', 'county', 'school_type', 'district_code',
    'city', 'district_name', 'school_name',
    'enrollment', 'uptodate_num', 'uptodate_pct', 'conditional_num', 'conditional_pct',
    'pme_num', 'pme_pct', 'pbe_num', 'pbe_pct',
    'pre_jan_pbe_num','pre_jan_pbe_pct',
    'hcp_counseled_pbe_num', 'hcp_counseled_pbe_pct',
    'religous_pbe_num', 'religous_pbe_pct',
    'dtp_num', 'dtp_pct', 'polio_num',
    'polio_pct', 'mmr1_num', 'mmr1_pct', 'mmr2_num', 'mmr2_pct', 'hepb_num', 'hepb_pct',
    'vari_num', 'vari_pct',
    'reported']


makedirs(XLS_DIR, exist_ok = True)
makedirs(FINISHED_DIR, exist_ok = True)

data = []
for xlsname in glob(os.path.join(XLS_DIR, '*.xls*')):
    # extract the year numbers from the file name
    # e.g. "2006" and "2007" from "K--2006-2007.xls"
    yr_1, yr_2 = re.search('(\d{4})-(\d{4})', xlsname).groups()
    year = int(yr_1)
    if year < 2012:
        headers = pre_2012_headers
    elif year < 2014:
        headers = pre_2014_headers
    else:
        headers = post_2014_headers


    # open the Excel workbook
    book = open_workbook(xlsname)
    # open the first non-empty spreadsheet
    sheet = [s for s in book.sheets() if s.nrows > 0][0]
    print(xlsname, "has", sheet.nrows, "rows")
    for x in range(1, sheet.nrows - 1):
        row = sheet.row_values(x)
        if re.search('\d{7}', str(row[0])):
            d = dict(zip(headers, row))
            d['year'] = year
            data.append(d)


print("There are", len(data), 'data rows all together')

# write a JSON
# Note: fields that don't exist in a given layout are *not* included as null values.
#       they are simply left out of each dict
jname = os.path.join(FINISHED_DIR, 'k-immune.json')
print("Writing to JSON:", jname)
with open(jname, "w") as jfile:
    jfile.write(json.dumps(data, indent = 4))

# write a CSV
cname = os.path.join(FINISHED_DIR, 'k-immune.csv')
print("Writing to CSV:", cname)
cfile = open(cname, 'w', encoding = 'utf-8')

writer = csv.DictWriter(cfile, fieldnames = common_headers, delimiter=',')
writer.writeheader()
for d in data:
    writer.writerow(d)
