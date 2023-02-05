---
layout: post
title:  "Leveraging 1x1 production to improve flow"
tags: lean
---
> In its ideal, 1x1 production means that parts move from one value-adding processing step directly to the next value-adding processing step, and then to the customer, without any waiting time or batching between those steps. — Toyota Kata, Mike Rother

In software development, 1x1 production, or a work-in-progress (WIP) of one, can be achieved by working together (mob programming) on a feature or story, instead of assigning distinct tasks to individuals within a team.

Numerous benefits of 1x1 production are usually experienced out of the box. To take an example, we might see improved quality since code is reviewed continuously and ideas from team members are integrated on the fly. This has knock-on effects: fewer bugs are produced and there is less rework. With less rework, the team can focus on value-added tasks, such as incorporating feedback from customers to make the product even better. Better products create profit.

### Seeing the rocks

The real power of 1x1 production however lies in its ability to expose problems that impede the flow of work. The idea is described in Taiichi Ohno’s _Toyota Production System_ as:

> Lowering water level in a river to be able to see the rocks.

Once we can see the rocks, we can chip away at them to improve flow.

In a single-piece flow, obstacles slow down the entire production since there is only ever one thread of work that is active. To improve flow the obstacle must be removed. If a more severe obstacle arises it can shut down production entirely. This may seem scary, but that is the intended effect: the only way forward is to correct the problem.

A system in such a state over an extended period of time can be said to be "Continuously Improving".

The contrary of a system that is continuously improving is one that attempts to make progress by starting multiple tasks in parallel. Progress is only illusory as the work done is merely firefighting to untangle the simultaneous threads of work e.g. code waiting to be reviewed, merge conflicts to be resolved, components developed in parallel that require rework since they don’t integrate as expected. In all this noise, the real problems go undetected and unresolved.

According to Mike Rother, such workarounds reveal a "make production" rather than an improvement mindset. The natural reaction of such a system when work gets blocked is to start more work in parallel, throwing the system into non-improving spiral.