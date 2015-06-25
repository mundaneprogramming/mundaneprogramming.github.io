---
title: Finding text within a group of images
description: |
  You remember documenting a website by taking screenshots. But how do you search by text?
featured: true
rank: 7
authors:
  - dannguyen
keywords:
  skills:
    - Image processing
    - Command line interface
---

How do you find text in images?

https://github.com/madmaze/pytesseract

![image](/files/images/tess/nytimes.com.201506231100.jpg)


~~~python
from PIL import Image
import pytesseract
fname = './files/images/tess/nytimes.com.201506231100.jpg'
img = Image.open(fname)
print(pytesseract.image_to_string(img)))
~~~


The header. The styled text was poorly translated, including the New York Times logo. But everything else is legible. There's a few spacing problems, `US.` and `NewYork` instead of `U.S.` and `New York`, respectively. It does capture the `SHOP THE NEW COLLECTION` in the Cartier ad.

~~~
U.S. INTERNATIONAL

(;,,.,,-H. (7.l1)eNv21n ﬂork Eimes  (;,,.,,.(,,.

!.I.§.
  
Tuesday, June 23, 2015 El Today's Paper I4 Video 87°F Nasdaq 0.00% 1

World US. Politics NewYork Business Opinion Technology Science Health Sports Arts Style Food Travel Magazine Real Estate ALL

Q/we/«
L

(70//er/1'0/'1 P0/'/Lu bi/1-if’//’ ll?/gz/6

> SHOP THE NEW COLLECTION
~~~


The full result:

{% include snippets/codepiece.html relpath="snippets/nytimes.com.tess.txt" parentdir="examples/"%}



