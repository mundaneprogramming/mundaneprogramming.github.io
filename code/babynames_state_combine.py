from glob import glob
import os.path
import re
import requests
from os import makedirs
from shutil import unpack_archive
DATA_DIR = "/tmp/babynames/state/" # replace with your choice
makedirs(DATA_DIR, exist_ok = True)
# Specify where the zip file stuff
ZIP_URL = 'http://www.ssa.gov/OACT/babynames/state/namesbystate.zip'
ZIP_DEST = os.path.join(DATA_DIR, 'names.zip')
DATAFILE_DEST = os.path.join(DATA_DIR, "all-state.csv")
# Download the zip...it may take a few minute
print("Downloading", ZIP_URL, "to", ZIP_DEST)
zipfile = requests.get(ZIP_URL).content
with open(ZIP_DEST, 'wb') as f:
    f.write(zipfile)
# Now to unzip it
print("Unzipping", ZIP_DEST)
unpack_archive(ZIP_DEST, DATA_DIR)
# DATA_DIR now contains a bunch of text files named like:
# AZ.TXT
# The text files do not have headers
# each row looks like this:
# AZ,F,1910,Elizabeth,15

# Now create the combined text file
dfile = open(DATAFILE_DEST, 'w')
# write the headers
dfile.write("state,sex,year,name,count\n")
# now glob all the files into a list
txtfiles = glob(DATA_DIR + '*.TXT')
print("There are", len(txtfiles), "textfiles")
for fn in txtfiles:
    # get the year from the filename
    state = os.path.basename(fn).split('.')[0]
    print("State:", state)
    with open(fn) as f:
        # no need to add things to each line, just copy the whole thing
        # iterate through each line
        dfile.writelines(f.readlines())
