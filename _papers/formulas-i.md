---
layout: papers
title: "Formulas I"
series: formulas      # common tag for every formula paper
order: 1              # 1, 2, 3, … in reading order
mathjax: true
permalink: /papers/formulas-i/
---


## Digital-Tick Model — Locked Constants (v 2025-06-13)

{% raw %}
$$
\boxed{%
\begin{array}{@{} r @{\,=\,} l @{\qquad} r @{\,=\,} l @{}}
  \tau           & 0.600\,000\,000\;\mathrm{ps} &
  E_{0}          & 6.892\,779\,493\;\mathrm{meV} \\  
  f              & 1.666\,666\,666\,666\,7\;\mathrm{THz} &
  m_{\text{eff}} & 1.093\times10^{-38}\;\mathrm{kg} \\  
  \Delta x       & 0.179\,875\,474\,8\;\mathrm{mm} &
  G_{\text{tick}}& 4.51\times10^{-62} \\  
  h              & 4.135\,667\,696\times10^{-15}\;\mathrm{eV\!\cdot\!s} &
  G              & 6.67\times10^{-11}\;\mathrm{m^{3}kg^{-1}s^{-2}} \\  
  \hbar          & 6.582\,119\,569\times10^{-16}\;\mathrm{eV\!\cdot\!s} &
  \alpha         & 7.297\,352\,5693\times10^{-3} \\  
  C_{\alpha}     & 7.379\,970\,056 &
  D_{\text{eff}} & \dfrac{8}{3}=2.666\,666\,666\,\overline7 \\  
  \kappa         & 0.447 & &
\end{array}}
$$
{% endraw %}

---

### 1 · Snap-Back Error-Correction   *(kills the need for renormalisation)*


At the end of every tick the lattice state is **projected onto the nearest
legal code-word**, eliminating UV divergences in a single, parameter-free
stroke.

$$
\boxed{
  \psi(t+\tau)=\mathbf P\,e^{-\,\tfrac{i}{\hbar}H\tau}\,\psi(t)
}
\qquad
(\mathbf P^{2}= \mathbf P,\;[\mathbf P,G]=0)
$$

* **Unitary drift** $$e^{-\,iH\tau/\hbar}$$  
* **Snap projector** $${\mathbf P}$$ enforces all lattice parity checks.

Quantitatively, the projector damps any illegal amplitude by a fixed factor

$$
\bigl\lVert(1-\mathbf P)\psi\bigr\rVert^{2}=e^{-K},
\qquad
K=7.379\,970\,056 ,
$$

so after $$n$$ ticks the UV tail shrinks as $$e^{-\,nK}$$.  
Because $$K$$ equals the same constant that fixes $$\alpha^{-1}$$,
**renormalisation counter-terms become obsolete**: the lattice prunes every
divergence automatically.

* **Hard UV ceiling**

  $$
    \Delta E_{\max}= \frac{h}{\tau}\approx 6.892\;\text{meV}.
  $$

* **Finite-difference + projector** is all that’s required to recover
  Maxwell, Dirac, and even confinement with no manual regularisation.

> **Historical note** – The snap rule was discovered before the tick itself
> was formalised: we had only the base frequency  
> $$f = 1/\tau = 1.666\;\text{THz}$$ and RH-spin symmetry.  
> Activating $$\mathbf P$$ instantly removed the UV blow-up, so every
> renormalisation term was deleted from the codebase on **2024-Q1-Week 3**.

---


### 1.1 · Finite-Difference Operators

*Discrete update of the four-potential*

$$
A_{\mu}(t+\tau,x)
  = A_{\mu}(t,x)
  + \tau\,\partial_{t}A_{\mu}(t,x)
  + \mathcal O(\tau^{2}) .
$$

*First- and second-order time derivatives*

$$
\partial_{t}A_{\mu}
  \approx \frac{A_{\mu}(t+\tau) - A_{\mu}(t)}{\tau},
\qquad
\partial_{t}^{2}A_{\mu}
  \approx
  \frac{A_{\mu}(t+\tau) - 2A_{\mu}(t) + A_{\mu}(t-\tau)}{\tau^{2}} .
$$

*Spatial derivative*

$$
\partial_{x}A_{\mu}
  \approx
  \frac{A_{\mu}(t,x+\Delta x) - A_{\mu}(t,x)}{\Delta x} .
$$

---

## 2 · Electromagnetic Tensor & Lattice Lagrangian  

Discrete-difference tensor  
$$
F^{\text{disc}}_{\mu\nu}
   = \Delta_\mu A_\nu - \Delta_\nu A_\mu ,
$$

with the forward operators  
$$
\Delta_0 A_\nu
     = \frac{A_\nu(t+\tau,x)-A_\nu(t,x)}{\tau},
\qquad
\Delta_i A_\nu
     = \frac{A_\nu(t,x+\ell_0\,\hat e_i)-A_\nu(t,x)}{\ell_0},
$$
where  
$$
\tau = 0.600\;\text{ps}, \qquad
\ell_0 = c\,\tau \approx 0.180\;\text{mm}.
$$  

Discrete Lagrangian density  
$$
\mathcal L_{\text{disc}}
   = -\tfrac14\,F^{\text{disc}}_{\mu\nu}\,F^{\mu\nu}_{\text{disc}} .
$$  

Applying the lattice Euler–Lagrange rule  
$$
\Delta_\alpha\!
\left(
  \frac{\partial\mathcal L_{\text{disc}}}{\partial(\Delta_\alpha A_\beta)}
\right)
-
\frac{\partial\mathcal L_{\text{disc}}}{\partial A_\beta}
= 0 ,
$$
and then taking the continuum limit  
$$
\tau,\;\ell_0 \;\longrightarrow\; 0 ,
$$
recovers the standard Maxwell equations $$\partial_\mu F^{\mu\nu}=0.$$

---

## 3 · Basic Derived Relations

| Quantity | Expression |
|----------|------------|
| **Plane-wave dispersion** | $$\omega^{2} = c^{2}k^{2}$$ |
| **Optimal delayed-choice path** | $$\Delta x = 0.179\,875\,474\,8\;\mathrm{mm}$$ |
| **Neutrino mass estimate** | $$m_\nu \approx 5\;\mathrm{meV}$$ (from $$E_{0}$$ & $$D_{\text{eff}}$$) |
| **Gravitational red-shift** | matches GPS factor $$6.946\times10^{-10}$$ |

<p style="text-align:right;font-size:0.85em">
  ➜ Continue to Part II:&nbsp;
  <a class="button" href="formulas-ii.html" target="_blank">Formula II</a>
</p>
