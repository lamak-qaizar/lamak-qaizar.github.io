---
layout: post
title:  "Why mob programming works"
tags: mob-programming
---
### Are we underestimating the complexity of writing code?
We must remember to write a failing test first.
Not to refactor in the red.
To refactor when we get to green.
Not to fall into the refactoring rabbit hole.
To keep in mind all the patterns and principles
e.g. SOLID, Object Calisthenics and DRY.
To keep in mind business context.

That is not all of it.
And yet, that is already a lot of things to juggle in our minds when we write code.
Can we expect an individual to do all this?
And do a good job of it?

### Programs must not only work well, they must read well too
Martin Fowler says:
> Any fool can write code that a computer can understand.
> Good programmers write code that humans can understand.

When we mob program, we make no assumptions about whether
the code is easy to understand. For those that have programmed with us, 
it is already understood.

### Flow efficiency vs. individual efficiency
When individuals are kept busy, work has to wait;
PRs wait to be reviewed, blockers wait to be removed.
Therefore, optimizing for individual efficiency seldom (or never?)
leads to flow efficiency.
When we mob, we are optimizing for flow.
Work is no longer has to wait for an individual to be available,
When an individual isn't available, work still goes on.

### It is a natural WIP constraint
> The Theory of Constraints, Lean production or the Toyota Production System, and Total Quality Management. Although each movement started in different places, they all agree on one thing: WIP is the silent killer.
> -- The Phoenix Project

Enough said?

### Issues get debugged at super sonic speeds
What do we do when an incident occurs? We swarm.
Somehow we are able to get to the bottom quicker 
than if an individual were at it.
When we are coding, we often run into issues as well,
e.g. a typo, a logical error or
just being unable to get a dependency to work.
When we're coding together,
we're effectively swarming on these issues as well.
Safe to assume then that they are being resolved much more quickly as well?

### If someone gets hit by a bus
