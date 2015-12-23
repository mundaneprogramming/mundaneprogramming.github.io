---
title: Download all files of a certain type from a single web page
rank: 2
---



Download all the pdfs

~~~
wget --recursive \
     --level 1 \
     --no-directories \
     --accept pdf \
     --ignore-case \
     --directory-prefix us.gsk.com.hcppayments
     http://fortherecord.payments.us.gsk.com/hcppayments/archive.html
~~~


Download all the xls,xlsx

~~~
wget --recursive \
     --level 1 \
     --no-directories \
     --accept xls,xlsx \
     --ignore-case \
     --directory-prefix cdph.ca.gov.immunization-spreadsheets \
     http://www.cdph.ca.gov/programs/immunize/pages/immunizationlevels.aspx
~~~

Offline-Mirror of a single page with single-site hierarchy

~~~sh
wget --recursive \
     --level 1 \
     --adjust-extension \
     --convert-links \
     --directory-prefix cdph.ca.gov.immunizationlevels.aspx \
     http://www.cdph.ca.gov/programs/immunize/pages/immunizationlevels.aspx
~~~


Offline mirror of a single page with multi-site hierarchy, one level of recursion

~~~sh
wget --recursive \
     --span-hosts \
     --level 1 \
     --adjust-extension \
     --convert-links \
     --directory-prefix CAPS-spanned-cdph.ca.gov.immunizationlevels.aspx \
     http://www.cdph.ca.gov/programs/immunize/Pages/ImmunizationLevels.aspx
~~~




