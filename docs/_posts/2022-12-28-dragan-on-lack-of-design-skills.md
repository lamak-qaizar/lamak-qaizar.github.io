---
layout: post
title:  "Dragan on lack of design skills"
tags: software-design
---
The following is a message shared on the company's internal messaging app
by [Dragan Stepanović](https://www.linkedin.com/in/dstepanovic)
while we worked together at Careem.
It was around 2018 or 2019.
I have referred to it time and time again
having also kept a copy of it for reference.
Sharing it here if it benefits anyone else.

The message follows...

---

Lack of proper design skills leads to setting up wrong service
boundaries and lots of the distributed systems I’ve seen in the wild 
end up as an entity service antipattern 
(see Michael Nygard’s [article](https://www.michaelnygard.com/blog/2017/12/the-entity-service-antipattern/) on this antipattern). 
This suboptimal design is reflected in high service coupling 
and lots of intertwined network dependencies.

This extends activation path (number of hops needed to fulfill end user request), 
which, in turn, increases response time for the end user request. 
That, as you go up the service call chain, drives call blocking time up, 
which drives upstream clients to increase the timeouts, 
which increases number of blocked request handling threads.
System hack around this is increasing number of scaled out instances, 
which introduces operational complexity and on the system level 
this drives costs up exponentially with the number of services. 

Anyway if anything goes down, you risk bringing down lots of the coupled 
functionality with that service as well. Not to mention team dependencies 
and increasing lead time to bring something out of the door 
(as soon as work leaves the team, lead time is by a magnitude longer), 
which hurts time to market and business bottom line at the end. 
Complexity around testing these kind of coupled services 
(integration, Consumer Driven Contracts etc.) 
is another topic caused by this root problem.

You would want to have such a service boundary 
that failure of this service causes graceful degradation of business functionality. 
E.g. if Recommendation Service on Amazon goes down, 
the only thing you won’t be able to do is to see recommended products 
for the one you’re looking at.

One heuristic I tend to use when trying to figure this out is asking: 
"What else will fail if this service fails?".

Try to imagine there’s just a single instance of every service 
you have in the system and think about how you would 
design the system so that the business impact is minimized 
in case of any service failure. 
Forget about circuit breakers, fallbacks, bulkheads, caches; 
they are addressing the symptom not the problem.
Microservices are a mean to an end, 
and you can achieve that end in a different way.

If we’re not able to make a modular monolith 
what makes us think we’ll be able to make modular microservices?
Most of the microservices implementation end up as 
distributed monolith which is way worse than a single process monolith 
from which migration started.

And yes, putting a bunch of events with a bunch of properties 
on Kafka is the same as having a huge monolith database 
where anyone can reach out and couple to anything. 
Note: Event Sourcing is a different thing; 
it’s not meant to be top a level architecture, 
for the stated coupling reasons, and should be applied to a single bounded context

**Takeaway is:** lack of a design skills reflects dramatically 
in reduced reliability of the distributed system 
and extended lead time to make a business impact.

If I was to advise a journey on this path of learning good design it would be: 

1. Low level (code) design and system design are very similar; 
start with Clean Code (accurate namings especially which leads 
to a better design because you gain more domain insights 
through this process of naming things the way they are)
2. Refactoring skills (Fowler’s book)
3. TDD (at one point tests are going to help you 
dramatically increase your design skills if you learn how to "listen to them")
4. Design patterns (a toolbox)
5. S.O.L.I.D.
6. 4 rules of simple design from Kent Beck 
7. GOOS book \[Growing Object-Oriented Software, Guided by Tests\]
8. Michael Feather’s book: Working Effectively with Legacy Code 
9. Then start with Domain-Driven Design 
(tactical: entities, value objects, aggregates etc. and then strategical patterns)
10. Read "Release It!" from Michael Nygard.

Unpopular opinion but lots of hyped technologies 
(e.g. service meshes, CDC, chaos engineering, gRPC) are a solution 
for problems caused by accidental, not essential complexity. 
Meaning, if you solve the right problem, you eliminate all the complexity 
caused by trying to solve a symptom rather than the cause.

-- Dragan Stepanović