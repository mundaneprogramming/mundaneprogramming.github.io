# get most recent execution and next execution
from datetime import datetime
from lxml import html
import requests
d = {}

# get next execution
url = "http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"
resp = requests.get(url)
doc = html.fromstring(resp.text)
row = doc.cssselect('table tr')[1]
cols = row.cssselect('td')
exdate = datetime.strptime(cols[0].text_content(), '%m/%d/%Y')


print((exdate - datetime.now()).days, "days until the next Texas death row execution")
# "10 days until the next Texas death row execution"
