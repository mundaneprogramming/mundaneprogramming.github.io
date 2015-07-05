---
title: Combining text files
description: |
  In many real world situations, data is not only dirty, it's not even put together in a single file.
the_routine:
  - Open a blank, new text file.
  - Open an existing text file.
  - Copy existing text file.
  - Paste existing text file into new text file.
  - Open another existing text file.
  - Repeat.
the_need: |
  Using the relatively clean and straightforward baby names data from the Social Security Administration, this example shows several variations of how to combine text files in Bash and in Python, including how to add data on a per-file, per-line basis. This is a good time to not only get acquainted with the conveniences of Bash programming, but to practice using higher-level CSV libraries (even though they are overkill in this situation).
keywords: |
  skills:
    - Regular expressions
    - Delimiting text
  languages:
    Python: ['csv', 're', 'os.path']
    Bash: ['cat']
authors:
  - dannguyen
rank: 1
featured: true
complete: false
files: 
  - name: code/babynames_nation_combine.py
  - name: code/babynames_state_combine.py



---



## Just `cat`

The Unix operating system has long had the simple __cat__ program, which has no other ambition than to take a list of files given to it and then to combine, or concatenate their streams:

~~~sh
cat file1.txt file2.txt > all.txt 
~~~

This is actually good enough for many situations, and even the most skilled practitioner will first think of `cat` as a first resort.


## Baby names by state

