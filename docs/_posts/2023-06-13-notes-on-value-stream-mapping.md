---
layout: post
title:  "Notes on Value-Stream Mapping"
tags: value-stream-mapping lean
---

> A value stream is the sequence of activities required to design, produce, and deliver a good or service to a customer, and it includes the dual flows of information and material. -- Value Stream Mapping by Karen Martin and Mike Osterling

Value-stream mapping is a technique that helps reveal opportunities for
improvement in a production system. 
John Shook and Mike Rother in _Learning to See_ state that most waste-reduction activities
fall through because they jump the critical step of mapping the 
end to end value stream. Although well-intentioned, 
the result is that one part of the stream improves only for
wastes and bottlenecks to emerge in a step downstream.
Without a holistic view and approach, an organisation may fail to achieve
lasting quality improvements and cost savings.

Value-stream mapping comprises the following high-level activities. 
A separate value stream should be drawn for each product-family
(a set of products that have a high number of common processing steps). 

1. Map the current state
2. Map the future (desired) state
3. Set goals and execute improvements
4. Repeat

Below we'll focus our attention on creating the current state map.

### The current state map
When mapping out a value-stream, the focus is on the "what", rather than the "how".
Karen Martin and Mike Osterling suggest that if map has more than 15 process blocks,
we should check if we are getting tangled up at the tactical level.
Tactical or process-level improvements are beyond the scope of value-stream mapping.
 
A value-stream map comprises two lanes:
1. Top lane that flows right to left (<-): Flow of customer request (e.g. initial request, quote, scheduling work)
2. Bottom lane that flows left to right (->): Flow of work to fulfil the customer request.

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
Some examples of activities that impede flow:
- Batching
- Shared resources or inaccessible staff
- Task switching and interruptions
- Defects and rework

### Summary metrics
Once the metrics of each activity are listed, they can be summarized into a table consisting of:
- Total process time (PT)
- Total lead time (LT)
- Activity ratio (PT/LT)
- Rolled %C&A (%C&A of each step multiplied together)

### Opportunities for improvement
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