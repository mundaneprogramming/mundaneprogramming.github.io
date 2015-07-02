# In progress...

# Fetches public school database and adds district and county codes
# Landing page
# http://www.cde.ca.gov/ds/si/ds/pubschls.asp
# More about schools
# http://www.cde.ca.gov/ds/si/ds/
from os import makedirs
from urllib.request import urlretrieve
import csv
import os.path
import shutil

DATA_DIR = './data-hold/cde'
DATA_FILES = {
    'district': {
        "url": 'http://www.cde.ca.gov/ds/si/ds/documents/legdist2014.xls',
        'local': os.path.join(DATA_DIR, 'legdist2014.xls')
    },
    'schools': {
        "url": 'ftp://ftp.cde.ca.gov/demo/schlname/pubschls.txt',
        'local': os.path.join(DATA_DIR, 'pubschls.txt')
    }
}
# TODO: pubschls gets updated daily; might be worth timestamping it upon each download
makedirs(DATA_DIR, exist_ok = True)
for d in DATA_FILES.values():
    # download the data
    resp = urlretrieve(d['url'])
    # whatever I don't even understand urllib
    shutil.copy(resp[0], d['local'])
    print("Copied", d['url'], 'to:', d['local'])

# Now work with the local schools file:
# TODO
# txt = open(DATA_FILES['schools']['local'], encoding = 'latin-1').read()
# rows = list(csv.DictReader(txt.splitlines(), delimiter = "\t"))
