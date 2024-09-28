---
layout: post
title:  "Worked example of Value-Stream Mapping"
tags: value-stream-mapping lean
---

Value-stream maps can be daunting at first glance like these maps on [Google Images](https://www.google.com/search?q=value+stream+map&udm=2). ValueTech (a made-up software company for the purpose of our example) thought so too until they created the map below. We'll walk through how they did it: starting with mapping the current state followed by mapping a future-desired state in order to plan out improvements.

We are using Miro to create the map. The notation as well as mapping process is a personal adaptation of what is usually found in value-stream mapping literature. Naturally, don't take the methods described here as prescriptive.

### Mapping the current state

Everyone who participates in software development process at ValueTech as well as everyone who can authorise improvement plans have gathered in a virtual meeting room: the CTO, the product manager, the lead developer and several representative developers. There is also a facilitator with past mapping experience.

#### 1. Create a legend

Symbols can be copied from the legend as they are needed in subsequent steps.

<center><img src="/assets/images/vsm-a-worked-example/1-legend.jpg" width="600" alt="Legend"></center>

#### 2. Map the customer

We place a symbol for the entity for whom we are creating value in the center of our map. For ValueTech, this is the "Customer".

<center><img src="/assets/images/vsm-a-worked-example/2-customer.jpg" width="600" alt="Add customer"></center>

#### 3. Map processes

We then map out each disjoint process that is carried out to fulfill the customers need. We mention the action in the upper half of our post-it and the actor in the bottom half.

<center><img src="/assets/images/vsm-a-worked-example/3-add-a-process.jpg" width="600" alt="Add a process"></center>

All the processes are listed linearly. Note that we focus on the critical sequence here (i.e. the sequence that dominates delivery time). Parallel steps can be listed if they contribute significantly to the delivery time. In case of ValueTech there aren't any.

<center><img src="/assets/images/vsm-a-worked-example/4-add-all-processes.jpg" width="600" alt="Add all processes"></center>

#### 4. Inventory

Preceding each process, we add how much work is in progress as well as how much work is waiting to be processed. We call this our [inventory](https://lamak-qaizar.github.io/2022/12/22/just-because-inventory-is-invisible.html).

For the review step, we're unsure how much inventory there usually is. So we just sample how many there are right at this very moment and use that figure.

<center><img src="/assets/images/vsm-a-worked-example/5-inventory.jpg" width="600" alt="Add inventory"></center>

#### 5. Add process metrics

- Process time is also known as "touch time". This is the time that we are actively working on something.
- Lead time is process time plus all the time that work is waiting to be worked on.
- Percentage complete and accurate (%C&A) is the percentage of times that work is reported as defective by the subsequent process step.

If there are any other metrics important to the value-stream, those can be noted down too.

Note that figures need not be very accurate but only indicative of times in the context of the rest of the stream.

<center><img src="/assets/images/vsm-a-worked-example/6-process-time.jpg" width="600" alt="Add metrics"></center>

#### 6. Add barriers to flow

Here we list down barriers to flow for each process. They indicate why inventory piles up between steps, why process time lags lead time and why defects/rework is reported by the subsequent process.

<center><img src="/assets/images/vsm-a-worked-example/7-barriers.jpg" width="600" alt="Add barriers to flow"></center>

#### 7. Add information systems

We map out the tools and systems that each process is dependent on.

<center><img src="/assets/images/vsm-a-worked-example/8-information-systems.jpg" width="600" alt="Add information systems"></center>

#### 8. Summarise metrics

We create a summary of the metrics listed against each process.

- "Rolled %C&A" is computed by multiplying all the process-level %C&As. Multiplication is indicative of the compounding effect of quality drops through the stream.
- "Activity ratio" is computed by dividing total process time by total lead time.

<center><img src="/assets/images/vsm-a-worked-example/9-summary-metrics.jpg" width="600" alt="Summary metrics"></center>

### Planning improvements

#### 9. Create a future state map

We envision a state of our value stream with improved flow which we call the future state. Books on value-stream mapping generally recommends to do this step a day after creating the current state map.

<center><img src="/assets/images/vsm-a-worked-example/10-future-state.jpg" width="600" alt="Future state map"></center>

#### 10. Break the future state into increments

Two increments are proposed:

1. Automating the deployment process
2. Consolidating the development and review processes into one step (by way of pair-programming)

<center><img src="/assets/images/vsm-a-worked-example/11-future-state-increments.jpg" width="600" alt="Future state with increments"></center>

Why did we choose to automate the deployment process before improving the review process?

Inventory that piles up at the deployment stage is larger than the review process. Lead time is also more than the lead time of review. If we were to improve the review process first, it would only cause more inventory to pile up at the deployment stage. More inventory would potentially lead to larger delays in deployment, make it harder to pinpoint which change caused a deployment to fail and so on.