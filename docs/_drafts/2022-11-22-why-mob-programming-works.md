---
layout: post
title:  "Why mob programming works"
tags: mob-programming
---
### Are we underestimating the complexity of writing code?
We must remember to write a failing test first.
To refactor only when we get to green.
But not to fall into the refactoring rabbit hole.
To code with all the patterns and principles in mind
e.g. SOLID, Object Calisthenics and DRY.
Oh, and we must make sure we're solving the business problem at hand.

That is not all of it.
Yet, that is already a lot of things to keep in mind when we write code.
It would be harsh to expect an individual to do all this and do a good job of it.
Mob programming helps spread some of these responsibilities.
If an individual forgets something, someone else can back them up.

### Programs must not only work well, they must read well too
Martin Fowler says:
> Any fool can write code that a computer can understand.
> Good programmers write code that humans can understand.

When we mob program, we make fewer assumptions about whether
the code is easy to understand. We are getting immediate feedback
about the understandability of the code as we write.

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

### Issues get debugged faster
What do we do when an incident occurs? We swarm.
Somehow we are able to get to the bottom quicker 
than if an individual were debugging.
When we are coding, we often run into issues as well,
e.g. a typo, a logical error or
just being unable to get a dependency to work.
When we're coding together,
we're effectively swarming on these issues as well.
It might be safe to assume then that these issues 
are being resolved much more quickly as well.