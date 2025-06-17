---
layout: default
title: "README"
nav_order: 1
mathjax: true
---

# **AeonLoop**

*A playground where a single digital tick ( $$\tau = 0.600\;\text{ps}$$ ) tries to retell the whole saga of cosmology and quantum theory.*

> **Working motto**  
> “The GR metric is nothing but a field of tick counters; curvature is a map of missing ticks.”

---

## Why bother with another framework?

1. **Discrete first, continuous second**  
   We fix one rigid tick $$\tau = 0.600\;\text{ps}$$ and *derive* smooth spacetime as a coarse-grained average. No continuum is assumed up front.

2. **Two axioms, dozens of pay-offs**  
   From just $$\tau$$ and an effective dimension  
   $$D_{\mathrm{eff}} = \tfrac83$$ we reproduce  
   * the strong/weak ladder $$195\;\text{MeV}\to80\;\text{GeV}$$,  
   * Newton’s $$G$$ and the tiny cosmic $$\Lambda$$,  
   * the solar-wind turbulence slope $$-1.667$$,  
   * and several SM anomalies—*without* new free parameters.

3. **Ad-hoc free**  
   Every number is either a lattice consequence or taken straight from experiment. No hand-tuned knobs.

---

## Core Modules (work in progress)

| Module | One-liner |
|--------|-----------|
| **CosmicReplicator** | Deterministic Friedmann update, one tick per step |
| **FracCalc** | All integrals acquire the $$D_{\mathrm{eff}}=\tfrac83$$ exponent |
| **Emergent $$h,G,\alpha$$** | Fundamental constants as lattice outputs |
| **Planck-Scale Discreteness** | Built-in UV cut-off; renormalisation disappears |
| **Rotational Combinatorics** | Seven-tick closure ⇒ lepton mass ladder |
| **Hidden Physics** | Muon $$g\!-\!2$$ & B-anomalies via chirality imbalance |

---

## Cheat-sheet keywords

`Digital Tick` • `2.667D geometry` • `1.667 THz clock`  
`Discrete Spacetime` • `Quantum Geometry` • `Ad-hoc-free`

---

## Repo tour

```text
papers/            polished write-ups  (PDF + MD)
ladder/            energy-ladder derivations
calculator/        CLI: query any derived constant
scripts/           one-off data pulls (Swift, Fermi, DESI…)
tests/             CI sanity (MathJax, links, CSS size)
yaml/constants.yaml   ← 🔒 v2025-06-14 — single source of numbers
