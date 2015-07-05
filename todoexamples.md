---
title: The Examples Todos
layout: listing
---
{% capture markdownblk %}
This site is not intended as a reference for best coding practices or universally useful scripts, but rather, a collection of _examples_ of the kinds of small, mundane tasks that we can try to program for, and the (often sloppy) design decisions and compromises that go into such one-off work.

The source code of the scripts is included &ndash; because, why not? &ndash; but they aren't guaranteed to work as-is, __so you copy-paste-execute at your own risk__.
{% endcapture %}
{{ markdownblk | markdownify }}
<!-- probably should make this blurb appear at the bottom of every example/recipe page -->

## Examples
{% include snippets/examples-table.html pagetype="example"%}

## Projects

{% include snippets/examples-table.html pagetype="project" %}
