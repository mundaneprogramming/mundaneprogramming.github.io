
### Step 1. Download the webpage


~~~py
import requests
CDE_URL = 'http://www.cde.ca.gov/ds/sp/ai/'
rawhtml = requests.get(CDE_URL).text
~~~
