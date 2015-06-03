#!/usr/bin/env python3
#
# Python 3 script that, given an addresses, calls Google's Geocoding API and prints to stdout: lat, lng, level of accuracy, and formatted address
#
# It can be configured to print the raw JSON or use a different delimiter for the single output

# Documentation of Google Maps API
# https://developers.google.com/maps/documentation/geocoding/


#
# Usage:
#
#    $ script.py "100 Broadway New York, NY"
#
# Response:
#
#    40.70791579999999  -74.01107309999999  ROOFTOP 100 Broadway, New York, NY 10006, USA
#
#
# usage: script.py [-h] [--copy] [--delimiter DELIMITER] [--json] addr

# positional arguments:
#   addr                  Enter an address, preferably quoted

# optional arguments:
#   -h, --help            show this help message and exit
#   --copy, -c            Copy JSON response to file at current directory
#   --delimiter DELIMITER, -d DELIMITER
#                         Use specified delimiter between values; default is ` `
#   --json, -j            Instead of the tab-delimited values, print the JSON
#                         response to stdout

########################################

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


### CLI
args = parser.parse_args()
addr = args.addr[0]
resp = requests.get(GOOGLE_MAPS_URL, params = {'address': addr})
results = resp.json()['results']
if results:
    if args.json:
        print(resp.text)
    else:
        outs = StringIO()
        c = csv.writer(outs, delimiter = args.delimiter, quoting = csv.QUOTE_MINIMAL)
        r = results[0]
        c.writerow([
            r['geometry']['location']['lat'],
            r['geometry']['location']['lng'],
            r['geometry']['location_type'],
            r['formatted_address']
        ])

        print(outs.getvalue().strip())

    ## save to file with --save
    if args.copy:
        # save to "The+Address+NewYork,NY.json"
        fpath = quote_plus(addr) + '.json'
        with open(fpath, 'w') as f:
            f.write(resp.text)
