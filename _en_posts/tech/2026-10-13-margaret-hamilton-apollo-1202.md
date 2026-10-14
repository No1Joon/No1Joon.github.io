---
title: "Margaret Hamilton Dies — Apollo 11's 1202 Alarm and Software Engineering"
description: "The design that kept essential calculations running despite overload alarms just before landing, and how Hamilton established software engineering as a field"
date: 2026-10-13
category: Tech
subcategory: Explainer
tags: [margaret-hamilton, apollo, software-engineering, nasa, history]
image: /assets/og/en-2026-10-13-margaret-hamilton-apollo-1202.png
---

Margaret Hamilton, who led the Apollo flight software, died on September 30, 2026, in Cambridge, Massachusetts, at 90. MIT published an obituary on October 7 and introduced her as the person who established software engineering as a field.

The moment Hamilton's name comes up most often is just before Apollo 11's landing on July 20, 1969. The lander's computer showed overload alarms five times yet never stopped the calculations needed for landing, and that design reflected the design principles of Hamilton's team.

![Margaret Hamilton in 1969 with printouts of the Apollo flight software](/assets/images/tech/margaret-hamilton-apollo-1202/01-photo.webp)
*Margaret Hamilton in 1969 with printouts of the Apollo flight software — Source: Draper Laboratory*

## Margaret Hamilton's career

Born in Indiana in 1936, she majored in mathematics at Earlham College in 1958, then began programming at MIT in 1959 by writing weather prediction programs for meteorologist Edward Lorenz. After working on the US Air Force's SAGE air defense system in 1961, she joined the MIT Instrumentation Laboratory (now Draper) in 1965 as the first female programmer on the Apollo project.

She went on to lead the Command Module software team and then took responsibility for all of the flight software. She founded Higher Order Software in 1976 and Hamilton Technologies about 10 years later, and in 2016 received the Presidential Medal of Freedom from then-President Barack Obama. The citation said her work laid the foundation for modern high-reliability software design and engineering.

She's also credited with helping spread the term software engineering. In a 2018 interview, Hamilton recalled that she started using the phrase so software would be treated as engineering, like hardware, and that for a while it was taken as a joke.

## The constraints of the Apollo Guidance Computer

![An actual Apollo Guidance Computer (AGC)](/assets/images/tech/margaret-hamilton-apollo-1202/02-photo-agc.webp)
*An actual Apollo Guidance Computer (AGC) — Source: Wikimedia Commons*

The Apollo Guidance Computer (AGC) aboard the lander was a very small machine by today's standards. According to Don Eyles, who worked on the lander software, its specs were as follows.

| Item | Value |
| :--- | :--- |
| Fixed memory (ROM) | 36K words |
| Writable memory (RAM) | <mark>2K words</mark> |
| Memory cycle | 11.7µs |
| Logic elements | About 5,600 three-input NOR gates |
| Weight / power | About 32kg / about 55W |

Programs were stored in rope memory, which recorded 0s and 1s by threading copper wire through or around magnetic cores, so they couldn't be changed after launch. Hamilton was called the "rope mother" because she was responsible for this memory.

![Diagram of the DSKY interface astronauts used to talk to the computer](/assets/images/tech/margaret-hamilton-apollo-1202/03-photo-dsky.webp)
*Diagram of the DSKY interface astronauts used to talk to the computer — Source: NASA · Wikimedia Commons*

Astronauts commanded the computer by entering Verb and Noun numbers on the calculator-like DSKY. When an alarm occurred, indicators such as PROG lit up on this display and numeric codes like 1202 appeared.

## The 1202 alarm and priority scheduling

![Timeline of program alarms during Apollo 11's powered descent](/assets/images/tech/margaret-hamilton-apollo-1202/en/04-chart.webp)
*Timeline of program alarms during Apollo 11's powered descent — Source: self-rendered from Don Eyles' account*

About 5 minutes after powered descent began, right after Buzz Aldrin called up the altitude and velocity display, the first 1202 alarm appeared. There were five alarms in all before landing (four 1202s and one 1201).

The AGC's Executive assigned each job a priority and allocated 8 job slots (core sets) and 5 vector computation areas (VACs) for jobs to use. 1202 meant no core sets were left, and 1201 meant no VACs were left. The MIT obituary presents this design — keeping essential jobs running according to priority — as an achievement of Hamilton's team.

With the rendezvous radar switch in the position the procedure called for, the power phase of the radar-side equipment didn't match the computer's, and unnecessary signals came in at up to 6,400 per second. Counting these signals consumed about 13% of the computer's processing time, and the longest navigation calculation (SERVICER), lowest in priority, couldn't finish on time and piled up, running out the job space.

What kicked in was restart protection. When there was no room, the computer restarted itself, restored only the latest navigation calculation from pre-marked points, and discarded pending jobs and less important jobs not marked for protection. That's also why the display Aldrin called up disappeared after the restart. Guidance and control calculations never stopped, and Houston mission control judged that it was fine to proceed as long as the alarms didn't keep repeating.

In the final phase before landing, essential jobs alone cut the margin below 10%, so restarts couldn't fully relieve the load. When Neil Armstrong switched to attitude hold at 102:43:08 and then to P66, close to manual control, the computing load fell, and the lander touched down at 102:45:40.

## Design principles applied in today's software

![Apollo 1202 alarm summary card](/assets/images/tech/margaret-hamilton-apollo-1202/en/05-items.webp)
*Apollo 1202 alarm summary card — Source: self-rendered from Don Eyles' account and the MIT obituary*

The design of Hamilton's team assumed that hardware faults or human actions could affect the system at any time, and specified in software which jobs to keep running when that happens. In a 1971 letter to Datamation, Hamilton wrote that without this recovery behavior, Apollo 11 might not have succeeded.

Job priorities, restarts by watchdog timers, and checkpoints that save state so calculation can resume after a restart are now common techniques in car controllers, medical devices, and server operating systems. Hamilton later continued research on preventing errors at the design stage with a design language called Universal Systems Language, and published more than 130 papers.

## Sources

- [[MIT News] Margaret Hamilton, computing pioneer who led software development for the Apollo program, dies at 90 (2026-10-07)](https://news.mit.edu/2026/margaret-hamilton-computing-pioneer-dies-1007)
- [[The Boston Globe] Margaret Hamilton obituary (2026-10-07, date of death, career)](https://www.bostonglobe.com/2026/10/07/nation/margaret-hamilton-apollo-software-mit/)
- [[NPR] Apollo software pioneer Margaret Hamilton dies at 90 (2026-10-08)](https://www.npr.org/2026/10/08/nx-s1-5994972/margaret-hamilton-obituary-software-engineer-apollo)
- [[Don Eyles] Tales from the Lunar Module Guidance Computer (causes and handling of the 1202 and 1201 alarms, AGC specs)](https://www.doneyles.com/LM/Tales.html)
