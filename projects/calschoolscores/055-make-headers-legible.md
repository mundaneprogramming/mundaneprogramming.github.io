
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
