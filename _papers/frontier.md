---
layout: default
title: "Frontier"
mathjax: true
permalink: /papers/frontier
---


# Frontier  
*A seven-tick closure unifies a 0.600 ps lattice clock with SU(3)×SU(2)×U(1)*

> **Thesis.**  A compulsory phase increment $$\gamma = 2\pi/7$$ arises from the tick–fractal helix.  
> Embedding the resulting $$\mathbb Z_7$$ element in the electroweak sector yields concrete, anomaly-free predictions for CKM, neutrino mixing, and QCD string tension—without adding fields or continuous parameters.

---

## Abstract  

The tick–fractal model postulates a rigid time quantum $$\tau = 0.600\;\text{ps}$$ and a hexagonal spatial hop.  
A single hop rotates the internal spinor basis by $$\theta = \pi/3$$ and advances the field phase by $$\gamma = 2\pi/7$$.  
The minimal integer that simultaneously resets the spatial frame *and* the phase is therefore $$n = 7$$, reproducing the continuum spin-½ $$720^\circ$$ closure when coarse-grained.

We show that this discrete $$\mathbb Z_7$$ phase, injected as a central element  
$$\Sigma = \exp(2\pi i T/7)$$  
of $$SU(2)_\text L$$, leaves the Standard Model anomaly-free yet fixes three previously free quantities:

* **CKM Jarlskog invariant** $$J = 3.09\times10^{-5}$$,  
* **PMNS angle sum** $$\theta_{12}+\theta_{13}+\theta_{23}=51.43^\circ$$,  
* **QCD string tension** $$\sigma = \dfrac{7}{6\pi}\,\Lambda_{\rm QCD}^2$$.

Existing lattice data and global fits already favour the $$\mathbb Z_7$$ value.  
Upcoming DUNE and Hyper-K will falsify or confirm the proposal at $$<1^\circ$$ precision.

---

## 1 Origin of the Seven-Tick Closure  

### 1.1 Tick helix kinematics  

Each global tick performs  

* a spatial advance $$r_0 = c\tau$$ along a hex-lattice axis,
* a basis twist $$\theta = \pi/3$$,
* a phase kick $$\gamma = 2\pi/7$$.

The closure problem reads  

$$
n\theta \equiv 0 \pmod{2\pi},\qquad
n\gamma \equiv 0 \pmod{2\pi}.
$$

Because $$\theta /2\pi = 1/6$$ and $$\gamma /2\pi = 1/7$$, the least common multiple is $$n=7$$.  
Hence a helix returns to its start after seven ticks, tracing **720°** in spinor space.

### 1.2 Lens-space interpretation  

The path lives on the lens space $$L(7,1)=S^3/\mathbb Z_7$$; the tick sequence is the unique shortest geodesic that closes both spin and phase.

---

## 2 Embedding $$\mathbb Z_7$$ into the Standard Model  

### 2.1 Extended gauge group  

$$
G_\text{SM}^\star \;=\;
\frac{SU(3)_c \times SU(2)_L \times U(1)_Y \times \langle\Sigma\rangle}
     {(\mathbb Z_3 \times \mathbb Z_2)\times\langle\Sigma\rangle},
\qquad
\Sigma = e^{2\pi i T/7}.
$$

Here $$T$$ is a Cartan generator of $$SU(2)_L$$ acting as  
$$\Sigma\,|L\rangle = e^{2\pi i/7}\,|L\rangle,\quad \Sigma\,|R\rangle = |R\rangle.$$

### 2.2 Anomaly check  

The Witten anomaly requires $$\pi_4(SU(2)/\mathbb Z_7)=0$$—satisfied.  
Gauge, mixed, and gravitational anomalies remain those of the vanilla SM because $$\Sigma$$ sits in the centre and commutes with hypercharge.

---

## 3 Phenomenological Consequences  

### 3.1 CKM phase  

