---
title: Mirror a single page and its links
rank: 3
---


This is useful for saving a page and its links



Mirror single page

~~~sh
wget  --recursive \
      --level=1 \
      --adjust-extension \
      --convert-links \
      --span-hosts \
      --page-requisites \
        http://fortherecord.payments.us.gsk.com/hcppayments/archive.html
~~~


http://fortherecord.payments.us.gsk.com/hcppayments/archive.html

