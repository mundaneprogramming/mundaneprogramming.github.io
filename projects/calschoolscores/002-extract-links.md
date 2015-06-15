### Step 2. Extract the links

~~~py
from lxml import html
doc = html.fromstring(rawhtml)
links = doc.cssselect('a')
~~~
