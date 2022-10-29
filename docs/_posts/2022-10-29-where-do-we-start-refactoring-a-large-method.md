---
layout: post
title:  "Where do we start refactoring a large method?"
categories: refactoring
---

#### We see a large method and decide to refactor.
#### There is so much to nip away at.
#### Where do we start?

Difficult question. That, and if this has happened to you, you may also know that if we pick a less than ideal place, we may end up with abstractions that also less than ideal.

So, again, where do we start?
Sandro Mancuso suggests we start with statements
nested most deeply within our code.

> "Start refactoring from the deepest branch"

The deepest branch gives us a small, localised problem to solve.
There are fewer dependencies to deal with, like those pesky global variables.
Not only that,
it is likely that the deepest parts of the code will be expressing
details that don't belong in the method.
Details that will be violating Uncle Bob's
"One Level of Abstraction per Function" rule.

As we nip away at those details,
patterns that express the methods true intent should emerge.
Once we see those patterns,
we can come up with better abstractions.

Sandro demonstrates the technique in the following video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/_NnElPO5BU0?start=1973" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The specific frame that I often find myself looking for:

<center><img src="/assets/images/start-refactoring-from-the-deepest-branch.png" width="600" alt="The Leader's Handbook - Debundling Process"></center>