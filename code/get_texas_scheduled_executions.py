# get most recent execution and next execution
from datetime import datetime
from lxml import html
from urllib.parse import urljoin
import json
import requests
d = {}

# get next execution
url = "http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"
resp = requests.get(url)
doc = html.fromstring(resp.text)
row = doc.cssselect('table tr')[1]
cols = row.cssselect('td')
bdate = datetime.strptime(cols[5].text_content(), '%m/%d/%Y')
exdate = datetime.strptime(cols[0].text_content(), '%m/%d/%Y')
d['next'] = {
    'exdate': exdate.strftime('%Y-%m-%d'),
    'link': urljoin(url, cols[1].cssselect('a')[0].attrib['href']),
    'last_name': cols[2].text_content(),
    'first_name': cols[3].text_content(),
    'tdcj': cols[4].text_content(),
    'birthdate': bdate.strftime('%Y-%m-%d'),
    'race': cols[6].text_content()
}

# get previous most recent execution
url = "https://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html"
resp = requests.get(url)
doc = html.fromstring(resp.text)
# most recent execution is at top
row = doc.cssselect('table tr')[1]
cols = row.cssselect('td')
exdate = datetime.strptime(cols[7].text_content(), '%m/%d/%Y')
d['previous'] = {
    'exdate': exdate.strftime('%Y-%m-%d'),
    'link': urljoin(url, cols[1].cssselect('a')[0].attrib['href']),
    'last_name': cols[3].text_content(),
    'first_name': cols[4].text_content(),
    'tdcj': cols[5].text_content(),
    'age': cols[6].text_content(),
    'race': cols[8].text_content()
}


json.dumps(d, indent = 2)
