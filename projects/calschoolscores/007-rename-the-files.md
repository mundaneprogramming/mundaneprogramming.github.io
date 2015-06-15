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
