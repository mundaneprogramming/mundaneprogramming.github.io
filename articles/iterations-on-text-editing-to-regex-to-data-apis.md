---
name: A Mundane Setup, from Learning how to Use A Text Editor to Automated API Scraping
---


### 1. Activate Find

__Find__ -> __Find__...

__Cmd-F__

### 2. Do a regex

      twitter.com/\w+

### 3. Change the selection to Find All

Hit the __Find All__ button.

__Option-Return__

### 4. Copy to Clipboard

Menu: __Edit -> Copy__

__Cmd+C__


### 5. Open a new window

Menu: __File -> New File__

__Cmd+N__

### 6. Paste into the New Window

Menu: __Edit -> Paste__

__Cmd+V__


### 7. Remove the Twitter handles

Menu: __Find -> Replace...__

__Cmd+Option+F__

Find: 

    twitter.com/

Replace:

    [nothing]

### 8. Undercase them

      (\w+)

      \L\1

### 9. Save the file

And you're done

-----------------

# Iteration 0
How to use text editor
How to save a list as text file

# Iteration 1

How to do Find and Replace
How to do charactersets
How to do Backreferences

# Iteration 2

- Lookbehinds
- All keyboard

# Iteration 3 - Command Line


# Iteration 4 - Through Python


# Iteration 5 - Through the Internet

----------------------


# Iteration 6 - Look ahead, multiple regexes, pages/then ids, alternation

# Iteration 7 - sed 

# Iteration 8 - Through Python and the Internet

# Iteration 9 - Through web scraping

# Iteration 10 - Adding Facebook API








--------------

Things you haven't been able to do:

- Sort them
- Remove duplicates
- 

