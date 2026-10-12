---
title: "A Battery You Swallow — MIT's 1.84V Paper Battery Breaks Down Inside the Body"
description: "The design, performance, and limits of research tackling the power problem in swallowable capsule devices with a dissolving magnesium paper battery"
date: 2026-09-23
category: Science
subcategory: Explainer
tags: [ingestible-electronics, biodegradable-battery, mit, medical-device, bioelectronics]
image: /assets/og/en-2026-09-23-ingestible-dissolvable-battery.png
---

MIT researchers have built a paper battery that dissolves inside the body after being swallowed, publishing the work in Nature Chemical Engineering on September 21, 2026. It puts out up to 1.84V and ran a capsule device for three days inside a pig's stomach before breaking into pieces and degrading over several weeks.

Swallowable capsule devices today mostly run on silver oxide coin cells. The researchers said they aimed to reduce both the risk of the cell injuring the digestive tract if the capsule's shell is damaged and the problem of excreted cells persisting in the environment.

![Paper title and abstract, with highlights on 1.84V, the Mg–MoO3 paper battery, and the pig experiment](/assets/images/science/ingestible-dissolvable-battery/01-paper.webp)
*Paper title and abstract, with highlights on 1.84V, the Mg–MoO3 paper battery, and the pig experiment — Source: Say et al., Nature Chemical Engineering (2026) (CC BY 4.0, highlights added)*

## Study overview

The paper is titled *Bioresorbable batteries for transient ingestible bioelectronics* and was led by Professor Giovanni Traverso's lab in MIT's Department of Mechanical Engineering. The first author is Mehmet Girayhan Say, a former MIT postdoctoral researcher; it was submitted in November 2025 and accepted for publication in August 2026.

- Anode: magnesium alloy (AZ31)
- Cathode: a paper composite of molybdenum trioxide (MoO3) mixed with cellulose nanofibers
- Electrolyte: a biodegradable ionic liquid gel made from choline chloride and lactic acid
- Packaging: beeswax and candelilla wax

The researchers said they designed the battery so that the amounts of all its components fall within recommended daily intake limits. It comes in two shapes — a 7.5mm-diameter disc and a 24mm-long rod — and the disc fits inside a pharmaceutical 000 capsule (26mm long, 9.5mm in diameter).

## Battery design and applications

