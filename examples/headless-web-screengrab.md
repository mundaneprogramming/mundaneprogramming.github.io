---
title: Automated webpage screenshots with CasperJS
description: |
  The problem with non-browser tools is that, well, they don't act like browsers. "Headless" programs provide some of the functionality of a full-fledged web browser for automated systems (such as testing, or mass screenshot grabbing)

routine:
  - Open browser.
  - Visit URL.
  - Activate screencapture program.
  - Highlight area of browser to capture.
  - Rename/move resulting screencapture image file.

authors:
  - dannguyen
files:
  - name: code/casper_capture.js
    description: Uses CasperJS combined with PhantomJS to take a screenshot.
---





// sample URL http://ogesdw.dol.gov/homePage.php
// http://stackoverflow.com/questions/26517852/taking-reliable-screenshots-of-websites-phantomjs-and-casperjs-both-return-empt



The [PastPages project](http://www.pastpages.org/) takes snapshots of news homepages and tracks stories.


CasperJS is often used for automated visual testing, such as seeing [what a site looks like across different device dimensions](http://www.phase2technology.com/blog/using-casperjs-capture-method/).




Use minimist: https://www.npmjs.com/package/minimist

```
 npm install -g minimist
```


http://www.smashingmagazine.com/2014/02/12/build-cli-tool-nodejs-phantomjs/
