---
layout: default
title: "README"
mathjax: true
permalink: /papers/readme/
---


# **AeonLoop**

*A digital playground where a single tick ($$\tau = 0.600\;\text{ps}$$) reinvents the saga of cosmology and quantum theory—tick by tick, revealing truth deeper.*

> **Working Motto**  
> “The GR metric is nothing but a field of tick counters; curvature is a map of missing ticks.”

---

## Why Bother With Another Framework?

1. **Discrete First, Continuous Second**  
   We lock in a fixed tick, $$\tau = 0.600\;\text{ps}$$, and *derive* smooth spacetime as a coarse-grained average. The continuum emerges—it isn’t assumed.

2. **Two Axioms, Dozens of Payoffs**  
   With only $$\tau$$ and an effective dimension $$D_{\mathrm{eff}} = \tfrac83$$, we naturally reproduce:  
   - The strong/weak ladder: $$195\;\text{MeV} \to 80\;\text{GeV}$$  
   - Newton’s constant $$G$$ and the minuscule cosmic $$\Lambda$$  
   - The solar-wind turbulence slope of $$-1.667$$  
   - Several Standard Model anomalies—all without extra parameters.

3. **Ad-Hoc Free and Engineered for Depth**  
   Every number is either a lattice consequence or taken straight from experiment. No hand-tuned knobs. Activate the “thin deeper” mode—here simplicity exposes the hidden structure.

---

## Core Modules (Under Active Development)

| Module                        | One-liner Description                                                               |
|-------------------------------|-------------------------------------------------------------------------------------|
| **CosmicReplicator**          | Deterministic Friedmann solver—one tick per update                                  |
| **FracCalc**                  | Recasts integrals: every computation adopts the $$D_{\mathrm{eff}}=\tfrac83$$ exponent |
| **Emergent $$h, G, \alpha$$** | Fundamental constants extracted directly from the tick lattice                      |
| **Planck-Scale Discreteness** | Automatic UV cutoff; renormalization simply drops out                              |
| **Rotational Combinatorics**  | Seven-tick closure yields the lepton mass ladder                                    |
| **Hidden Physics**            | Muon $$g\!-\!2$$ and B-anomalies emerge via a natural chirality imbalance           |

---

## Cheat-Sheet Keywords

`Digital Tick` • `2.667D Geometry` • `1.667 THz Clock`  
`Discrete Spacetime` • `Quantum Geometry` • `Ad-hoc Free` • *Think Deeper*

---

## Repo Tour

```text
papers/             polished write-ups (PDF + MD)
ladder/             energy-ladder derivations
calculator/         CLI: query any derived constant
scripts/            one-off data pulls (Swift, Fermi, DESI…)
tests/              CI sanity (MathJax, links, CSS size)
yaml/constants.yaml  ← 🔒 v2025-06-14 — the single source of numbers
