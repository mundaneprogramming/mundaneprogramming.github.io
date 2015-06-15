### Downloading the spreadsheets

~~~py
from os.path import basename
for url in urls:
  with open(basename(url), "wb") as f:
    print("Downloading", url)
    f.write(requests.get(url).content)
~~~

