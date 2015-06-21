import re
RX = {
        "lorem": "lorem|etaoin?shrdlu|asdf|quick brown fox|blah|etc|\b[uh][hm]+\b",
        "todo": "tk|cq|to[\-_]?do|(?:[x?]{3,})",
        "lol": "lol(?:ol)*|lulz|wt[fh]|rtfm|lmao|rofl|\bw[au]t\b|ffs",
        "carlin": "\bass|arse|ass-?[fhks]|butt|anus|fu[\Wck]?k|shit|piss|cunt|\bcock|tit",
        "holy": "dam[mn]|god(?:d\b)|jesus|\bhell\b|heck|holy",
        "cuss": "douche|d[i1!]ck|boob|p[iu]ss|dildo|(?:re)?tard|whore|bi?tch|gay|porn",
        "neg": "anal|stupid|jerk|dumb|nazi|idiot|douche|suck|screw|moron|turd|wank|bull|funk|fubar|snafu|doof|whatev|d[uo]h",
        "ps": "[^aeioutrs_\s\W]{4,}.+",
        "doubles": r"\bthe\s+the\b|(?P<doubles>\b\w{5,}\b)\s+\b(?P=doubles)\b",
        "triples": r"(?P<triples>\b\w{1,4}\b)(?:\s+\b(?P=triples)\b){2,}"
    }

testtext = """
hello world
by Dan LOLOLOL
Tis now the very witching time of of of night,
When churchyards yawn and hell itself breathes out
Contagion[cq] to this world: now could I drink hot blood,
(what a wanker)
And do such bitter business as the the day
Ending goes a little or slow Lorem ipsum dolor sit amet, illum velit!
TODO: add stuff
(Shakespeare is a fukker)
The Great Gatsby (etc)
(kind of a dumb name)
In my younger and more vulnerable years my father father gave me some advice
that I’ve been turning over in my mind ever since.
"TK call dad tomorrow"
AWS_ID="AKJASD3787sajzzkOQURQqqz"
"""

print("\nnWithout case-insensitivity", '\n-----------------')
for key, rx in RX.items():
    for m in re.finditer(rx, testtext):
        print("%s:" % key, m.group())

print('\nWith case insensitivity', '\n-----------------')
for key, r in RX.items():
    rx = re.compile(r, re.IGNORECASE)
    for m in re.finditer(rx, testtext):
        print("%s:" % key, m.group())


print('\nLine-by-line with line numbers:', '\n-----------------')
for lineno, line in enumerate(testtext.splitlines()):
    for key, r in RX.items():
        rx = re.compile(r, re.IGNORECASE)
        for m in re.finditer(rx, line):
            print("%d:%s - %s" % (lineno, key, m.group()))


print('\nLine-by-line with full lines:', '\n-----------------')
for lineno, line in enumerate(testtext.splitlines()):
    for key, r in RX.items():
        rx = re.compile(r, re.IGNORECASE)
        for m in re.finditer(rx, line):
            print("%d:%s - %s" % (lineno, key, line))


print('\nLine-by-line with highlighted line context:', '\n-----------------')
for lineno, line in enumerate(testtext.splitlines()):
    for key, r in RX.items():
        rx = re.compile(r, re.IGNORECASE)
        for m in re.finditer(rx, line):
            a = line[:m.start()]
            b = m.group()
            c = line[m.end():]
            lx = ("%d:%s::" % (lineno, key)).ljust(15)
            ly = "%s __%s__%s" % (a, b, c)
            print(lx + ly)



