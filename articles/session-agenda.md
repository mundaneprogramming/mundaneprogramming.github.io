---
title: SRCCON 2015 Session Agenda
description: Talking points and topics for the SRCCON session on Mundane Programming
---


{% include snippets/toc.html %}

## Overall format

Assume audience is a wide range of programming ability and roles: j-school students, career-pivoting professionals, NICAR bootcamp attendees, recently-minted newsroom developer. Don't assume that everyone is or will be a journalist.

Some principles of mundane programming:

- __Programming requires constant practice__ - If you wait to use it on an "important" project, you won't be good enough to be effective, or worse, you'll doom the project. This negative feedback loop will result in you never having the motivation to program.
- __Code for yourself__ - Don't worry about making things for other people. If you are a human being, and you make something useful for yourself, chances are good that it will be useful for other people.
- __Repetition is important__ - Programming is an intellectual pursuit, but parts of it can be mechanical and reflexive, such as keyboard shortcuts, tab-autocomplete, and just being familiar with the general text patterns. Work on making those things as instinctive as muscle memory.
- __There's more to programming than programming__ - Programming is ultimately about filtering and organizing information, information created by real-world systems. The easiest way to learn about these systems is to reach out and touch them, such as via an API. If you can do this via programming, you'll expand both your knowledge of programming and about the complexities of data and institutions.




## Topics

(Status: currently a brain dump)

What do you currently do with programming? How often do you do it? How often do you think to reach for it as a tool to solve any given day-to-day problem?

What friction or barriers are there between you _thinking_ about programming (or even just opening up your text editor) and you _actually_ programming?


## Demos

Walkthroughs of turning daily tasks into code. For example, everyone knows how to visit a URL via their webbrowser.

### curl

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


#### Send a text message from Twilio

via their [API explorer for the message-create endpoint](https://www.twilio.com/user/account/developer-tools/api-explorer/message-create):

~~~sh
curl -X POST \
'https://api.twilio.com/2010-04-01/Accounts/YOURACCOUNTID/Messages.json'  \
--data-urlencode 'From=+15553675309' \
-u YOURACCOUNTID:[AuthToken]
~~~





### More complicated examples?



