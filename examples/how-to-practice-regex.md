---
title: How to practice regular expressions
description: Regexes are incredibly powerful. But they are (initially) as boring as they sound. Here's how to go about finding ways to practice them daily.
authors:
  - dannguyen
---

## Get a text editor





~~~
 [ [ 4, 4, 6, 11, 24, 24, 24, 24 ],
        [ 4, 5, 6, 16, 24, 24, 24, 24 ],
        [ 6, 6, 14, 24, 24, 24, 24, 24 ],
        [ 11, 16, 24, 24, 24, 24, 24, 24 ],
        [ 24, 24, 24, 24, 24, 24, 24, 24 ],
        [ 24, 24, 24, 24, 24, 24, 24, 24 ],
        [ 24, 24, 24, 24, 24, 24, 24, 24 ],
        [ 24, 24, 24, 24, 24, 24, 24, 24 ] ];
~~~

```
 *([\[\]]) *
```

~~~
[[4, 4, 6, 11, 24, 24, 24, 24],
[4, 5, 6, 16, 24, 24, 24, 24],
[6, 6, 14, 24, 24, 24, 24, 24],
[11, 16, 24, 24, 24, 24, 24, 24],
[24, 24, 24, 24, 24, 24, 24, 24],
[24, 24, 24, 24, 24, 24, 24, 24],
[24, 24, 24, 24, 24, 24, 24, 24],
[24, 24, 24, 24, 24, 24, 24, 24]];
~~~

```
^(?=\[\d)
```


Done:

~~~
[[4, 4, 6, 11, 24, 24, 24, 24],
 [4, 5, 6, 16, 24, 24, 24, 24],
 [6, 6, 14, 24, 24, 24, 24, 24],
 [11, 16, 24, 24, 24, 24, 24, 24],
 [24, 24, 24, 24, 24, 24, 24, 24],
 [24, 24, 24, 24, 24, 24, 24, 24],
 [24, 24, 24, 24, 24, 24, 24, 24],
 [24, 24, 24, 24, 24, 24, 24, 24]]
~~~



### Rename stuff

```
dan daniel dani DAN 
rodan dan dandan daniel dan
daniel danny Dan danielle
```

Rename all "dan" as "daniel"



### Find and select and copy

Cmd-Option-F
regex a pattern
Find-All, Cmd-C
