---
layout: post
title:  "Where do we start refactoring a large method?"
tags: refactoring
---

> We see a large method and decide to refactor.  
> There is so much to nip away at.  
> Where do we start?

Has this happened to you? 
It is not only difficult picking a starting point, 
but if we pick a less than ideal place to start, 
the abstractions we end up developing may be no better. 

Sandro Mancuso suggests we start with statements
nested most deeply within our code.

<center><img src="/assets/images/start-refactoring-from-the-deepest-branch.png" width="500" alt="Start refactoring from the deepest branch"></center>

The deepest branches gives us small, localised problems to solve
where there are fewer dependencies to deal with.
It is also likely that the deepest branches will be expressing
details that don't belong in the method, i.e.
details that violate Uncle Bob's
'one Level of abstraction per method' rule.
As we nip away at those details,
patterns that express the methods true intent should emerge.
Once we start seeing those patterns,
we can come up with better abstractions.

Sandro demonstrates the technique in the following video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/_NnElPO5BU0?start=1973" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>