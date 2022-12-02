---
layout: post
title:  "What we can learn from airplane crashes"
---
From 1978 to 1988, Korean Air had a “loss” rate of 4.79 planes per million departures.
In contrast, United Airlines had a loss rate of 0.27 per million -- 94% less than Korean Air. 
Pilots in both airlines were as skilled as each other, 
had as many flying hours under their belts, and were flying equally good planes. 
Why did Korean Air then have so many more crashes?

Malcom Gladwell studies the disasters of Korean Air 
and other airlines in a chapter of his book “Outliers”. 
What he finds common is that the causes are overbearingly due to errors in teamwork and communication.

> The kinds of errors that cause plane crashes are invariably errors of teamwork and communication. -- Outliers

That’s right, planes crash more for social reasons than technical reasons. 
Does any part of this statement sound familiar?

We’ll get back to the question. 
First, let’s explore some findings from “Outliers”.

### Planes crash when the pilots don’t communicate effectively

The airline industry realised long ago that having _pilots_
onboard significantly reduces the risk of disaster. 
Commercial airlines require at least two pilots. 
Longer flights may require as many as three or four.

They also realised that having two pilots in a cockpit is not enough. 
The pilots must work together. 
Earl Weener, once the chief engineer for safety at Boeing, said:

> For a long time it’s been clear that if you have two people operating the airplane cooperatively, 
> you will have a safer operation than if you have a single pilot flying the plane 
> and another person who is simply there to take over if the pilot is incapacitated.

In case of Korean Air, the first officers
were subservient -- happy to follow orders but unwilling to challenge the captain. 
Sometimes they would make an important observation
and yet be hesitant to tell the captain. 
This lack of collaboration led to seemingly trivial errors.

These errors however added up. 
Malcom Gladwell points out that industrial accidents are, 
on average, the result of a sequence of seven human errors. 
Each error if analysed in isolation might be considered harmless,
but in sequence they can lead to nuclear meltdowns and plane crashes.

> The typical accident involves seven consecutive human errors.
> 
> One of the pilots does something wrong that by itself is not a problem.
> Then one of them makes another error on top of that,
> which combined with the first error still does not amount to a catastrophe.
> But then they make a third error on top of that, and then another
> and another and another _and another_, and it is a combination of all those errors
> that lead to disaster. -- Outliers

Why did the first officers of Korean Air 
not challenge nor share observations with their captain? 
The captain was a superior. 
Korean customs and power dynamics inhibit 
the effectiveness of communication between people of differing ranks. 
Pilots on airlines such as United Air, an American airliner, 
could share feedback with and challenge each other much more freely.

It is worth asking if the power dynamics in our organisations
have similar effects. Are people in lower ranks,
who sometimes have the best view of problem,
able to challenge and share feedback with those in higher positions?

### Planes crash when the most experienced pilot is flying

> Historically, crashes have been far more likely to happen
> when the captain is in the flying seat. -- Outliers

Planes crash more often when the captain is flying 
than when the first officer is flying. That is surprising
since the captain is usually the more experienced of the two.

What's happening here? When the captain is flying, 
the first officers instinct is to assume that the captain is always “right”.
The captain is more experienced after all.
Hesitation like this could lead to delay in sharing critical information --
or worse, critical information that is not shared at all.
In a cockpit, hesitation like this could prove to be fatal for everyone.

When the first officer is in the flying seat and the captain spots an error,
they are much less likely to hesitate in calling it out.

### Planes crash when the pilots are working under duress

An overwhelming number of crashes occur when flights 
are delayed and the pilots are stretching to meet schedule. 
Even more accidents occur when the pilots are overworked -- 
in 52 percent of airplane crashes, 
pilots have been awake for 12 hours or more.

Airlines skimp on hotel costs by minimising layovers 
and getting pilots to fly back-to-back flights. 
When pilots are tired, they’re not as sharp.
This leads to errors in judgement, and like we saw previously, 
these errors add up. 

E.g. the pilots are tired and the weather isn’t great. 
The glide scope, a beam of light to guide the pilot to the runway, 
is out of service. There’s a backup radar, 
but the captain decides to take a visual approach to landing. 
An error in judgement when the weather isn’t great. 
The first office points out the error. Thrice. 
But the message is so subtle, the captain misses it. 
That’s how KAL 801, a Korean Air flight, crashes into the hills, 
killing 228 of the 258 people on board.

When airlines skimp on hotel costs
they inadvertently end up losing millions of dollars in lost aircraft, 
tainted reputation, legal costs and more. 
Not to mention the pilots, crew and passengers who never get home.

---

Back to _that_ question, 
does any part of the following statement sound familiar?

> "Planes crash more for social reasons than technical reasons."

If we replace ‘_plane crashes_’ with ‘_problems in software development_’, 
we get the premise of “Peopleware” -- a book on managing software projects.

> The major problems of our work are not so much 
> technological as sociological in nature. -- Peopleware

A cursory glance at an airplane crash may indicate a technical malfunction. 
But investigators don’t settle there -- they dig deeper. 
They question what led to the malfunction 
and in the process often reveal faults elsewhere,
e.g. in social constructs such as how the pilots communicate or collaborate.

In software projects, we frequently attribute failures 
to technical errors such as missing tests or alerts. 
Seldom do we question the social constructs that lead to those technical faults.

What are the social constructs that could lead to failures in software projects? 
Here are a few examples:

- Are we overworking developers like pilots on back-to-back flights 
so that they are writing code and solving problems while they are not at their sharpest? 
- Are we assigning projects and tasks to individuals 
because pair programming (or a co-pilot) would cost us more? 
- Are we shielding our most experienced developers from 
those less experienced so that they can go faster, 
much like the captains in the flying seat?

After Korean Air discovered the problems that were plaguing the airline, 
it did turn itself around. Since 1999, the airline has a spotless record 
and is as safe to fly as any other airline in the world.

Is the software industry in need of a turn around?
I don't know, and I don't want to wait to find out either.
What we can do now is take caution from these tales
and try not to repeat the same mistakes again.