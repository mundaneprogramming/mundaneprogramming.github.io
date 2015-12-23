---
title: Archive a single webpage and its visual elements
rank: 3
description: |
  Take a basic snapshot of a webpage and the stylesheets and images used in its visual presentation.
authors:
  - dannguyen
---

~~~sh
wget --page-requisites \
     --span-hosts \
     --no-directories \
     --adjust-extension \
     --convert-links \
     --backup-converted \
     --timestamping \
     --directory-prefix=flair.myfloridacfo.com.cvphsrch.htm \
     http://flair.myfloridacfo.com/approot/dispub2/cvphsrch.htm
~~~



See a [full description of the flags and options in this gist](https://gist.github.com/dannguyen/03a10e850656577cfb57).
