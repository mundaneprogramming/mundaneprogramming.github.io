
~~~py
from lxml import html
import requests

url = "http://www.fldoe.org/accountability/accountability-reporting/act-sat-ap-data/act-sat-ap-data-archive.stml"

doc = html.fromstring(requests.get(url).text)
xlslinks = [a for a in doc.cssselect('a') if 'xls' in a.attrib['href'].lower()]


for a in xlslinks:
  href = a.attrib['href']
  if 'ap' in href and 'sch' in href:
    print(href) 

~~~


