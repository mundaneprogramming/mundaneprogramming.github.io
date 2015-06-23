import os.path
import re
import requests
from glob import glob
from os import makedirs
from shutil import unpack_archive
DATA_DIR = "/tmp/babynames/nation/" # replace with your choice
makedirs(DATA_DIR, exist_ok = True)
# Specify where the zip file stuff
ZIP_URL = 'http://www.ssa.gov/oact/babynames/names.zip'
ZIP_DEST = os.path.join(DATA_DIR, 'names.zip')
DATAFILE_DEST = os.path.join(DATA_DIR, "all-nation.csv")
# Download the zip...it may take a few minute
print("Downloading", ZIP_URL, "to", ZIP_DEST)
zipfile = requests.get(ZIP_URL).content
f = open(ZIP_DEST, 'wb')
f.write(zipfile)
f.close()

# Now to unzip it
print("Unzipping", ZIP_DEST)
unpack_archive(ZIP_DEST, DATA_DIR)
# DATA_DIR now contains a bunch of text files named like:
# yob1990.txt
# The text files do not have headers
# each row looks like this:
# Pamela,F,258
# One of the things we need to do is add a year column

# Now create the combined text file
dfile = open(DATAFILE_DEST, 'w')
# write the headers
dfile.write("name,sex,count,year\n")

# now glob all the files into a list
txtfiles = glob(DATA_DIR + '*.txt')
print("There are", len(txtfiles), "textfiles")
for fn in txtfiles:
    # get the year from the filename
    year = re.search("\d{4}", fn).group()
    print("Year:", year)
    f = open(fn)
    # iterate through each line
    for line in f.readlines():
        dfile.write(line.strip() + "," + year + "\n")
    # add ",year" to each line
    f.close()
