---
layout: post
title:  "Where do we start refactoring a large method?"
categories: refactoring
---
#### We see a large method.
#### Our mouth waters (or not).
#### We could nip at it from so many places.
#### Where do we start?

Have you been here?

"Where do we start?"

Sometimes we confuse ourselves with the question.
Sometimes it is an ensemble session that is confused. Everyone seems to want to refactor a different part of the code.
And that is not the worst of it. Sometimes we refactor out large blocks of code too early and end up with less than ideal abstractions.

So, again, where do we start?

Sandro Mancuso suggests we start with statements
nested most deeply within our code.

> Start refactoring from the deepest branch

The deepest branch gives us a small, localised problem to solve.
There are fewer dependencies to deal with, like those pesky global variables.
Not only that,
it is likely that the deepest parts of the code will be expressing
details that don't belong in the method.
Details that will be violating Uncle Bob's
"One Level of Abstraction per Function" rule.

As lower levels of detail are refactored out,
patterns the express the methods true intent should emerge.
Once we see those patterns in the clear,
we can come up with better abstractions.

Sandro demonstrates the technique in the following video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/_NnElPO5BU0?start=1973" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>