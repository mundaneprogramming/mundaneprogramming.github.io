---
title: Chicago metadata as a package
authors:
  - geoffhing
description: |
  Make it easy to use information about Chicago and its geographies. Because sometimes you just need to loop through a list of Chicago neighborhoods.
---

## Introduction

At the Chicago Tribune, we often need to get a list of names of neighbrhoods, for example, to be used as taxonomy terms for content items in a Django app:

~~~py
# From a Django settings module
# ...
TOPICS = [
    'Albany Park',
    'Andersonville',
    'Archer Heights',
    'Armour Square',
    'Ashburn',
    'Auburn Gresham',
    'Austin',
    'Avalon Park',
    'Avondale',
    # ...
]
~~~ 

The first approach was to copy and paste the name from a canonical list of names and use regular expressions in my editor to quote the names so they work as members of a Python list.  This is fine, but it means you have a really long list of names in your source code.  If you want to do the same thing in another project, you end up copying and pasting the list from one project to another.  Want to use Chicago Community Areas (a statistical geography generally corresponding to neighborhood) instead? And include the community area number?  That means more copying, pasting and transforming the list in the editor.

## Reading data from a CSV

The city provides structured data about neighborhoods in CSV format:

~~~
SEC_NEIGH,PRI_NEIGH,SHAPE_AREA,SHAPE_LEN
BRONZEVILLE,Grand Boulevard,48492503.1554000005126,28196.837157000001753
PRINTERS ROW,Printers Row,2162137.971390000078827,6864.247156000000359
UNITED CENTER,United Center,32520512.705299999564886,23101.363744999998744
SHEFFIELD & DEPAUL,Sheffield & DePaul,10482592.29869999922812,13227.049745000000257
~~~

It's easy to open this up and load it into a dictionary:

~~~py
import csv

NEIGHBORHOOD_CSV_FILENAME = os.path.join(DATA_DIRECTORY,
    'Neighborhoods_2012b.csv')

neighborhood_names = []

with open(NEIGHBORHOOD_CSV_FILENAME, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        neighborhood_names.append(row['PRI_NEIGH'])
~~~

This lets you easiely maintain the neighborhood data separately from your code.  It also lets you easily add an remove columns from the data.  However, it's still not very reusable between projects because now you have to copy both a code snippet and a CSV file between projects.

## Packaging and refactoring

The ultimate solution is to package both the code to load data from CSV files and the source CSV files themselves as a python package.  This then allows you to install the package with pip:

~~~sh
pip install chicago
~~~

and then use it to access neighborhood names in your code:

~~~py
import chicago

THREADS_TOPICS = [n.name for n in chicago.NEIGHBORHOODS]
~~~

This is an example of using a mundane programming task, reading names from a CSV file, to learn something less mundane: implementing a Python package. It's probably a daunting task to do something more difficult programatically and also learn how to package that code, but this task leaves plenty of space to learn new things in a short time.

This task also is a good opportunity for practicing refactoring by breaking the code for proccessing the CSV into classes and implementing logic that makes it easy to handle differences between different source CSVs.

## Repository

You can see the full source code of the python-chicago package [on GitHub](https://github.com/newsapps/python-chicago).



