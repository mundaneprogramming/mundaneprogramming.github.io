# get most recent execution and next execution
from datetime import datetime
from lxml import html
import requests
d = {}

# get next execution
url = "https://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html"
resp = requests.get(url)
doc = html.fromstring(resp.text)
row = doc.cssselect('table tr')[1]
cols = row.cssselect('td')
exdate = datetime.strptime(cols[7].text_content(), '%m/%d/%Y')

print((datetime.now() - exdate).days, "days since Texas executed someone.")
# "5 days since Texas executed someone.""
