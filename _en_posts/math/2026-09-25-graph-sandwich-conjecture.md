---
title: "The Graph Sandwich Conjecture Is Finally Proved, 22 Years On"
description: "What the Kim–Vu conjecture — that a regular graph can be sandwiched between two binomial random graphs — says, and what its proof means"
date: 2026-09-25
category: Math
subcategory: Explainer
tags: [graph-theory, random-graph, sandwich-conjecture, probability, combinatorics]
image: /assets/og/en-2026-09-25-graph-sandwich-conjecture.png
---

A graph theory conjecture from 2004 has been fully proved 22 years later. It claims that a regular graph can be wedged between two graphs that are easier to work with — hence its name, the **sandwich conjecture**.

The proof was posted to arXiv on October 23, 2025, and became known outside mathematics when Quanta Magazine revisited the result's significance on September 18, 2026.

![Title and abstract of the proof paper](/assets/images/math/graph-sandwich-conjecture/01-paper.webp)
*Title and abstract of the proof paper — Source: arXiv:2510.20765 / Behague, Il'kovič, Montgomery*

## Two kinds of random graph

![Comparison of the two random graph models](/assets/images/math/graph-sandwich-conjecture/en/02-chart.webp)
*Comparison of the two random graph models — Source: illustrative example · self-rendered*

A graph is a structure of points (vertices) and the lines joining them (edges). Treat people as points and friendships as lines, and a social network becomes a graph.

[Binomial random graph G(n, p)]
Take n points and, for every possible pair, flip a separate coin with probability p to decide whether to add an edge

[Random d-regular graph]
Pick one uniformly at random from all graphs in which every point has exactly d edges

The difference is **independence**. In a binomial graph each edge is decided without regard to the others, which makes calculation easy. The standard tools of probability theory apply directly.

A regular graph, by contrast, does not choose its edges independently. Placing one edge at a point reduces how many more edges that point can take, which changes the next choice. That makes it far harder to handle. The trouble is that many real structures are closer to the regular side — computer networks and telecom networks, say, where each node's number of connections is fixed by specification.

## What the sandwich means

![The sandwich structure](/assets/images/math/graph-sandwich-conjecture/en/03-chart.webp)
*The sandwich structure — Source: illustrative example · self-rendered*

The conjecture Kim and Vu put forward in 2004 goes like this. Choose one binomial graph with slightly fewer edges and one with slightly more, and a random d-regular graph satisfies the containment relation between them.

| Layer | Graph | Edge probability |
| :--- | :--- | :--- |
| Bottom | Binomial random | (1-o(1)) × d/n |
| Middle | **Random d-regular** | <mark>corresponding to d/n</mark> |
| Top | Binomial random | (1+o(1)) × d/n |

Sandwiched here means contained as a subgraph: the bottom graph is a subgraph of the middle one, and the middle one is a subgraph of the top one. The conjecture says all three graphs can be constructed together so that this happens **with high probability**.

This is useful because it lets properties be carried across. A property preserved when edges are added can be carried from the bottom graph to the middle one, and a property preserved when edges are removed can be carried from the top graph to the middle one. In other words, results proved for binomial graphs don't have to be proved again for regular graphs.

Michael Krivelevich of Tel Aviv University said of the conjecture that it was in some ways a very natural claim, and that its remaining unproved had been a persistent irritation.

## The logarithmic condition

With n points and d edges at each point, **d has to grow faster than log n**. In notation, d = ω(log n).

Why such a threshold is needed becomes visible if you think about degrees being too small. Because a binomial graph draws edges independently, the number of edges varies a lot from point to point. Even with an average of 3, one point may have 0 and another 8.

In a regular graph every point has exactly d. Even with the same average, the distribution is entirely different. When d is small this difference stands out, and no binomial graph can produce the required containment relation with a regular graph. As d grows, a binomial graph's degree distribution concentrates around the average and comes to resemble a regular graph. That threshold is log n.

## 22 years of progress

![22 years of the sandwich conjecture](/assets/images/math/graph-sandwich-conjecture/en/04-chart.webp)
*22 years of the sandwich conjecture — Source: self-rendered from arXiv and Quanta materials*

After the conjecture appeared, a line of work gradually relaxed its conditions. Gao, Isaev, and McKay showed it holds when d is much larger than the fourth power of log n, and the coupling procedure they introduced had been analyzed only up to d larger than n divided by √(log n).

The 2025 paper analyzed that very procedure to the end and proved the remaining range. The authors are Richard Montgomery of the University of Warwick, along with Natalie Behague, then his postdoctoral researcher, and Daniel Il'kovič, a doctoral student. The paper states that they have fully proved the sandwich conjecture.

The proof does not build the three graphs separately and compare them. It adds edges one at a time, adjusting the probabilities so that the containment relation holds at every moment. At each step, conditional probabilities are tuned to respect the regular graph's degree condition while still containing the bottom binomial graph.

## Where the result applies

The sandwich conjecture serves less as a result in itself than as a tool used in other proofs. When you want to show some property of random regular graphs, you can find the corresponding binomial graph result and apply it.

- Properties preserved when edges are added, such as Hamiltonian paths, take the bottom graph's results
- Properties preserved when edges are removed, such as upper bounds on chromatic number, take the top graph's results
- Combining both directions can confine a regular graph's properties to a narrow range

Only properties with a fixed direction under adding or removing edges can be carried across; problems that count exact numbers aren't solved directly this way. What holds below the condition d = ω(log n) is also outside what this paper covers.

![Sandwich conjecture summary](/assets/images/math/graph-sandwich-conjecture/en/05-items.webp)
*Sandwich conjecture summary — Source: summary of this post · self-rendered*

## Sources

- [[arXiv] A proof of the Kim-Vu sandwich conjecture, Behague·Il'kovič·Montgomery (submitted 2025-10-23, revised 2025-12, source of one image in this post)](https://arxiv.org/abs/2510.20765)
- [[Quanta Magazine] Explainer on the sandwich conjecture proof (2026-09-18)](https://www.quantamagazine.org/mathematicians-build-long-awaited-graph-sandwich-20260918/)
- [[arXiv] Kim-Vu's sandwich conjecture is true for d ≫ log⁴ n, Gao·Isaev·McKay (earlier partial result)](https://arxiv.org/pdf/2011.09449)
