---
layout: post
title:  "Notes on Value-Stream Mapping"
tags: value-stream-mapping lean
---

> A value stream is the sequence of activities required to design, produce, and deliver a good or service to a customer. -- Value Stream Mapping by Karen Martin and Mike Osterling

Value-stream mapping is a technique that takes a holistic view of a 
value-producing system in order to reveal opportunities for improvement. 
John Shook and Mike Rother in _Learning to See_ state that most waste-reduction activities
fall through because they fail to see the whole, i.e. they skip the critical 
step of mapping the end-to-end value stream. 
The result is that one part of the system improves only for
wastes and bottlenecks to emerge in a step downstream.

Value-stream mapping comprises the following high-level activities. 
A separate value stream should be drawn for each product-family
(a set of products that have a high number of common processing steps). 

1. Pick a value-stream
2. Map the current state
3. Map the future (desired) state
4. Set goals and execute improvements
5. Repeat steps 2 through 5

Below we'll focus our attention on creating the current state map.

### The current state map
When mapping out a value-stream, the focus is on the "what", rather than the "how".
Karen Martin and Mike Osterling suggest that if map has more than 15 process blocks,
we should check if we are getting tangled up at the tactical level.
Tactical or process-level improvements are beyond the scope of value-stream mapping.

A mapping activity can be carried out through the following steps.
The sequence is not definitive -- it is just a workflow I have in mind as I prepare to do mapping activity.
1. List out all the activities (processes) and arrange them as a timeline.
2. Add actors involved in each activity
3. Add a symbol for inventory between processes (where it exists) along with the count of inventory
4. Add information systems (e.g. Jira, Notion) that each process uses
5. Add the following details to each process
   - Process time (PT) a.k.a. "touch time", the time that work is being worked upon
   - Lead time (LT), time inclusive of waiting
   - Percentage complete & accurate (%C&A), as reported by downstream process
   - Any additional metrics suitable to the value-stream
   - The barriers to flow (described below)

"Flow" is the movement of work from one process to the next without interruption or delay.
Following are some activities to look out for while listing barriers to flow:
- Non-value adding activities
- Back-flow due to defects
- Waiting
- Inventory
- Hand-offs
- Inspection
- Work that could be standardised or automated

### Summary metrics
Once the metrics of each activity are listed, they can be summarized into a table consisting of:
- Total process time (PT)
- Total lead time (LT)
- Activity ratio (PT/LT)
- Rolled %C&A (%C&A of each step multiplied together)

### Notation
This is an adapted notation that I used on an online white-boarding tool.

<center><img src="/assets/images/value-stream-mapping-symbols.png" width="600" alt="Value-stream mapping notation"></center>

### Example map
A sample diagram I drew with a client.

<center><img src="/assets/images/value-stream-mapping-sample.png" width="600" alt="Value-stream mapping sample diagram"></center>

### Common problems that a current state map may reveal
Karen Martin and Mike Osterling describe a set of common problems 
that current state mapping may reveal. They are listed below.

> - Loop-backs (sending back work to previous step)
> - Unnecessary hand-offs
> - Rework due to errors and lack of clarity
> - Batching
> - Functions missing or getting involved too early or too late in the process
> - Redundant activities
> - High variation in how work is performed
> - No documented standard work
> - Excessive inspection (review, approval, audits)
> - Overspecialization of staff
> - Existing technology is not fully leveraged
> - Under-utilization of skills
> - Compliance overkill
> - Delays due to juggling multiple responsibilities
> - Push and overburden