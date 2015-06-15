
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
