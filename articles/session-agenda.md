---
title: SRCCON 2015 Session Agenda
description: Talking points and topics for the SRCCON session on Mundane Programming
---


[Original proposal](http://srccon.org/sessions/#proposal-106215):

> Programming creates so many technical and creative inventions that it's natural for aspiring programmers to dream of big projects in the cloud. But this ambition ignores the actual goal of programming, which is almost completely about making machines do mundane work. And it is counterproductive to learning how to program, which requires consistent practice as in every other form of literacy and art. So this session will be about mundane programming. Programming not to be the next Zuckerberg, or to get a better job 3 months from now, but to make today or just the next ten minutes more enjoyable. Instead of focusing specifically on how to code, we'll expand upon the reasons of why we code (though seeing is often believing when it comes to code, so feel free to bring both ideas and Gists). And we'll trim the personal prerequisites of programming, which don't include being an entrepreneur, having a profitable idea, building a website, contributing to open source, or changing the world or your career. Programming can be learned, and done, with a willingness to learn and a wide variety of small problems to practice upon.


## Topics

(Status: currently a brain dump)

Discussion: If you reach whatever you imagine is "competency" in programming, what do you imagine you'd be doing with it?

What do you currently do with programming? How often do you do it? How often do you think to reach for it as a tool to solve any given day-to-day problem?

What friction or barriers are there between you _thinking_ about programming (or even just opening up your text editor) and you _actually_ programming?


## Demos

### Simple

#### curl

- Use __curl__ to fetch the raw text of a webpage
- Doesn't have to be a webpage; Chrome Web Inspector will show you the `curl` command to emulate any given web request. Some API panels will also provide copy-paste examples, such [as Twilio for sending a text message](https://www.twilio.com/user/account/developer-tools/api-explorer/message-create).
- Use curl to get the status code of a response
- Use curl to get the redirected destination of a shortened URL -- useful for seeing if a URL is phishy without risking getting hit by a JavaScript attack.
- Use curl in combination with
- Once you've figured out curl, emulate some of its behavior in Python, or scripting language of choice.


#### Google Geocode

In many situations, a programming task will involve far more time reading documentation and studying a domain, rather than actual code writing.

- Reading documentation is often more effective for solving your problem than pure programming knowledge. Here are the [Google docs for doing a latitude/longitude lookup.](https://developers.google.com/maps/documentation/geocoding/#geocoding)
- You should always explore an API the "old-fashioned way" if possible. Don't just [curl this endpoint right away; visit in your browser, first](https://maps.googleapis.com/maps/api/geocode/json?address=100+Broadway+New+York,NY).
- Now that you've seen what that URL looks like in your browser, `curl` it from the command-line:
  
        curl https://maps.googleapis.com/maps/api/geocode/json?address=100+Broadway+New+York,NY

- Pick out the latitude and longitude by eyeballing it. If you needed to geocode something to save your life __right now__...well, congrats, you've done it.
- Eyeballing that lat/lng data is kind of a chore, if you're doing it more than once. Now figure out a way to have the computer do it for you.


### More complicated

#### Assessing California schools

[California posts the SAT/ACT/AP performance of its schools in the past 15 years](http://www.cde.ca.gov/ds/sp/ai/). There's nothing wrong with clicking each of those individual hyperlinks -- all 45 of them -- and then waiting for them to download. And then opening each of them, carefully highlighting and copying the thousands of rows and columns in each of them, and pasting them into a combined spreadsheet. But unless analyzing their SAT/ACT/AP performance is a matter of immediate national/job security, this is a great time to practice some mundane coding.

A similar data project: [compiling vaccination data for California's kindergartens](https://www.cdph.ca.gov/programs/immunize/Pages/ImmunizationLevels.aspx).


Note: projects aren't a great example of "mundane programming"; though successfully doing them is a result of practiced mundane programming. You should focus on writing code to do selfish chores before trying to save the world with code.



##### Example from Twilio:

via their [API explorer for the message-create endpoint](https://www.twilio.com/user/account/developer-tools/api-explorer/message-create):

~~~sh
curl -X POST \
'https://api.twilio.com/2010-04-01/Accounts/YOURACCOUNTID/Messages.json'  \
--data-urlencode 'From=+15553675309' \
-u YOURACCOUNTID:[AuthToken]
~~~


