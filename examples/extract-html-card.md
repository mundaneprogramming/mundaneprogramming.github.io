---
title: Extract useful metadata from a web article
description: Just how do they make those Flipboard/Twitter/Facebook previews anyway
todos:
  - Take facebook screenshot
  - Do simple web parsing
---


Sample URL:

https://www.themarshallproject.org/2015/07/02/is-google-more-accurate-than-the-fbi

Sample Slack preview:

![image](/files/images/screenshots/slack-marshallproj-preview.png)


![image](/files/images/screenshots/twitter-marshallproj-preview.png)



### Facebook linter

https://developers.facebook.com/tools/debug/

https://developers.facebook.com/tools/debug/og/object?q=https%3A%2F%2Fwww.themarshallproject.org%2F2015%2F07%2F02%2Fis-google-more-accurate-than-the-fbi


![image](files/images/screenshots/fblinter-marshallproj-foundtags.png)

![image](files/images/screenshots/fblinter-marshallproj-opengraph.png)

![image](files/images/screenshots/fblinter-marshallproj-preview.png)


What does Facebook's scraper see?

https://developers.facebook.com/tools/debug/og/echo?q=https%3A%2F%2Fwww.themarshallproject.org%2F2015%2F07%2F02%2Fis-google-more-accurate-than-the-fbi

Raw mirror file: [file](/files/htmls/fb-linter-marshallproj-article.html)

