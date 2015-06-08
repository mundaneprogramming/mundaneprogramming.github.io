---
title: Fetch latest updates on Texas death row
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

The third variation of the script is only slightly more complicated: instead of just doing a day count, it returns all the relevant meta data about the executions, such as the condemned's name, age, and case file. As you get into the business of making apps, you'll find that it's worth taking the extra step to structure the scraped information.




