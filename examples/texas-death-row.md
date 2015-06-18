---
title: Fetch latest updates on Texas death row
authors:
  - dannguyen
  - Jane Eyre
  - Leland Junior
description: |
  An exercise in scraping and parsing HTML about criminal justice events.
featured: true
rank: 9
files:
  - name: code/count_days_since_texas_execution.py
    description: Reads the top row from the past executions list and parses the date value.
  - name: code/count_days_until_texas_execution.py
    description: Reads the top row from the scheduled executions list and parses the date value.
  - name: code/get_texas_scheduled_executions.py
    description: Instead of getting just the date value, this script returns JSON-formatted metadata about the most recent and next Texas execution.
---




The Texas Department of Criminal Justice publishes a variety of data about who it imprisons and executes, including lists on [past](https://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html) and [upcoming]( http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html) executions. 

Let's say you want a reminder of when the next execution comes up. Or how many days since the last one.

The third variation of the script is only slightly more complicated: instead of just doing a day count, it returns all the relevant meta data about the executions, such as the condemned's name, age, and case file. 





As you get into the business of making apps, you'll find that it's worth taking the extra step to structure the scraped information.

In this example, I've only done a small amount of work translating the HTML table columns into JSON attributes; for example, converting the `birthdate` attribute from `10/11/1969` to `1969-10-11`. The result of this script is a JSON file that can be read by a web app. I leave it to the web app designer to come up with their own "X days until John Smith, age 42, is executed" type message:

~~~json
{
  "next": {
    "exdate": "2015-06-18",
    "link": "http://www.tdcj.state.tx.us/death_row/dr_info/russeaugregory.html",
    "first_name": "Gregory",
    "race": "B",
    "birthdate": "1969-10-11",
    "last_name": "Russeau",
    "tdcj": "999430"
  },
  "previous": {
    "exdate": "2015-06-03",
    "link": "https://www.tdcj.state.tx.us/death_row/dr_info/bowerlester.jpg",
    "first_name": "Lester",
    "race": "White",
    "age": "67",
    "last_name": "Bower",
    "tdcj": "000764"
  }
}
~~~




