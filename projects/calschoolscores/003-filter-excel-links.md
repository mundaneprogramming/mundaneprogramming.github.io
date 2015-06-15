

### Step 3. Extract only the Excel links

~~~py
xlslinks = [link for link in links if 'xls' in str(link.attrib.get('href'))]
~~~


There are 45 links

~~~py
len(xlslinks)
# 45
~~~
