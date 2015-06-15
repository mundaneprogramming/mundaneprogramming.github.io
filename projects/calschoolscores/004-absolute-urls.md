
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
