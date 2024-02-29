---
layout: post
title:  "Notes on Value-Stream Mapping"
tags: value-stream-mapping lean
---

> A value stream is the sequence of activities required to design, produce, and deliver a good or service to a customer. -- Value Stream Mapping by Karen Martin and Mike Osterling

John Shook and Mike Rother in _Learning to See_ state that most improvement efforts
fail because they don't see the whole. The result is that one part of the system improves only for
wastes and bottlenecks to emerge in other parts of the system.
Value-stream mapping helps us take a holistic view of the system before we jump in to make improvements.

Value-stream mapping comprises the following high-level activities.

1. Pick a value-stream
2. Map the current state
3. Map the future (desired) state
4. Set goals and execute improvements
5. Repeat steps 2 through 5

Note that a separate value stream should be drawn for each product-family
(a set of products that have a high number of common processing steps).

Below we'll focus our attention on creating the current state map.

### Creating the current state map
The sequence below is not definitive -- it is just a workflow I have in mind as I prepare to do mapping activity.
1. List out all the activities (processes) and arrange them as a timeline
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
Barriers to flow include:
- Non-value adding work
- Back-flow due to defects
- Waiting
- Creation of inventory
- Hand-offs
- Inspection
- Work that could be standardised or automated

A more detailed list by Karen Martin and Mike Osterling is shared towards the end of the article.

A handout PDF that I used for a mapping activity can be found [here](/assets/pdf/Value_Stream_Mapping_Handout.pdf).

### Summarising the metrics
Once the metrics of each activity are listed, they can be summarized into a table consisting of:
- Total process time (PT)
- Total lead time (LT)
- Activity ratio (PT/LT)
- Rolled %C&A (%C&A of each step multiplied together)

### Notation
This is an adapted notation that I used on an online white-boarding tool.

<center><img src="/assets/images/value-stream-mapping-symbols.png" width="600" alt="Value-stream mapping notation"></center>

### Sample map
A sample diagram I drew with a client with details blurred out.

<center><img src="/assets/images/value-stream-mapping-sample.png" width="600" alt="Value-stream mapping sample diagram"></center>

### Barriers to flow
Karen Martin and Mike Osterling describe a set of common problems 
that current state mapping may reveal. They are listed below for reference.

> - Loop-backs
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