The U.S. [Social Security Administration releases bulk data on baby names](http://www.ssa.gov/oact/babynames/limits.html) in two different zip files: [by state](http://www.ssa.gov/oact/babynames/state/namesbystate.zip) and [by year (nationwide)](http://www.ssa.gov/oact/babynames/names.zip). Each zip file contains dozens of text files totaling in the tens of megabytes.

The [states file](http://www.ssa.gov/oact/babynames/state/namesbystate.zip) is pretty straightforward. The list of text files, one for each state, looks like this:

~~~
AK.TXT    HI.TXT    MI.TXT    NV.TXT    TX.TXT
AL.TXT    IA.TXT    MN.TXT    NY.TXT    UT.TXT
AR.TXT    ID.TXT    MO.TXT    OH.TXT    VA.TXT
AZ.TXT    IL.TXT    MS.TXT    OK.TXT    VT.TXT
CA.TXT    IN.TXT    MT.TXT    OR.TXT    WA.TXT
CO.TXT    KS.TXT    NC.TXT    PA.TXT    WI.TXT
CT.TXT    KY.TXT    ND.TXT    RI.TXT    WS_FTP.LOG
DC.TXT    LA.TXT    NE.TXT    SC.TXT    WV.TXT
DE.TXT    MA.TXT    NH.TXT    SD.TXT    WY.TXT
FL.TXT    MD.TXT    NJ.TXT    StateReadMe.pdf
GA.TXT    ME.TXT    NM.TXT    TN.TXT
~~~


Each text file is _headerless_. Each row has this comma-separated value format:

    state abbreviation, sex, year, name, count

e.g.

    AK,F,1910,Mary,14
    AK,F,1910,Annie,12
    AK,F,1910,Anna,10
    AK,F,1910,Margaret,8
    AK,F,1910,Helen,7


### Bash cat

Because the files are all the same format, we just have to paste them one-after-another into a combined file, not having to worry about deleting the redundant headers.

Assuming you're currently in the directory containing the unzipped text files, here's how to combine all the state files (i.e. files that end with `.TXT`) into a file named `allstates.csv`

~~~sh
cat *.TXT > allstates.csv
~~~


#### Adding a header line

That was just too easy. Of course, we *want* column headers in the combined `allstates.csv`, so that other programs (such as Excel, or a SQL database) or, generally, anyone who wants to use `allstates.csv`, knows what the columns are.

We can do this manually with `echo`:

~~~sh
echo "state,sex,year,name,count" > allstates.csv
cat *.TXT >> allstates.csv
~~~



### Bash for-loop

Using `cat` seems simple enough. Let's practice the `for` construct:

~~~sh
echo "state,sex,year,name,count" > allstates.csv
for fname in *.TXT; do
  echo Adding $fname
  cat $fname >> allstates.csv
done
~~~



__Note:__ It's not an issue here &ndash; but because of the naive way that bash handles spaces-within-filenames, the above `for`-loop [can be quite erratic, if not dangerous](http://superuser.com/questions/31464/looping-through-ls-results-in-bash-shell-script). However, I'll leave the lengthy discussion on the ins-and-outs of that for another occasion; in this (_very_) controlled scenario, you shouldn't run into any filename/operating-system-specific issues.


### Python for-loop

Hopefully you can see the elegance of the bash solution. But pretend you're not on a Unix-like system, or that you want to practice Python:

~~~python
from glob import glob
output = open("allstates.csv", "w")
output.write("state,sex,year,name,count\n")
for fname in glob("*.TXT"):
    print("Adding", fname)
    f = open(fname)
    output.write(f.read())
    f.close()
output.close()
~~~



### Practicing the `with` statement

This is a good time to get into the habit of using [Python's `with` statement](https://www.python.org/dev/peps/pep-0343/), which isn't important in this situation, but standard practice when working with bigger datasets and real-world operating scenarios:


~~~python
from glob import glob
with open("allstates.csv", "w") as output:
    output.write("state,sex,year,name,count\n")
    for fname in glob("*.TXT"):
        print("Adding", fname)
        with open(fname) as f:
           output.write(f.read())
~~~





## Baby names by year

How the SSA packages the [nationwide _by year_ baby names text files](http://www.ssa.gov/oact/babynames/names.zip) is more complicated. 

Each year has its own headerless file:

~~~
NationalReadMe.pdf  yob1924.txt   yob1969.txt
yob1880.txt   yob1925.txt   yob1970.txt
yob1881.txt   yob1926.txt   yob1971.txt
yob1882.txt   yob1927.txt   yob1972.txt
yob1883.txt   yob1928.txt   yob1973.txt
~~~

However, unlike the state text files, the year text files _do not include the year on each row. For example, here are the first five lines from `yob1984.txt`:

      Jennifer,F,50556
      Jessica,F,45849
      Ashley,F,38759
      Amanda,F,33903
      Sarah,F,25873

But how do you know that they originated from the `1984` file, without having been told beforehand? This means that simply `cat`-ing all the files together would make it impossible to distinguish which row comes from which year.


### Grep and iterate line-by-line, per-file, in Bash

Luckily, we practiced using the `for`-loop in both Bash and Python, which gives us the flexibility to alter the files on a per-file, per-line basis. With bash and the use of `grep` to capture the year per filename:

~~~sh
echo "year,name,sex,count" > allyears.csv
for fname in *.txt; do
  year=$(echo $fname | grep -oE [0-9]{4})
  echo Year $year
  cat $fname | while read -r line; do
    echo "$year,$line" >> allyears.csv
  done
done
~~~


### Python for-loops and regex module

Same concept here. If you already have some [basic familiarity with regular expressions](https://docs.python.org/3/library/re.html), try practicing a positive-lookbehind and Python's `os.path` module for more exactness (even though it's not needed here):

~~~python
from os.path import basename
from glob import glob
import re
with open("allyears.csv", "w") as output:
    output.write("year,name,sex,count\n")
    for fname in glob("*.txt"):
        year = re.search(r'(?<=^yob)\d{4}', basename(fname)).group()
        print("Adding", year)
        with open(fname, 'r') as f:
           # readlines is OK here, bad in practice for massive files
            for line in f.readlines():
                output.write("%s,%s" % (year, line)) 
~~~


### Python csv module

Again, the SSA babynames scenario is simplified, including in how we can safely expect that each line is a "simple" CSV rather than a complicated one, in which commas-within-fields and special characters have to be dealt with. In such real-world scenarios, the following is a **very bad** way to add a comma-delimited field:

~~~python
# ...    
      output.write("%s,%s" % (year, line))
~~~


So it's worth practicing [Python's `csv` module](https://docs.python.org/3/library/csv.html); to be honest, it's taken me a *lot* of time to figure out the conventions.

#### csv.Reader and csv.Writer


~~~python
from os.path import basename
from glob import glob
import re
import csv
with open("allyears.csv", "w") as output:
    cw = csv.writer(output)
    # notice different data layout, with year at the end of each row
    cw.writerow(['name', 'sex', 'count', 'year'])
    for fname in glob("*.txt"):
        year = re.search(r'(?<=^yob)\d{4}', basename(fname)).group()
        print("Adding", year)
        with open(fname, 'r') as f:
            for row in csv.reader(f):
                row.append(year)
                cw.writerow(row)
~~~


#### csv.DictReader and csv.DictWriter

If you prefer using dictionaries to track the structure of your data:

~~~python
from os.path import basename
from glob import glob
import re
from csv import DictReader, DictWriter
with open("allyears.csv", "w") as output:
    cw = DictWriter(output, fieldnames = ['name', 'sex', 'count', 'year'])
    # DictWriter will lay out columns in an unspecified order
    cw.writeheader()
    for fname in glob("*.txt"):
        year = re.search(r'(?<=^yob)\d{4}', basename(fname)).group()
        print("Adding", year)
        with open(fname, 'r') as f:
            for row in DictReader(f, fieldnames = ["name", "sex", "count"]):
                row['year'] = year
                cw.writerow(row)
~~~
