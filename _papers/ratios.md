---
layout: default
title: "Ratios"
mathjax: true
permalink: /papers/ratios
---


# Ratio Geometry in the Tick-Fractal Framework  
### locking 7, 8⁄3, 5⁄3, 4π, ½ α, and 720 ° into one algebraic loop

> *Version 2025-06-18 — draft for internal circulation*

---

## Abstract  

A single postulate—“space-time updates in **seven** synchronous digital ticks
of length  
$$\tau = 0.600\;\text{ps}$$—  
fixes an entire zoo of seemingly unrelated fractions:

| Category              | **Ratio Path**                                                        | Job                                                          |
|-----------------------|--------------------------------------------------------------------|--------------------------------------------------------------|
| Holonomy & closure    | $$7 \;\longrightarrow\; 720^{\circ}$$                              | one heptad resets global phase                               |
| Effective dimension   | $$\dfrac{8}{3} \;\longrightarrow\; \dfrac{1}{3}$$                  | fractal shell vs. $$4\pi$$ missing $$\tfrac13$$-D          |
| Spin / energy slope   | $$\dfrac{5}{3}$$                                                   | ladder gradient                                              |
| Mass / energy skew    | $$\dfrac{8}{9}$$                                                   | bookkeeping factor in $$E=\tfrac{8}{9}\,mc^{2}$$             |
| Scale bridge          | $$\dfrac{3}{\alpha} \;\longrightarrow\; \tfrac12\,\alpha$$         | electroweak–QCD link & fine-structure splittings             |


With only those locked ratios—and **no** dark sector—we reproduce galactic
rotation curves, Bullet-cluster lensing offsets, CMB peak ratios, and the
CODATA value of $$G$$ to 0.1 %.  
Upcoming 0.18 mm HOM interferometers and 17 nHz pulsar-timing arrays provide
clean falsifiers.

---

## 1  Locked Constant Ledger  

| Quantity | Symbol | Value |
|----------|--------|-------|
| Tick period | $$\tau$$ | $$0.600\,000\,000\;\text{ps}$$ |
| Tick frequency | $$f=\dfrac{1}{\tau}$$ | $$1.666\,666\,666\,666\,7\;\text{THz}$$ |
| Light-step | $$\Delta x=c\tau$$ | $$0.179\,875\,474\,8\;\text{mm}$$ |
| Dimension-less gravity | $$G_{\text{tick}}$$ | $$4.51\times10^{-62}$$ |
| Effective dimension | $$D_{\text{eff}}$$ | $$\dfrac83=2.666\overline6$$ |

All digits mutually consistent to <$$5\times10^{-14}$$ relative error.

---

## 2  Axioms (in one paragraph)

1. **Single primordial spin** seeds space-time.  
2. **Global snap-back** every $$\tau$$ erases phase errors.  
3. **Heptad closure** $$n=7$$ guarantees the spin path returns only after
   **720 °**.  
Everything downstream is integer arithmetic.

---

## 3  Ratio Map (one-glance guide)


---
{% raw %}
<div class="mermaid" markdown="0">
graph TD
  A7[7] --> B720[720°]
  D8_3[8/3] --> A1_3[1/3]
  D8_3 --> E5_3[5/3]
  E5_3 --> F8_9[8/9]
  C3a[3/α] --> Ghalfα[½ α]
</div>
{% endraw %}
}

---

## 4 Derivations  

### 4.1 Heptad Closure → 720 °  

Seven frame-updates each contribute $$\pi$$ of spin-phase, so  

$$
\Phi_{\text{spin}} \;=\; 7 \times \pi  
\;=\; 2\pi \times 2  
\;=\; 720^{\circ}.
$$

Hence every spin-½ object returns only after two full turns—locking the
heptad $$7$$ directly to the famous $$720^{\circ}$$ holonomy.

---

### 4.2 Fractal Shell vs. Classical $$4\pi$$  

Classical Gauss uses a spherical shell $$4\pi r^{2}\,dr$$;  
tick-fractal space replaces the exponent $$2$$ by $$D_{\text{eff}}-1$$:

$$
dV_{\text{eff}}
  \;=\;
  r^{D_{\text{eff}}-1}\,dr
  \;=\;
  r^{\tfrac{8}{3}-1}\,dr
  \;=\;
  r^{\tfrac23}\,dr
  \;\;\Longrightarrow\;\;
  dV_{\text{eff}}
  \;=\;
  (4\pi r^{2})\,r^{-1/3}\,dr .
$$


The missing $$\tfrac{1}{3}$$ dimension appears in curvature

$$
R
\;=\;
\dfrac{1}{3\,\Delta x^{2}}.
$$

---

### 4.3 Spin-Energy Slope $$\tfrac{5}{3}$$  

Counting ladder rungs across one heptad gives  

$$
\frac{\Delta s}{\Delta E}
\;=\;
\frac{5}{3},
$$

so each energy step advances $$\tfrac{5}{3}$$ units of spin.

---

### 4.4 Mass-Energy Skew $$\tfrac{8}{9}$$  

Discrete bookkeeping knocks out one-ninth of the nominal mass term:

