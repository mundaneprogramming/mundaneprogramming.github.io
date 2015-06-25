---
title: Combining text files
description: |
  In many real world situations, data is not only dirty, it's not even in a condition for any single program to deal with.
---



## Just `cat`

The Unix operating system has long had the simple __cat__ program, which has no other ambition than to take a list of files given to it and then to combine, or concatenate their streams:

~~~sh
cat file1.txt file2.txt > all.txt 
~~~

In some situations, this is actually good enough, and even the most skilled practitioner will first think of `cat` as a first resort.

### Combining state SSA baby name files

TKTK


### 

However, while `cat` takes care of the combining part, at the file level, it is as singular and inflexible of tool as they come. It does nothing when data needs to be added at a _line-by-line_ level.

TKTK: Show state example
