from csv import DictReader, DictWriter
from collections import defaultdict
NATION_BABYNAMES_FILENAME = './files/datadumps/all-nation-babynames.csv'
START_YEAR = 1950
END_YEAR = 2014
DATA_FILENAME = './files/datadumps/babynamegenders.csv'
DATA_HEADERS = ['name', 'likely_gender', 'likely_percent', 'total', 'total_rank', 'per_million']


def compile_data_file(all_fname = NATION_BABYNAMES_FILENAME,
                        data_fname = DATA_FILENAME):
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
    dfile = open(data_fname, 'w')
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
    for n n

