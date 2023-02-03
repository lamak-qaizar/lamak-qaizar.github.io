---
layout: post
title:  "Leveraging one-piece production to improve flow"
tags: lean
---
> What is one-piece production? In its ideal, one-piece production means that parts move from one value-adding processing step directly to the next value-adding processing step, and then to the customer, without any waiting time or batching between those steps. — Toyota Kata, Mike Rother

In software development, one-piece production, or a work-in-progress (WIP) of one, can be achieved by working together (mob programming) on a feature or story, instead of assigning distinct tasks to individuals within a team.

Numerous benefits of one-piece production can be experienced out of the box. To take an example: we might see improved quality since code is reviewed continuously and ideas from team members are integrated on the fly. This has knock-on effects: fewer bugs are produced and there is less rework. With less rework, the team can focus on value-added tasks, such as incorporating feedback from customers to make the product even better. Better products create profit.

The real benefit of one-piece production however lies in its ability to the expose problems and obstacles that impede flow. The idea is described in Taiichi Ohno’s _Toyota Production System_ as lowering water level in a river to be able to see the rocks. Once we can see the rocks, we can chip away at them to improve flow.

Whenever an impediment arises during a one-piece production workflow, it is as clear as daylight since it stops or slow down the entire production. The way forward then is to correct the problem and improve the system. A system in such a state over an extended period of time can be said to be “Continuously Improving”.

The contrary of a system that is continuously improving is one that attempts to make progress by starting multiple work in parallel. Progress is only illusory, as all the activity is really constant firefighting to untangle all the threads that have been started in parallel e.g. code that is waiting to be reviewed, merge conflicts need to be resolved, components that have been developed in parallel but now require rework since they don’t integrate as expected. The real problems that caused work to start work in parallel in the first place go unresolved and the system falls into a non-improving cycle.

Worse still, whenever work gets blocked, the natural reaction of such a system is to start even more work in parallel. This throws the system into self-defeating spiral. According to Mike Rother, such workarounds reveal a "make production" rather than an improvement mindset.