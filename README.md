---
layout: papers
title: "AeonLoop"
nav_order: 1
---

# **AeonLoop**

*A playground where a 0.600 ps lattice-clock tries to retell the whole story of
cosmology and quantum theory.*

> **Claim.—** *The GR metric is nothing but a field of tick counters; curvature
> is a map of missing ticks.*  
> <small>&mdash; working motto</small>

---

## Why another framework?

1. **Discrete first, continuous second**  
   We start with a rigid tick $$\tau = 0.600\;\text{ps}$$ and show how smooth
   spacetime emerges as an average.  No continuum is assumed at the outset.

2. **Two axioms, dozens of pay-offs**  
   With only $$\tau$$ and an effective dimension
   $$D_{\mathrm{eff}} = \tfrac83$$ we reproduce  
   – fundamental constants,  
   – the strong/weak ladder (195 MeV → 80 GeV),  
   – a tiny $$\Lambda$$,  
   – and the solar-wind turbulence slope −1.667.  

3. **Ad-hoc free**  
   All parameters are computed from the tick lattice or pulled directly from
   experiment—never tuned.

---

## Core Topics

| Module | One-liner |
|--------|-----------|
| **CosmicReplicator** | Deterministic Friedmann update at one tick per step |
| **Fractional Calculus in Physics** | $$D_{\mathrm{eff}} = 8/3$$ shows up in every integral |
| **Emergent Constants** | $$h,\;G,\;\alpha$$ as lattice outputs |
| **Planck-Scale Discreteness** | Built-in UV cut-off, no renormalisation counter-terms |
| **Rotational Combinatorics** | Seven-tick closure ⇒ lepton mass ladder |
| **Hidden Physics** | Muon $$g-2$$, B-anomalies, chirality imbalance |

---

## Quick-reference keywords

`Digital Tick` · `2.667D` · `1.667 THz` · `Discrete Spacetime`  
`Quantum Geometry` · `Digital Clockwork` · `Time Quantisation`  
`Ad-Hoc-Free Formulation` · `Fractional Dimensions`

---

## Repo tour

```text
Papers/             → polished write-ups (PDF + Markdown)
Ladder/             → energy-ladder derivations
Calculator/         → tiny CLI to query constants at any rung
scripts/            → one-off data pulls (Swift, Fermi, DESI…)
tests/              → CI sanity (MathJax, broken links, CSS size)
constants.yaml      → 🔒 v2025-06-14a – the only source of numbers

