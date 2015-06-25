from csv import DictReader, DictWriter
from collections import defaultdict, Iterable
from copy import copy
import json
import argparse

NATION_BABYNAMES_FILENAME = './files/datadumps/all-nation-babynames.csv'
DATA_FILENAME = './files/datadumps/babynamegenders.csv'
DATA_HEADERS = ['name', 'likely_gender', 'likely_percent', 'total', 'total_rank', 'per_million']
START_YEAR = 1950
END_YEAR = 2014


def compile_data_file():
    names = defaultdict(lambda: defaultdict(int))
    with open(NATION_BABYNAMES_FILENAME) as sfile:
        rows = DictReader(sfile)
        for r in rows:
            year = int(r['year'])
            if year >= START_YEAR and year <= END_YEAR:
                n = r['name'].upper()
                s = r['sex']
                names[n][s] += int(r['count'])

    # now everything is in a neat list: somenames
    # first, let's get total number of rows
    print("Unique names:", len(names.keys()))
    # each entry in namesbysex looks like:
    # {
    #     ('JAMES', 'M'): 100000
    # }
    # let's sum up the babies
    total_babies = sum(sum(vals.values()) for vals in names.values())
    print("Total babies:", total_babies)
    # Now for each unique name
    compiled_names = []
    for name, sexes in names.items():
        z = {'name': name}
        # find entries in namesbysex...there's, at most, 2
        s1, s0  = ['F', 'M'] if sexes['F'] >= sexes['M'] else ['M', 'F']
        z['likely_gender'] = s1
        z['total'] = sexes[s1] + sexes[s0]
        z['likely_percent'] = round(sexes[s1] * 100 / z['total'])
        z['per_million'] = z['total'] * 1000000 // total_babies
        compiled_names.append(z)
    # now write to file
    sorted_names = sorted(compiled_names, key = lambda x: x['total'], reverse = True)
    dfile = open(DATA_FILENAME, 'w')
    dcsv = DictWriter(dfile, fieldnames = DATA_HEADERS)
    dcsv.writeheader()
    xrank = 0
    xtotal = 0
    for idx, row in enumerate(sorted_names):
        if row['total'] < xtotal or xrank == 0:
            xrank = idx + 1
            xtotal = row['total']
        row['total_rank'] = xrank
        dcsv.writerow(row)
    dfile.close()





def find_names(*names):
    with open(DATA_FILENAME) as f:
        rows = list(DictReader(f))
    null_result = {'likely_gender': 'NA', 'likely_percent': 0, 'total': 0, 'total_rank': -1, 'per_million': 0}
    results = []
    for n in flatten(names):
        nup = n.upper()
        d = copy(next((r for r in rows if r['name'] == nup), null_result))
        d['name'] = n # keep original capitalization of name there
        results.append(d)
    return results


# a little convenience function for flattening an array
# http://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists-in-python
def flatten(things):
    for x in things:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for y in flatten(x):
                yield y
        else:
            yield x



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("names", nargs = '*', help = 'A list of names')
    parser.add_argument("--column-names", "-c", action = "store_true", default = False, help = 'Include headers for CSV')
    parser.add_argument("--json", "-j", action = "store_true", default = False, help = 'JSON format instead of CSV')
    parser.add_argument("--compile-data", "-d", action = "store_true", default = False, help = "recompile data")
    args = parser.parse_args()
    names = args.names
    results = find_names(names)

    if args.compile_data:
        print("Compiling data file")
        compile_data_file()
    else:
        # normal operation

        if args.json:
            data = json.dumps(results, indent = 2)
            print(data)
        else: # do CSV
            if args.column_names:
                print('name,likely_gender,likely_percent,per_million,rank')
            for r in results:
                if r.get('likely_gender'):
                    print("%s,%s,%s,%s,%s" %
                        (r['name'], r['likely_gender'], r['likely_percent'], r['per_million'], r['total_rank']))
                else:
                    print('%s,NA,0,0,0' % r['name'])
