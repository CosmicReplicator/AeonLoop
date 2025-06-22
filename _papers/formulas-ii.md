---
layout: papers
title: 'Formulas II'
series: formulas
order: 2
mathjax: true
permalink: /papers/formulas-ii
---

{% raw %}
<div class="mermaid" markdown="0">
flowchart TD
  A["τ = 0.600 ps"] -- "1 / τ" --> B
  B["f = 5 / 3 THz"] --| h --> C[h]
  C --> D["E₀ = h f"]
  C -- "Δx = c τ" --> E["Δx = c τ"]
  E -- "D_eff = 8 / 3" --> F["Volume law"]
  D -- "anchor W boson" --> G["Energy Ladder"]
  G --| β = 1 / 3 --> H["a(t) ∼ t^{3/4}"]
  F --| β = 1 / 3 --> H
  E  -. "Q = 409.8" .-> G
</div>
{% endraw %}

## 4 · Cosmological-Constant Sketch

$$
\Lambda \sim \frac{1}{L_{\text{curv}}^{2}}, \quad
L_{\text{curv}} \approx \left(\frac{\hbar c}{\rho_{\text{vac}}^{(3D)}}\right)^{1/4}
$$

$$
L = \Delta x \approx 0.18~\text{mm}
$$

$$
L_{\text{cosmo}} \sim 10^{26}~\text{m}
$$

$$
\Rightarrow \Lambda \sim 10^{-52}~\text{m}^{-2}
$$

---

## 5 · Fine-Structure Constant from Fractal Geometry

$$
\alpha = \exp\left[-\,C_{\alpha}(D_{\text{eff}} - 2)\right]
= \exp\left[-\,7.379\,970\,056 \times \tfrac{2}{3}\right]
\approx \frac{1}{137.035999}
$$

---

## 6 · Tick-Based Lorentz Block

$$
\gamma = \frac{1}{\sqrt{1 - \beta^2}}, \quad
\beta = \frac{v \tau}{\Delta x} = \frac{v}{c}, \quad
c = \frac{\Delta x}{\tau}
$$

---

## 7 · Quick-Look Examples

- **GPS red-shift (1 m height)**  
  $$
  \Delta f / f = 1.09 \times 10^{-16}
  $$

- **Tick density at Earth’s surface**  
  $$
  1 - 6.946 \times 10^{-10}
  $$

- **Missing-brick curvature slice**  
  $$
  \frac{1}{9} \text{ of the nine-brick ledger}
  $$

<p style="text-align: right; font-size: 0.85em">
  ⇦ to Part III:&nbsp;
  <a class="button" href="formulas-iii.html" target="_blank">Formula III</a>
</p>
