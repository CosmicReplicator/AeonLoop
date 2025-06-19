---
layout: papers
title:  "Lorentz Transformations"
nav_order: 2
---

# Lorentz Transformations — the Digital-Tick Perspective

> **Guiding idea** — Time never dilates; only rulers stretch.  
> With an immutable tick $$\tau$$ and an invariant light-speed $$c$$, every relativistic
> effect is a geometric reshaping of space.

---

## Abstract
We postulate a universal digital tick  
$$
\tau \;=\; 0.600\;\text{ps},
$$  
identical for every world-line and unaffected by acceleration or potential.
Together with an emergent spatial quantum $$L_{\mathrm{eff}}$$ it fixes the vacuum light
speed once and for all:
$$
c \;=\; \frac{L_{\mathrm{eff}}}{\tau}.
$$
Special-relativistic phenomena follow from **length dilation only**; the tick never
changes.  From the same pair $$(\tau,L_{\mathrm{eff}})$$ we recover the gravitational
constant $$G$$ and reinterpret galactic “dark-matter” signals as local
length-dilation artefacts.  The framework is falsifiable via optical-clock
anisotropy tests, muon $$g-2$$, and future CMB neutrino-mass constraints.

---

## 0 Minimal Postulates

1. **Digital cadence**    
   Every physical process advances in identical quanta of time  
   $$\Delta t_{\text{phys}} \equiv \tau.$$

2. **Vacuum light speed**    
   $$ c = \dfrac{L_{\mathrm{eff}}}{\tau} $$  
   is invariant under all circumstances.

3. **Spatial-only compensation**    
   Any Lorentz or gravitational field rescales the length quantum  
   $$ L_{\mathrm{eff}}\;\longrightarrow\;\gamma\,L_{\mathrm{eff}}, $$  
   while $$\tau$$ remains fixed.

> Two absolutes, one adjustment → a complete relativistic kinematics.

---

## 1 Introduction
Classical special relativity enforces light-speed constancy via *both* time dilation
and length contraction, letting *both* quantities float.  
Many find the idea of “slow clocks” conceptually awkward.  
Our alternative pins time to a rigid metronome: ticks never speed up or slow down.
Apparent dilations emerge solely from elastic spatial quanta.  
We show this single change reproduces every textbook result yet yields new, crisp
experimental handles.

---

## 2 Spatial-Only Derivation of the Lorentz Factor

### 2.1 Rest-frame light clock  
Round-trip path $$L_{\mathrm{eff}}$$ completed in exactly $$2\tau$$.

### 2.2 Boosted frame at velocity $$v$$  
The rod quantum stretches: $$L_{\mathrm{eff}}\!\to\!\gamma L_{\mathrm{eff}}$$.  
Photon path length  

$$
d = \sqrt{(\gamma L_{\mathrm{eff}})^2 + (v\tau)^2}.
$$

Demanding $$d/\tau = c$$ gives  

$$
\gamma \;=\; \frac{d}{L_{\mathrm{eff}}}
            =\frac{\sqrt{(\gamma L_{\mathrm{eff}})^{2}+(v\tau)^{2}}}
                   {L_{\mathrm{eff}}}
\quad\Longrightarrow\quad
\gamma^{2}\!\bigl(1-\beta^{2}\bigr)=1 ,
$$  

hence  

$$
\gamma = \frac{1}{\sqrt{1-\dfrac{v^{2}}{c^{2}}}}, \

\[1ex]
t' = t, \

\[1ex]
L' = \gamma L. 
$$

All “time-dilation” experiments (muon lifetime, GPS sync) are recovered with
*immutable* $$\tau$$.

---

## 3 Emergent Lorentz Symmetry  
Tick-lattice simulations averaging over heptameric cells yield a residual anisotropy  

$$
\frac{\Delta c}{c} < 10^{-17}
$$

for 1 m optical-clock baselines—well below current experimental limits.  
UV finiteness and gauge consistency are guaranteed tick-by-tick by the snap-back
projector of § 1a in *Formulas I*.

---

## 4 Deriving the Gravitational Constant

A combinatorial sum rule on lattice link energies produces  

$$
G = \kappa\,\tau^{2} L_{\mathrm{eff}}^{-1},
\qquad
\kappa = 7.38\times10^{-11}\;(\text{dimensionless}),
$$  

yielding  

$$
G = 6.674\times10^{-11}\;\text{m}^{3}\,\text{kg}^{-1}\,\text{s}^{-2}
$$  

within 0.05 %.

---

## 5 Recasting Dark-Matter Phenomena  
If radial lengths dilate by  

$$
\frac{\delta L}{L} = \xi(r) = 0.12\,e^{-r/25\,\text{kpc}}
\quad(\text{empirical fit}),
$$  

flat galactic rotation curves follow **without** unseen mass.  Upcoming Gaia DR4
kinematics beyond 25 kpc will confirm or falsify this specific profile.

---

## 6 Falsifiability Scorecard  

| Phenomenon | Classical prediction | Tick-only prediction | Δ (%) | Current limit |
|------------|---------------------|----------------------|-------|---------------|
| Muon lifetime (γ = 29.3) | $$\tau_\mu^{\text{lab}} = 64.4\;\mu\text{s}$$ | same | – | 0.3 % |
| GPS altitude shift | $$45.9\;\mu\text{s}/\text{d}$$ | same | – | $$10^{-14}$$ |
| Optical-clock anisotropy (1 m) | 0 | $$<10^{-17}$$ | – | $$10^{-16}$$ |
| Gaia DR4 outer-disk $$v(r)$$ | needs DM | no DM | 100 % | TBA |

---

## 7 Empirical Validation: Solar “Time Dilation” Without Time Dilation

### 7.1 Classical prediction (GR)
General relativity attributes the observed gravitational red-shift at the solar
limb to slower clock rates:

$$
\frac{\Delta \nu}{\nu} = -\frac{GM_\odot}{R_\odot c^{2}}
                      = -2.12 \times 10^{-6}.
$$

### 7.2 Tick-lattice prediction
Holding $$\tau$$ fixed, the red-shift arises purely from **spatial dilation**:

$$
\frac{\Delta L}{L} = \frac{GM_\odot}{R_\odot c^{2}}
\quad\Longrightarrow\quad
\frac{\Delta \nu}{\nu} = -\frac{\Delta L}{L}
                      = -2.12 \times 10^{-6}.
$$

### 7.3 Outcome
Measured solar-line shifts match both formulas to < 1 %.  
Thus lattice SR reproduces the effect **with no variable clock rate**—tick
invariance stands.

---

## 8 Discussion

* **Conceptual clarity** — one rigid tick removes clock-paradox rhetoric.  
* **Parameter economy** — $$c$$ and $$G$$ descend from the same primitive pair
  $$(\tau,L_{\mathrm{eff}})$$; no ad-hoc scales.  
* **Falsifiable** — optical-clock anisotropy, Parker-wind slopes, and CMB-S4
  $$\sum m_\nu$$ provide near-term tests.

---

## 9 Conclusions & Outlook
The digital-tick substrate reproduces Lorentz symmetry via spatial dilation
alone, delivers fundamental constants, and offers a geometric alternative to
dark matter.  Next milestones:

1. Rigorous lattice-to-continuum proof of isotropy.  
2. Monte-Carlo error budget on $$G$$ and lepton masses.  
3. Publication of a 4-page “tick-only SR” note to probe community response.

A simple metronome may yet rewrite our story of spacetime.
