---
layout: papers
title: 'Formulas I'
markdown: false
---

<h2>Digital-Tick Model — Locked Constants (v 2025-06-13)</h2>

<div class="eq">
  {% raw %} \[ \boxed{ \begin{array}{@{}r@{\,=\,}l @{\qquad} r@{\,=\,}l@{}} \tau
  & 0.600\,000\,000\ \mathrm{ps} & E_{0} & 6.892\,779\,493\ \mathrm{meV} \\ f &
  1.666\,666\,666\,666\,7\ \mathrm{THz} & m_{\text{eff}} & 1.093\times10^{-38}\
  \mathrm{kg} \\ \Delta x & 0.179\,875\,474\,8\ \mathrm{mm} & G_{\text{tick}} &
  4.51\times10^{-62} \\ h & 4.135\,667\,696\times10^{-15}\ \mathrm{eV\!\cdot\!s}
  & G & 6.67\times10^{-11}\ \mathrm{m^{3}kg^{-1}s^{-2}} \\ \hbar &
  6.582\,119\,569\times10^{-16}\ \mathrm{eV\!\cdot\!s} & \alpha &
  7.297\,352\,5693\times10^{-3} \\ C_{\alpha} & 7.379\,970\,056 & D_{\text{eff}}
  & \dfrac{8}{3}=2.666\,666\,666\,\overline{7} \\ \kappa & 0.447 & & % last cell
  blank \end{array}} \] {% endraw %}
</div>

<hr />

<h2>1 · Finite-Difference Operators</h2>

<p><em>Discrete update of the four-potential</em></p>
<div class="eq">
  \[ A_{\mu}(t+\tau,x)=A_{\mu}(t,x)+\tau\,\partial_{t}A_{\mu}(t,x)+\mathcal
  O(\tau^{2}). \]
</div>

<p><em>First- and second-order time derivatives</em></p>
<div class="eq">
  \[ \partial_{t}A_{\mu}\approx\frac{A_{\mu}(t+\tau)-A_{\mu}(t)}{\tau},\qquad
  \partial_{t}^{2}A_{\mu}\approx
  \frac{A_{\mu}(t+\tau)-2A_{\mu}(t)+A_{\mu}(t-\tau)}{\tau^{2}}. \]
</div>

<p><em>Spatial derivative</em></p>
<div class="eq">
  \[ \partial_{x}A_{\mu}\approx\frac{A_{\mu}(t,x+\Delta x)-A_{\mu}(t,x)}{\Delta
  x}. \]
</div>

<hr />

<h2>2 · Electromagnetic Tensor & Lagrangian</h2>

<div class="eq">
  \[ F_{\mu\nu}=\partial_{\mu}A_{\nu}-\partial_{\nu}A_{\mu},\qquad \mathcal
  L=-\tfrac14 F_{\mu\nu}F^{\mu\nu}. \]
</div>

<p class="note">
  Discrete Euler–Lagrange steps recover Maxwell in the continuum limit as
  \(\tau,\Delta x\to0\).
</p>

<hr />

<h2>3 · Basic Derived Relations</h2>

<table>
  <tr>
    <td><strong>Plane-wave dispersion</strong></td>
    <td><div class="eq">\[\omega^{2}=c^{2}k^{2}.\]</div></td>
  </tr>

  <tr>
    <td><strong>Optimal delayed-choice path</strong></td>
    <td>\( \Delta x = 0.179\,875\,474\,8\;\mathrm{mm}\)</td>
  </tr>

  <tr>
    <td><strong>Neutrino mass estimate</strong></td>
    <td>
      \(m_\nu \approx 5\;\mathrm{meV}\) (from \(E_{0}\) & \(D_{\text{eff}}\))
    </td>
  </tr>

  <tr>
    <td><strong>Gravitational red-shift</strong></td>
    <td>matches GPS factor \(6.946\times10^{-10}\)</td>
  </tr>
</table>

<p style="text-align: right; font-size: 0.85em">
  ➜ Continue to Part II:&nbsp;
  <a class="button" href="Formulas_II.html" target="_blank">Formula II</a>
</p>
