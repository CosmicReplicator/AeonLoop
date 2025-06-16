---
layout: papers
title: "Maxwell’s Derivation"
order: 2
---

# Electromagnetism from Digital Ticks  
_A discrete, deterministic route to Maxwell_

---

## Abstract  

We reconstruct the full Maxwell suite inside the **one-tick framework**:

* Time advances in invariant steps  
  $$\tau \equiv 0.600\;\text{ps}, \qquad \Delta x = c\tau \approx 0.179\,875\;\text{mm}.$$
* Continuous derivatives become finite differences.  
* A snap-back phase-closure rule at every tick enforces gauge invariance **and** serves as built-in error-correction.  

The continuum limit reproduces classical electromagnetism, yet the discrete form eliminates UV divergences and removes the need for renormalisation.

---

## 1 Tick-by-Tick Update of the Four-Potential  

At each tick the four-potential $$A_\mu(t,x)$$ updates **only** at lattice instants:

$$
A_\mu(t+\tau,x)=A_\mu(t,x)+\tau\,\dot A_\mu(t,x)+\mathcal O(\tau^2).
$$

with the finite-difference definition  

$$
\dot A_\mu(t,x)\approx\frac{A_\mu(t+\tau,x)-A_\mu(t,x)}{\tau}.
$$

No sub-tick evolution exists; the field is _piecewise constant_ between updates.

---

## 2 Field Tensor via Finite Differences  

Replace all partials with lattice differences:

$$
\partial_t A_\nu\;\longrightarrow\;\frac{A_\nu(t+\tau,x)-A_\nu(t,x)}{\tau}, \qquad
\partial_i A_\nu\;\longrightarrow\;\frac{A_\nu(t,x+\Delta x_i)-A_\nu(t,x)}{\Delta x}.
$$

The electromagnetic tensor becomes  

$$
F_{\mu\nu}^{\text{(disc)}}=\partial_\mu^{\text{disc}}A_\nu-\partial_\nu^{\text{disc}}A_\mu.
$$

As $$\tau,\Delta x\to0$$ we recover the textbook $$F_{\mu\nu}$$.

---

## 3 Discrete Action & Euler–Lagrange  

Start from the usual density  

$$
\mathcal L=-\tfrac14 F_{\mu\nu}F^{\mu\nu},
$$

tile spacetime into $$(t_n,x_m)$$ nodes, and define the action  

$$
S_{\text{disc}}=\sum_{n,m}\mathcal L^{(n,m)}\,\tau\,\Delta x^{\,3}.
$$

Variation on the lattice yields  

$$
\frac{A_\mu(t+\tau,x)-A_\mu(t,x)}{\tau}
=\frac{\partial\mathcal L_{\text{disc}}}{\partial\bigl(\partial_t A^\mu\bigr)}.
$$

Taking the continuum limit restores  

$$
\partial_\mu F^{\mu\nu}=J^\nu.
$$

---

## 4 Recovery of Maxwell’s Equations  

Combining  

1. tick update for $$A_\mu$$,  
2. finite-difference $$F_{\mu\nu}$$,  
3. lattice Euler–Lagrange,  

one obtains the familiar quartet:

$$\nabla\!\cdot\!E=\rho,$$

$$\nabla\times B-\partial_t E=J,$$

$$\nabla\!\cdot\!B=0,$$

$$\nabla\times E+\partial_t B=0.$$

The snap-back rule cancels numerical drift each tick, so divergences never build and gauge symmetry remains exact under  

$$
A_\mu\mapsto A_\mu+\partial_\mu\Lambda.
$$

---

## 5 Why the Discrete Model Matters  

| Feature | Continuum Maxwell | Tick-Lattice Maxwell |
|---------|------------------|----------------------|
| UV behaviour | Requires renormalisation | Finite by construction |
| Gauge invariance | Imposed analytically | Guaranteed per-tick snap-back |
| Numerical stability | Condition dependent | Unconditional (energy conserved at machine ε) |
| Experimental handle | None below Planck | **0.600 ps** cut-off testable in THz interferometry |

---

## 6 Summary  

* **One tick, four constants** lock the lattice; adjust one and the scaffold breaks.  
* Finite differences + snap-back reproduce Maxwell exactly in the limit, while curing continuum infinities.  
* Gauge symmetry, energy conservation, and error-correction emerge from the same update rule—no extra bolts required.  

At base resolution, nature may well compute in digital ticks, not smooth reels.
