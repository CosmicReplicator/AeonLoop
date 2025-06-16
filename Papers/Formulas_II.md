---
layout: papers
title: 'Formulas II'
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
---

<h2>4 · Cosmological-Constant Sketch</h2>

<div class="eq">
  \[ \Lambda \;\sim\; \frac{1}{L_{\text{curv}}^{2}},\qquad L_{\text{curv}}
  \;\approx\; \bigl(\hbar c/\rho_{\text{vac}}^{(3D)}\bigr)^{1/4}. \]
</div>

<p>
  Hierarchy \(L=\Delta x\approx0.18\text{ mm}\) versus
  \(L_{\text{cosmo}}\sim10^{26}\text{ m}\) suppresses \(\Lambda\) to
  \(\sim10^{-52}\text{ m}^{-2}\).
</p>

<hr />

<h2>5 · Fine-Structure Constant from Fractal Geometry</h2>

<div class="eq">
  \[ \alpha =\exp\!\bigl[-\,C_{\alpha}\,(D_{\text{eff}}-2)\bigr]
  =\exp\!\bigl[-\,7.379\,970\,056\times\tfrac23\bigr]
  \approx\frac{1}{137.035999}. \]
</div>

<hr />

<h2>6 · Tick-Based Lorentz Block</h2>

<div class="eq">
  \[ \gamma =\frac{1}{\sqrt{\,1-\beta^{2}\,}}, \qquad
  \beta=\frac{v\,\tau}{\Delta x} =\frac{v}{c}, \qquad c=\frac{\Delta x}{\tau}.
  \]
</div>

<hr />

<h2>7 · Quick-Look Examples</h2>

<ul>
  <li>
    <strong>GPS red-shift (1 m height)</strong>
    \(\Delta f/f = 1.09\times10^{-16}\)
  </li>
  <li>
    <strong>Tick density at Earth’s surface</strong>
    \(1-6.946\times10^{-10}\)
  </li>
  <li>
    <strong>Missing-brick curvature slice</strong>
    \(1/9\) of the nine-brick ledger
  </li>
</ul>

<p style="text-align: right; font-size: 0.85em">
  ⇦ to Part III:&nbsp;
  <a class="button" href="Formulas_III.html" target="_blank">Formula III</a>
</p>
