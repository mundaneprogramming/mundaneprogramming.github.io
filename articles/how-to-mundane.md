---
title: What to learn and etc.
---

# How to learn?

Basically, learn how to debug.

# Is it worth the time?
Maybe.


## Things to focus on

- Debugging
- Learning the command-line
- Learning OS hacks
- System environment
- Working with and deserializing text files
- Github
- Designing a user (text-based) interface
- Understanding do-one-thing-do-it minimalism
- Learning APIs
- Integrating new libraries
- Refactoring code
- Some error handling
- Self-documenting code style
- Following best practices in style
- Reducing file clutter
- Creating environments

## Things to not worry about

- Object-oriented programming
- Web publishing
- Test driven development
- Documentation (in the form of comments)
- Complete DRY
- Optimization
- Big O notation
- Feature creep

## Learn one, or two new things at a time. 
Don't replace your whole process. For example, this [thorough webscraping tutorial](http://newcoder.io/scrape/) might be _too_ thorough, as it introduces:

- Setting the Scraper environment
- Building the project folder
- Using SQLAlchemy
- Setting up Posgres
- Writing the parser
- Writing the spider
- Setting up cron

Focus on one thing at a time. Figure out the parser. And just use that. Then move on to spidering. And then move to deserialization. And then, later, to databases.


# Things to do

1. Put the Terminal icon on your dock
2. Enable opening from Terminal from Finder
3. Use Tab for auto complete
4. (put this as 1) Learn the keyboard shortcut for Application switching
5. Download a text editor
6. Enable syntax highlighting
7. Run script files from the command line
8. Open iPython
9. Use the %paste
10. Cmd-C for Copy
11. Cmd-V for paste
12. head and tail
13. curl a file instead of downloading
14. grep a text file for text
15. (move higher) Cmd-S for Save
16. Find and replace with regex
17. Grep with regex
18. Keyboard short cut for history
19. Cmd-W to close a window
20. Cmd-F to Find in a document
21. Cmd-F-Shift in a project
22. How to open a text file
23. How to write a text file to disk
24. How to download and read a file from Python
25. How to download and save a file from Python
26. How to parse CSV from basic functions
27. How to parse JSON
28. How to convert JSON into CSV 
29. How to rename a file

# Goals

- Don't touch your mouse
- Look for efficiencies. Things like syntax-hilighting are incredibly important
  - Compare autocompletion and highlight in Sublime vs textpad
- Stop hard-coding things
- 

# Concrete skills

- Visual recognition
- Regex
- xpath
- Keyboard shortcuts
- CSS selectors
- JSON/CSV serialization
- cronjobs
- Remote deployment
- Multithreading



### How to build interfaces

[The beauty of grep](https://medium.com/@rualthanzauva/grep-was-a-private-command-of-mine-for-quite-a-while-before-i-made-it-public-ken-thompson-a40e24a5ef48)

### Visual acuity

One of the must-read examples of code is Peter Norvig's spell-checker in 21 lines. It's in Python but he has links to translations in every other major language.

http://norvig.com/spell-correct.html

~~~py
splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
~~~

~~~py
splits = []
for i in range(len(word) + 1):
  a = word[0:i]
  b = word[i:-1]
  splits.append((a, b))
~~~


https://www.youtube.com/watch?v=1juW3dDQ968
