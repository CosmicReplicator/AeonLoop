---
layout: papers
title: "Formulas I"
series: formulas      # common tag for every formula paper
order: 1              # 1 , 2 , 3 … in reading order
mathjax: true
---

## Digital-Tick Model — Locked Constants (v 2025-06-13)

$$
\boxed{
\begin{array}{@{} r @{\,=\,} l @{\qquad} r @{\,=\,} l @{}}
  \tau      & 0.600\,000\,000\;\mathrm{ps} &
  E_{0}     & 6.892\,779\,493\;\mathrm{meV} \

\[2pt]
  f         & 1.666\,666\,666\,666\,7\;\mathrm{THz} &
  m_{\text{eff}} & 1.093\times10^{-38}\;\mathrm{kg} \

\[2pt]
  \Delta x  & 0.179\,875\,474\,8\;\mathrm{mm} &
  G_{\text{tick}} & 4.51\times10^{-62} \

\[2pt]
  h         & 4.135\,667\,696\times10^{-15}\;\mathrm{eV\!\cdot\!s} &
  G         & 6.67\times10^{-11}\;\mathrm{m^{3}kg^{-1}s^{-2}} \

\[2pt]
  \hbar     & 6.582\,119\,569\times10^{-16}\;\mathrm{eV\!\cdot\!s} &
  \alpha    & 7.297\,352\,5693\times10^{-3} \

\[2pt]
  C_{\alpha}& 7.379\,970\,056 &
  D_{\text{eff}} & \dfrac{8}{3}=2.666\,666\,666\,\overline{7} \

\[2pt]
  \kappa    & 0.447 & &
\end{array}}
$$

---

## 1 · Finite-Difference Operators

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

## 2 · Electromagnetic Tensor & Lagrangian

$$
F_{\mu\nu} = \partial_{\mu}A_{\nu} - \partial_{\nu}A_{\mu},
\qquad
\mathcal L = -\tfrac14\,F_{\mu\nu}F^{\mu\nu}.
$$

Discrete Euler–Lagrange steps recover Maxwell in the continuum limit as
$$\tau, \Delta x \to 0$$.

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
  <a class="button" href="Formulas_II.html" target="_blank">Formula II</a>
</p>