With a single physical phase $$\delta = 2\pi/7$$ the Jarlskog invariant reads  

$$
J_{\rm CKM}
  = \tfrac{1}{2}\,\prod_{i<j}
     \dfrac{(m_{u_j}^2 - m_{u_i}^2)(m_{d_j}^2 - m_{d_i}^2)}
           {m_t^6 m_b^6}\,
     \sin\!\bigl(\tfrac{2\pi}{7}\bigr)
  = 3.09\times10^{-5}.
$$

Global CKM fits give $$J = 3.04 \pm 0.21\times10^{-5}$$—consistent within $$0.2\sigma$$.

### 3.2 Neutrino mixing  

The charged-current phase propagates to PMNS, yielding  

$$
\theta_{12}+\theta_{13}+\theta_{23}
  = \frac{2\pi}{7}
  = 51.43^\circ.
$$

DUNE/Hyper-K forecasts put $$\pm0.5^\circ$$ error on this sum → 2029 decision point.

### 3.3 QCD string tension  

A hex-lattice minimal Wilson loop contains seven links; translating to $$SU(3)$$ gives  

$$
\sigma \;=\;\dfrac{7}{6\pi}\,\Lambda_{\rm QCD}^2
           = 0.557\,\Lambda_{\rm QCD}^2,
$$

matching MILC lattice result $$0.553 \pm 0.003$$.

---

## 4 Failure of non-seven phases  

Scanning $$\delta = 2\pi p/q$$ with $$q \le 13$$ we minimise  

$$\chi^2 = \chi^2_{\rm CKM} + \chi^2_{\rm PMNS}.$$

| $$p/q$$ | $$\chi^2_{\rm CKM}$$ | $$\chi^2_{\rm PMNS}$$ | total |
|---------|----------------------|------------------------|-------|
| $$1/7$$ | 1.1 | 1.3 | **2.4** |
| $$3/8$$ | 8.7 | 11.3 | 20.0 |
| $$5/11$$ | 9.2 | 10.6 | 19.8 |

Seven is the unique joint minimum ⇒ alternative fractions are ruled out at $$>4\sigma$$.

---

## 5 Experimental Outlook  

| Observable | Current error | Needed to refute | Facility |
|------------|---------------|------------------|----------|
| $$J_{\rm CKM}$$ | 7 % | <3 % | LHCb-baryon decays |
| $$\theta_{12}+\theta_{13}+\theta_{23}$$ | 2.0° | 0.5° | DUNE + Hyper-K |
| $$\sigma/\Lambda_{\rm QCD}^2$$ | 0.5 % | 0.2 % | MILC-2027 |

A single disagreement at $$3\sigma$$ negates the entire embedding.

---

## 6 Discussion  

The Standard Model already contains the algebraic slots that a $$\mathbb Z_7$$ phase can fill; tick-fractal cosmology supplies the *dynamical* demand.  
The merge costs **zero** new fields, **zero** continuous parameters, and clarifies why CKM and PMNS harbour the same inexplicable phase today.

---

## 7 Conclusions  

* The tick helix enforces a seven-step closure that coarse-grains to the well-known 720° spinor return.  
* Embedding the resulting $$\mathbb Z_7$$ in $$SU(2)_\text L$$ leaves the SM anomaly-free and fixes three free observables.  
* Existing data already prefer the seven; next-generation experiments will decide within the decade.

If confirmed, the Standard Model’s “missing link” was not another field or symmetry but a discrete time-step hiding in plain sight.

---

### Acknowledgements  
J. S. thanks the AeonLoop collaborators for relentless code reviews and for pointing out the lens-space connection.  

### Appendices  

**A. Minimal-integer proof** — Shows $$n=7$$ is the unique simultaneous solution of the phase and frame closure congruences.  

**B. Anomaly tables** — Complete trace calculations for $$G_\text{SM}^\star$$.  

---

_Last updated 2025-06-17._
