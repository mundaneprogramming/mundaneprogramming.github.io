
import argparse
import csv
from io import StringIO
import requests
from urllib.parse import quote_plus
GOOGLE_MAPS_URL = "https://maps.googleapis.com/maps/api/geocode/json"

parser = argparse.ArgumentParser()
parser.add_argument("addr", nargs = 1, help = "Enter an address, preferably quoted")

parser.add_argument('--copy', '-c',
    action = 'store_true',
    help ='Copy JSON response to file at current directory' )

parser.add_argument('--delimiter', '-d',
    default = "\t",
    help ='Use specified delimiter between values; default is `\t`' )

parser.add_argument('--json', '-j',
    action = 'store_true',
    help ='Instead of the tab-delimited values, print the JSON response to stdout' )

