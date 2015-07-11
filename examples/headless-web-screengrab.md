---
title: Automated webpage screenshots with PhantomJS
description: |
  The problem with non-browser tools is that, well, they don't act like browsers. "Headless" programs provide some of the functionality of a full-fledged web browser for automated systems (such as testing, or mass screenshot grabbing)

featured: true
rank: 4

the_usecase: |
  I wanted a way to quickly screencap good and bad examples of fancy web graphics. However, using __wget__ doesn't work because wget won't execute the JavaScript that's often used in modern web visualizations. Using PhantomJS, I create a command-line script that can _act_ like a web browser without me having to open up an actual browser.
the_routine:
  - Open browser.
  - Visit URL.
  - Activate screencapture program.
  - Highlight area of browser to capture.
  - Rename/move resulting screencapture image file.

authors:
  - dannguyen
files:
  - name: code/phantomscreencap.js
    description: A PhantomJS command-line script that visits a URL and takes a screenshot of the rendered site.
  - name: code/casper_capture.js
    description: Uses CasperJS, a testing framework that sits atop PhantomJS, to take the screenshot. Turns out to be more overhead than it's worth.

related_links:
  - title: PhantomJS Examples
    url: http://phantomjs.org/examples/
  - title: How To Build A CLI Tool With Node.js And PhantomJS 
    url: http://www.smashingmagazine.com/2014/02/12/build-cli-tool-nodejs-phantomjs/ 
  - title: "StackOverflow: how to ignore errors in phantomjs"
    url: http://stackoverflow.com/a/19538646/160863
  - url: http://www.phase2technology.com/blog/using-casperjs-capture-method/
    title: Using CasperJS Capture Method
  - title: "Render not honoring viewport size · Issue #10619 · ariya/phantomjs · GitHub (github.com)"
    url: https://github.com/ariya/phantomjs/issues/10619
  - title: "Web Fonts do not render, use fallback fonts instead. · Issue #10592 · ariya/phantomjs · GitHub (github.com)"
    url: https://github.com/ariya/phantomjs/issues/10592

---




## wget isn't good enough

Check out the rad graphics on the [U.S. Department of Labor's Data Enforcement homepage](http://ogesdw.dol.gov/homePage.php):

![image](/files/images/screenshots/ogesdwdol.png)

I'd like to archive that gem, along with a list of many other sites. But it's a tedious pain to open each page and snapshot it. You [might think that using __wget__](/examples/wget-snapshot) would suffice. But the graphics on the Labor Dept. page are rendered dynamically via JavaScript. If you're new to web development, this means there's no direct URL to an image file.

If you take a [wget snapshot](/examples/wget-snapshot):

~~~sh
wget -E -H -k -K -nd -N -p\
  -P /tmp/ogesdw \
  http://ogesdw.dol.gov/homePage.php
~~~

You'll find that the dynamic parts of the page don't get mirrored:

![image](/files/images/screenshots/ogesdwdol-wget-broken.png)


Using the {% include github-link.html filename="code/phantomscreencap.js" %} command-line script:

~~~sh
phantomjs phantomscreencap.js http://ogesdw.dol.gov/homePage.php
~~~

We get a screenshot like this:

![img](/files/images/phantomjs/ogesdw_dol_gov_homepage_php.2015-07-04T202404.jpg)

OK, that introduced a few other problems, but at least it rendered the JavaScript-powered visualizations.


## Headless browsing with PhantomJS

[PhantomJS](http://phantomjs.org/) is "is a headless WebKit scriptable with a JavaScript API." For us, it means it's a way to have programmatic access to a web browser. So instead of opening up a web browser, then visiting a webpage, just to see how long it takes to load (after everything is loaded and rendered), we can [write a script to do all that webpage rendering](https://github.com/ariya/phantomjs/blob/master/examples/loadspeed.js), _without opening up the web browser_ and clicking around. See [more examples here](http://phantomjs.org/examples/).

So PhantomJS is great if you ever need to open a lot of web pages or access them in a bulk/batch fashion. The [PastPages project](http://www.pastpages.org/), which archives news sites' homepages, uses PhantomJS to take the snapshots.



## Demonstration 

Using {% include github-link.html filename="code/phantomscreencap.js" %}, the basic usage is:

~~~sh
phantomjs phantomscreencap.js http://www.example.com
~~~

Output:

~~~
Options:
{ url: 'http://www.example.com',
  format: 'jpg',
  output_filename: 'www_example_com.2015-07-04T190333.690Z.jpg',
  quality: 75,
  dim: { width: 1200, height: 900 } }
~~~


By default, the screenshot will be output to a timestamped filename based off of the URL, e.g. `www_example_com.2015-07-04T190333.690Z.jpg`

## Problems

Basically, web stuff is a whole new world of complexity. And because PhantomJS isn't, well, a full-service browser with hundreds of engineers working on it, its rendering of modern webpages will sometimes be significantly different than expected.

### Can't lock the viewport

Here's part of the [www.drudgereport.com](http://www.drudgereport.com) snapshot; because of the complexities of web-rendering, my attempt to affix the viewport at 1200x900 pixels doesn't quite work. So this is just a crop:

![drudge.comimage](/files/images/phantomjs/phantomjs-www_drudgereport_com.jpg)

### No fancy webfonts

Webfonts won't be rendered, so [sites with fancy fonts won't appear exactly as intended](https://github.com/ariya/phantomjs/issues/10592). Here's [www.nytimes.com](http://www.nytimes.com) as seen by PhantomJS:

![nytimes.comimage](/files/images/phantomjs/phantomjs-www_nytimes_com.2015-07-04T194150.jpg)

Here's what www.nytimes.com is _supposed_ to look like, with its web fonts rendered by the Google Chrome browser:

![nytimes screenshot](/files/images/phantomjs/nytimes-real-screenshot.jpg)



### CasperJS

[CasperJS is a framework](http://casperjs.org/) that sits atop PhantomJS and is intended to make it easier to write automated visual testing, such as seeing [what a site looks like across different device dimensions](http://www.phase2technology.com/blog/using-casperjs-capture-method/). I used it in the {% include github-link.html filename="code/casper_capture.js" %} example but it turns out to be more complicated than I needed. The killer problem for me was the [trouble getting CasperJS to deal with HTTPS sites](http://stackoverflow.com/questions/26415188/casperjs-phantomjs-doesnt-load-https-page), which is the result of flaws in other parts of the web tech stack.