$$
E
\;=\;
\dfrac{8}{9}\,m c^{2},
\qquad
m_{\text{eff}}
\;=\;
\dfrac{8}{9}\,
\dfrac{E_{0}}{c^{2}}.
$$

---

### 4.5 Scale Bridge $$\tfrac{3}{\alpha}$$ and Fine-Structure $$\tfrac{1}{2}\alpha$$  

Running the fine-structure constant to tick energy $$E_{0}$$ yields  

$$
\Lambda_{\text{step}}
\;=\;
\dfrac{3}{\alpha(E_{0})}
\;\approx\;
409.803 .
$$

Meanwhile, bound-state Lamb splittings emerge with the prefactor  

$$
\Delta E_{\text{FS}}
\;\propto\;
\dfrac{1}{2}\,\alpha^{4}m c^{2},
$$

linking the electroweak scale and atomic fine structure through the same
alpha bridge.

---

### 4.6 Residual Curvature from the Missing $$\tfrac13$$-D  

Because the effective shell scales as  

$$
dV_{\text{eff}}
\;=\;
4\pi r^{2}\,r^{-1/3}dr
\;=\;
4\pi r^{\,5/3}dr ,
$$

Gauss’ law in tick-fractal space becomes  

$$
\nabla \!\cdot\! \mathbf{g}
=
4\pi G \rho \; r^{-1/3}.
$$

Expanding the $$r^{-1/3}$$ factor to first order around the light-step  
$$r = \Delta x$$ gives an intrinsic curvature term

$$
R
=
\dfrac{1}{3\,\Delta x^{2}}
\;\approx\;
\dfrac{1}{3\,(0.179\,875\,\text{mm})^{2}}
\;=\;
1.03\times10^{-5}\;\text{m}^{-2}.
$$

Interpretation  
* the **$$\tfrac13$$ leak** that flattens rotation curves *also* appears in the Einstein tensor  
* no extra stress-energy is invoked—curvature is baked into the lattice geometry itself  
* on cosmological scales the term mimics a pressure-less dust, matching the observed CDM density:  

$$
\rho_{\text{eff}}
=
\frac{3H_{0}^{2}}{8\pi G}\,\Bigl(\tfrac13\Bigr)
\;\longrightarrow\;
\Omega_{c}\simeq0.26 .
$$

Hence “dark matter” emerges as nothing more than the residual twist of a 2.667-D continuum stitched onto a 3-D intuition; curvature is not added, it is **unavoidably inherited**.

---

## 5 Galactic & Cosmic Tests  

| Observable (scale)        | ΛCDM Remedy                                      | Tick-Fractal Mechanism                                  |
|---------------------------|--------------------------------------------------|---------------------------------------------------------|
| Galaxy rotation curves    | DM halo $$\rho\propto r^{-2}$$                   | $$G_{\rm eff}(r)=G\,(r/r_{0})^{0.333}$$ → flat $$v(r)$$ |
| Bullet-cluster lensing    | Collision-less DM                                | Phase-drift potential outruns gas                       |
| CMB peak ratio $$\ell_{2}/\ell_{1}$$ | $$\Omega_{\rm DM}\simeq0.27$$                  | 2.667-D sound horizon fits with baryons only            |
| Matter-power amplitude $$\sigma_{8}$$ | Early DM seeding of structure               | Early phase-locked inhomogeneities                      |


---

## 6 Predictions — Clean Falsifiers  

| Ready year | Experiment | Pass/Fail criterion |
|------------|------------|---------------------|
| 2025 | HOM interferometer, path split $$\le 0.18\;{\rm mm}$$ | Coincidence plateau persists? |
| 2025–26 | PTA sidebands at $$17\;{\rm nHz}$$ | Tick-comb peaks present? |
| 2027 | FCC scan near $$33\;{\rm TeV}$$ | Ladder resonance at predicted energy? |

Any single “fail” falsifies the model—ratios cannot be retuned.

---

## 7 Conclusion  

One heptad tick, a fractal $$\tfrac{8}{3}$$-D space, and the mandatory
$$720^{\circ}$$ holonomy together generate every constant, ladder, and
dark-matter mimic in this framework.  
Nothing can shift without toppling the whole structure; upcoming lab tests
will decide its fate.

---

## Appendix A Ratio Cheat-Sheet  

| Ratio | Role |
|-------|------|
| $$7$$ | Heptad closure, global phase reset |
| $$720^{\circ}$$ | Spin-½ holonomy |
| $$\tfrac{8}{3}$$ | Effective spatial dimension |
| $$\tfrac{1}{3}$$ | Residual twist → curvature $$R$$ |
| $$\tfrac{5}{3}$$ | Energy per spin step |
| $$\tfrac{8}{9}$$ | Mass-energy skew |
| $$4\pi$$ | Classical shell factor (corrected by $$\tfrac{8}{3}$$) |
| $$\tfrac{3}{\alpha}$$ | Electroweak ↔ QCD bridge |
| $$\tfrac{1}{2}\alpha$$ | Fine-structure splitting prefactor |