![The dissolving battery's structure, the medication-tracking RFID and gastric stimulation capsules, and a schematic of degradation](/assets/images/science/ingestible-dissolvable-battery/02-paper-fig1.webp)
*The dissolving battery's structure, the medication-tracking RFID and gastric stimulation capsules, and a schematic of degradation — Source: Say et al., Nature Chemical Engineering (2026) Fig. 1 (CC BY 4.0)*

### RFID for confirming medication

RFID (radio frequency identification) tags are used to confirm from outside whether a pill has been swallowed. Existing passive tags have no battery, so the reader had to be held close to the neck or waist; a tag with this battery kept communicating with a reader 1.5m away. When the capsule enters the esophagus, signal strength drops by about 10dB, and that change marks the moment it was swallowed.

### Gastric electrical stimulation capsule

This capsule passes a weak current through the stomach wall to increase secretion of the appetite hormone ghrelin. One battery sustained stimulation for 3 days, and two connected in parallel for up to 7. In three pigs, blood ghrelin rose by an average of 36.3% after 20 minutes of stimulation, with a maximum of about 50%.

MIT explained that stimulating ghrelin secretion could be used to treat cachexia, the weight loss seen in cancer patients and others. An earlier version of this capsule ran on two silver oxide coin cells.

## Voltage and run time

![Open-circuit voltage by cathode material for magnesium-anode batteries](/assets/images/science/ingestible-dissolvable-battery/03-chart.webp)
*Open-circuit voltage by cathode material for magnesium-anode batteries — Source: self-rendered from figures in the Nature Chemical Engineering paper*

Magnesium dissolves in the body at 1.2–12㎛ (micrometers) a day, which is why it has been studied as an anode for biodegradable batteries. In prior work cited by the paper, pairing magnesium with molybdenum, iron, or tungsten gave 0.15–0.75V, while the molybdenum trioxide cathode combination raised it to **1.84V**.

At an operating voltage of 1.84V, areal capacity was 2.43mAh/㎠, and the researchers wrote that including energy and power density, it is comparable to other biodegradable batteries. Connected in series, it supplied more than 3V for over 24 hours, which they judged usable even for capsules carrying a microcontroller or a wireless communication module.

![Change in open-circuit voltage for batteries placed in a pig's stomach](/assets/images/science/ingestible-dissolvable-battery/04-chart.webp)
*Change in open-circuit voltage for batteries placed in a pig's stomach — Source: self-rendered from Fig. 2 of the Nature Chemical Engineering paper*

The researchers put the batteries in capsules, fixed them in pigs' stomachs endoscopically, then retrieved and measured them on days 1 and 3. Voltage declined gradually over three days in both shapes, and the larger battery's energy density fell from 1.32mWh/㎠ to 0.22mWh/㎠.

## How it breaks down in the body

![The gastric stimulation capsule degrading in simulated gastric fluid at 0, 14, 40, and 90 days](/assets/images/science/ingestible-dissolvable-battery/05-paper-fig4.webp)
*The gastric stimulation capsule degrading in simulated gastric fluid at 0, 14, 40, and 90 days — Source: Say et al., Nature Chemical Engineering (2026) Fig. 4k (CC BY 4.0)*

Capsules immersed in simulated gastric fluid (pH 1.2, 37℃) began dissolving from day 14, and when moved to 75℃ to accelerate degradation, most dissolved within 40 days. By day 90, only small particles remained.

In the pig experiments, capsules softened and broke apart over one to two weeks and passed through the digestive tract, with only occasional metal residue from the battery found. The non-dissolving part of the RFID tag is a single RFID chip about 18㎟ in size, which the researchers expect to be excreted naturally.

## Where this touches Korea

By the Korea Consumer Agency's count, there were 268 button cell ingestion incidents among children under 10 over the past five years. A swallowed cell can trigger electrochemical reactions in the body, causing burns and perforation of the esophagus and stomach, and in July 2025 the Korean Agency for Technology and Standards said it would establish standards requiring child-resistant packaging for button cells.

This paper's introduction also cites cases of esophageal perforation and death from accidentally swallowed button cells, explaining that a dissolving battery could improve safety when a capsule breaks or stays in the body a long time. This battery is designed as a power source for medical capsules, though, so it is far from a product that would replace household button cells.

No Korean company or institution has been confirmed to have participated in this research or announced plans to adopt it.

## Limits and remaining work

![Concept image of a capsule dissolving inside the body](/assets/images/science/ingestible-dissolvable-battery/06-agy.webp)
*Concept image of a capsule dissolving inside the body — Source: concept image · self-generated with agy*

[Circuit board]
The stimulation capsule's printed circuit board (PCB) does not yet dissolve, and the researchers named a fully dissolving circuit as the next task.

[Experimental conditions]
The animal experiments used a small number of fasted pigs, and conditions with food present, varying acidity, and differences in intestinal motility have not been tested.

[Operating life]
With the current packaging, performance degrades substantially past one week. They attributed this to the electrolyte gel drying out and the packaging partly dissolving.

[Variation between units]
Performance differed from battery to battery, which the researchers attributed to manufacturing tolerances and differences in wax thickness. They wrote that shelf life also needs further validation.

[Use in humans]
There have been no human trials yet. MIT said it plans to begin clinical trials of SAFARI, an RFID medication-confirmation system using this battery, in about two years.

Funding came from Novo Nordisk and others.

## Summary

![Summary card for the dissolving paper battery](/assets/images/science/ingestible-dissolvable-battery/07-items.webp)
*Summary card for the dissolving paper battery — Source: self-rendered from the Nature Chemical Engineering paper*

## What to watch next

- Entering the clinic: human trials of the SAFARI medication-confirmation system, which MIT put about two years out
- Extension to implants: application to short-term implantable devices lasting hours to days, which the researchers mentioned

## Sources

- [[Nature Chemical Engineering] Say et al., Bioresorbable batteries for transient ingestible bioelectronics (2026-09-21, source of three images in this post)](https://www.nature.com/articles/s44286-026-00443-7)
- [[MIT News] Research on batteries that break down in the GI tract (2026-09-21)](https://news.mit.edu/2026/batteries-safely-break-down-in-gi-tract-could-improve-ingestible-devices-0921)
- [[Aju Business Daily] Child-resistant packaging for button cells and 268 ingestion incidents (2025-07-15)](https://www.ajunews.com/view/20250715082228941)
