---
layout: post
title:  "Automobile assembly line kata"
tags: lean kata
---
This is the blueprint for practical workshop to learn about lean principles.
We run a simulation of an automobile assembly line using LEGO blocks.
If LEGO blocks are not available, the ideas of the workshop
can be adapted to another form of assembly using other material.
If you do an adaptation I am curious to know how you did it, so please do leave a comment.

For my workshop, I used [Bricks and Wheels 11014](https://www.google.com/search?q=lego+classic+bricks+and+wheels+1104), a LEGO Classic set.

### Workshop
- The assembly line consists of three stations: wheels, body and embellishments.
- One participant is positioned at each station.
- The assembly line is run for three iterations, known as "shifts".
- Each shift has a set of constraints (e.g. cannot talk to each other). In the third shift, the participants come up with their own constraints by doing a _Gemba_ (a discussion on the factory floor).
- Personnel change after each iteration.
- In each iteration, specs are released to the assembly line, and the line has 7 minutes to construct as many automobiles as possible.
- At the end of the line, a QA checks that the vehicles are according to spec. If there is a defect, the automobile is sent back to the line. The QA returns the automobile to the station they believe produced the defect. The automobile then passes through the line as per normal operation before returning again to the QA.
- The QA tracks time of completion and # of defects for each automobile and writes them on a whiteboard.

#### Shift 1
Constraints:
- Stations cannot talk to each other.
- Each station must build on top of what they receive. They cannot deconstruct. 
- Specs are released as a big batch (4 specs) at the start of the shift.

Possible discussion points after shift 1:
- What wastes did you identify?
- Will it help if we increase batch size?
- What will be the impact of 1 WIP on quality and throughput?

#### Shift 2
Constraints:
- Same rules as Shift 1 except specs are released one at a time (WIP of 1). The next spec is released when QA gives "OK" to the last automobile.

At the end of the shift, participants perform a Gemba to come up with constraints for shift 3. WIP of 1 is carried through because in shift 2 it is likely to have improved quality and throughput.

#### Shift 3
Constraints:
- Participants discuss and come up with their own constraints.

Possible discussion points after shift 3:
- What did we do and what would a conventional manager have done? Why?
- Mapping the 7 wastes of manufacturing to software engineering

### Facilitation
Guidance for the discussion points listed above. Suggestions are provided based on my experiences conducting the workshop.

#### What wastes did you identify?
Some wastes the participants may be able to identify one their own e.g. waiting and defects, whereas others such as inventory may require some guidance from the facilitator to spot.

#### Will it help if we increase batch size?
Usually participants will say 'no' because 4 automobiles were not completed in shift 1. A bigger batch will just result in more defects, more inventory, more waiting etc.

#### What will be the impact of 1 WIP on quality and throughput?
Most participants will agree that quality will improve and throughput will decrease. To make the other case for throughput, we can present the lean way of thinking. Lean says to increase throughput, we have to reduce wastes, one of which is defects. If we reduce defects, we are improving quality, therefore throughput should increase.

#### What did we do and what would a conventional manager have done? Why?
We can do this activity on a whiteboard by drawing two columns, one for each side.
Things that we did:
- Reduced batch size
- Set up WIP limits
- Improved quality
- Broke down silos
- Cross trained people
- Increased collaboration

Things that a conventional manager might have done:
- Released more work to the line (increase batch size)
- Punished or fired someone
- Tried to motivate them
- Set hard objectives (MBO)
- Create incentive systems
- Hired more people

We can then ask the participants "why" a conventional manager may have acted in such a way.

#### Mapping the 7 wastes of manufacturing to software engineering
This mapping exists in [Lean Software Development: An Agile Toolkit](https://www.google.com/search?q=Lean+Software+Development%3A+An+Agile+Toolkit) by Mary and Tom Poppendieck and can be presented from there.

<center><img src="/assets/images/seven-wastes-of-manufacturing-mapping.png" width="500" alt="Start refactoring from the deepest branch"></center>

### Specifications

Where color is not specified, any color can be used. Specs 1 - 4 are released as a big batch in shift 1. Shift 2 continues on from spec #5, and shift 3 continues from where shift lets off.

#1 Police car
- Red wheels
- Base
- Black body and bonnet
- Blue tinted windshield (front and rear)
- Red & blue police lights on top

#2 School bus
- Small wheels
- Base
- Yellow body
- Big windshield
- 4 black side windows
- Front red lights

#3 Tractor
- Small front wheels
- Big back wheels
- Base
- Red body
- Red front fender
- Big windshield

#4 Sedan
- Small wheels
- Base
- Blue body
- Front and back fender
- Front windshield
- Front lights

#5 Monster truck
- Big wheels
- Base
- White & blue body
- Steering wheel
- Small windshield
- Eyes up front

#6 Hearts car
- Small wheels
- Base
- White & pink body and bonnet
- Windshield
- Embellished with hearts
- Purple back spoiler

#7 Yellow sports car
- Small wheels
- Base
- Yellow body and bonnet
- Yellow fenders (front and back)
- Small windshield
- Yellow back spoiler

#8 Black cab
- Small wheels
- Base
- Black body and bonnet
- Front windshield
- Single red light on top

#9 Earth car
- Small wheels without rubber
- Base
- Green and blue body
- Green bonnet
- Windshield
- Eyes up front

#10 Pickup truck
- Wheels
- Base
- Red body
- Windshield
- Steering wheel
- 2 x gears