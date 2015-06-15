
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
