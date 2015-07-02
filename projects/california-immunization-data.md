## Fetching and collating the California Kindergarten immunization data in Python and Bash


by Dan Nguyen [@dancow](https://twitter.com/dancow)

*__tl;dr__: a quick example of practicing reproducible data journalism, and somewhat timely given the [recent school vaccination law signed by California Gov. Jerry Brown](http://www.npr.org/sections/thetwo-way/2015/06/30/418908804/california-governor-signs-school-vaccination-law)*


These are scripts that are part of the [mundaneprogramming.github.io repo for SRCCON 2015](http://mundaneprogramming.github.io) and will soon have their own entry/explanation on that site. They aren't meant to be best/canonical practices (e.g. I felt like using csv.DictWriter so there it is), nor do I guarantee that they work. But you're free to run them to see what happens. All they currently do is download the relevant spreadsheets and compile them into a file, which ends up being one of the most tedious parts of the entire investigation due to how the [files are organized on the homepage](http://www.cdph.ca.gov/programs/immunize/pages/immunizationlevels.aspx) and their internal organization. For example, after 2012, the column layouts change, which accounts for most of the code in [__collate.py__](#file-collate-py). 



##### Example pre-2012 spreadsheet

![Imgur](http://i.imgur.com/RCm9u8P.png)

##### Example post-2012 spreadsheet

![Imgur](http://i.imgur.com/0yWIuxc.png)


##### Resulting spreadsheet after `collate.py`

![Imgur](http://i.imgur.com/wF1XBFy.png)

### Bash preparation

It's always nice when dealing with government data to create a complete mirror of the site, just in case it changes or gets removed at some point in the future. This is a good time to practice some basic but very reusable shell commands.

#### Mirror the site

Use [__wget__](http://www.gnu.org/software/wget/manual/wget.html) to perform a _recursive_ fetch, __one__-_level_ deep. In the fetched pages, convert the links to relative locations, and append `.html` to all webpage-like files (i.e. `somepage.aspx.html`). This partial mirror will be saved to the local path in a subdirectory named `www.cdph.ca.gov`:

    wget --recursive --level=1 --adjust-extension --convert-links \
    http://www.cdph.ca.gov/programs/immunize/pages/immunizationlevels.aspx

Use [Amazon's AWS command-line interface tool](http://docs.aws.amazon.com/cli/latest/userguide/using-s3-commands.html) to upload the wgotten-files to S3:

    aws s3 sync www.cdph.ca.gov/ s3://www.mundaneprogramming.com/sites/ --acl public-read

The resulting live Web address (if [you've configured your S3 instance to act as a staticweb server](http://www.smalldatajournalism.com/projects/one-offs/using-amazon-s3/)) would look something like this:

http://www.mundaneprogramming.com.s3.amazonaws.com/sites/programs/immunize/pages/immunizationlevels.aspx.html



### Description of the Python scripts

The scripts below are written for __Python 3.x__ and were tested specifically on OS X 10.10 / __Python 3.4.3 :: Anaconda 2.2.0 (x86_64)__. The [Anaconda 3.x distribution](http://continuum.io/downloads) includes all the necessary dependencies, including [xlrd for manipulating of Excel files](http://www.python-excel.org/).

- [__fetcher.py__](#file-fetcher-py) - Downloads the Excel spreadsheets containing Kindergarten-level data from the [California Department of Health's Immunization Levels in Child Care and Schools homepage](http://www.cdph.ca.gov/programs/immunize/pages/immunizationlevels.aspx). Files are saved into a local path, `./data-hold/xls/immunization`, and are given a more uniform-naming scheme, e.g. `K--2013-2014.xls` rather than `2013-2014%20CA%20Kindergarten%20Data.xls`. The data currently dates back to the [2000-2001 school year]( http://www.cdph.ca.gov/programs/immunize/Documents/2000-2001%20CA%20Kindergarten%20Data.xls)

- [__collate.py__](#file-collate-py) - Assuming __fetcher.py__ has been run, this opens each downloaded spreadsheet and saves them to a single spreadsheet. In 2012, the column layout changes. This script reconciles both layouts and includes the *union* of possible columns (e.g., the `mmr1_num` column is simply left empty for post-2012 datasets). The data is compiled into two different (but equivalent) formats: CSV and JSON. One caveat: if you decide to open up one of the downloaded spreadsheets with Excel, it will create a temporary, hidden `.xlsx` file while Excel is running. And then if you run `collate.py`, you'll get an error as it tries to open this shadow file...So, don't open these files in Excel while running `collate.py`, basically.





#### Output of `collate.py`

    ./data-hold/xls/immunization/K--2000-2001.xls has 7442 rows
    ./data-hold/xls/immunization/K--2001-2002.xls has 7527 rows
    ./data-hold/xls/immunization/K--2002-2003.xls has 7453 rows
    ./data-hold/xls/immunization/K--2003-2004.xls has 7377 rows
    ./data-hold/xls/immunization/K--2004-2005.xls has 7386 rows
    ./data-hold/xls/immunization/K--2005-2006.xls has 7396 rows
    ./data-hold/xls/immunization/K--2006-2007.xls has 7389 rows
    ./data-hold/xls/immunization/K--2007-2008.xls has 7334 rows
    ./data-hold/xls/immunization/K--2008-2009.xls has 7199 rows
    ./data-hold/xls/immunization/K--2009-2010.xls has 7150 rows
    ./data-hold/xls/immunization/K--2010-2011.xls has 7190 rows
    ./data-hold/xls/immunization/K--2011-2012.xls has 7351 rows
    ./data-hold/xls/immunization/K--2012-2013.xls has 7662 rows
    ./data-hold/xls/immunization/K--2013-2014.xls has 7404 rows
    ./data-hold/xls/immunization/K--2014-2015.xlsx has 7494 rows
    There are 110264 data rows all together
    Writing to JSON: ./data-hold/finished/k-immune.json
    Writing to CSV: ./data-hold/finished/k-immune.csv



#### Sample CSV output




#### Sample JSON output

~~~json
[
    {
        "school_type": "PUBLIC",
        "polio_num": 80.0,
        "mmr2_num": 80.0,
        "pme_num": 0.0,
        "district_code": "75101",
        "conditional_num": 0.0,
        "pbe_pct": 0.0,
        "hepb_num": 80.0,
        "pbe_num": 0.0,
        "dtp_num": 80.0,
        "uptodate_num": 80.0,
        "polio_pct": 100.0,
        "mmr2_pct": 100.0,
        "school_name": "ALISAL ELEM",
        "conditional_pct": 0.0,
        "dtp_pct": 100.0,
        "year": 2000,
        "enrollment": 80.0,
        "school_code": "6002315",
        "county": "ALAMEDA",
        "mmr1_num": 80.0,
        "hepb_pct": 100.0,
        "uptodate_pct": 100.0,
        "pme_pct": 0.0,
        "mmr1_pct": 100.0
    }
]
~~~




### Reproducible data

These scripts are meant to be examples of reproducability. Specifically, the kind of reproducible build that comes as part and parcel of programming. Obviously, you could write scripts to turn the collated the data into visualizations. Or, more mundanely but just as important -- back up the original files to a separate mirror, just in case California state changes their data offering. Either way, the mindset is to describe the steps you *have* to do, as code. It takes extra time at first, but then you can re-run them at any time to get exactly what you had before. This consistency is not just a hobgoblin of little minds; once the steps have been abstracted to code, it becomes very easy, and error-free, to recollect/reorganize the data when, later in the investigation, you've decided that, oh, it'd be nice to include what in retrospect seemed like an irrelevant datapoint/dataset.

__Case in point:__ the preschool data isn't currently included in these batch scripts but they seem to be similar in structure and organization (though the earliest, non-summarized data is [for 2010-2011](http://www.cdph.ca.gov/programs/immunize/Documents/2010-2011%20Child%20Care%20Data.xls)). It's relatively easy to adjust [fetcher.py](#file-fetcher-py) and [collate.py](#file-collate-py) to create a dataset that includes both kinds of schools, even if you're already at the part where you've visualized/mapped the data.

__And speaking of mapping the data__: After running `collate.py`, you would need to join the schools against the [California Department of Education's Public Schools Data file](http://www.cde.ca.gov/ds/si/ds/pubschls.asp), which contains addresses and geo coordinates. However, that's just another script in the pipeline. And considering the Department of Health has an inconsistent way of naming the schools, across the years and across post/pre-2012 layouts, having a script like `collate.py` is pretty much essential to *sanely* joining the health data to the CDE's geodata. 

In other words, for the immunization dataset, you need to derive the unique school identifier from this:



| SCHOOL CODE |  COUNTY | PUBLIC/PRIVATE |       PUBLIC SCHOOL DISTRICT       |   CITY  |       SCHOOL NAME        |
|-------------|---------|----------------|------------------------------------|---------|--------------------------|
|     0130419 | ALAMEDA | PUBLIC         | ALAMEDA COUNTY OFFICE OF EDUCATION | HAYWARD | ALAMEDA COUNTY COMMUNITY |
|             |         |                |                                    |         |                          |

| SCHOOL CODE |  COUNTY |
|-------------|---------|
|     0130419 | ALAMEDA |


To join against the corresponding foreign key in the [public schools database](http://www.cde.ca.gov/ds/si/ds/fspubschls.asp):

         01100170130419





Why doesn't the immunization dataset just include the school's unique identifier, i.e. the __CDSCode__ found in the [public schools data file](http://www.cde.ca.gov/ds/si/ds/pubschls.asp)? Because the CDSCode is a convention created by the Department of Education. And the immunization data is generated by the Department of Public Health. Obvious, isn't it?.

So it's not necessary to see reproducible data as being an issue of transparency; it is a direct consequence of systematically expressing the data-gathering steps as code, a process which is necessary for doing the kind of expansive data-joining operations common in investigative journalism. So it's a win-win for journalist and audience.

It's also _horribly boring_ to write that code. On the other hand, even if it takes you longer to write the code than to do the work manually, it's still a great time to learn how to program, or to experiement with different libraries. For instance, I had almost never used [Python's xlrd library](http://www.python-excel.org/) for opening/reading Excel files. But not only is it essential for this scenario, it is an incredibly useful library that now makes it much, *much* easier for me to work with Excel data in the future -- and yet I would've never bothered looking at [xlrd](http://www.python-excel.org/) for a project on deadline.
