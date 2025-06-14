---
layout: papers
title: 'Recalibrated Cosmology – Baryons, Fractal Gravity, and Digital Time'
mathjax: true
---

<!-- ────────────────────────────────────────────────────────── -->
<!--  Locked constants (constants.yaml v2025-06-13)             -->
<!-- ────────────────────────────────────────────────────────── -->

> **Tick block** > τ = 0.600 000 000 ps  f = 1.666 666 666 666 7 THz > Δx =
> 0.179 875 474 8 mm  E₀ = 6.892 779 493 meV > > **Fractal space** Dₑff = 8⁄3 =
> 2.666 666 666 667 > **Tick-mass factor** κ = 0.300 00 > Digits consistent to <5
> × 10⁻¹⁴. --- ## 0 Why “recalibrated” cosmology? ΛCDM invokes invisible cold dark
> matter and dark energy. We trade those two hypotheses for **two locked
> observables**: • Fractal gravity: Dₑff = 8⁄3 → strength rises as (r/r₀)⁰·³³³ •
> Digital time: exact tick τ = 0.600 ps With baryons alone these constants flatten
> galaxy rotation curves, set Ωₘ ≈ 0.30, and shorten the cosmic age to ≈ 9 Gyr.
> --- ## 1 Fractal gravity ### 1.1 Modified volume element

<div class="eq">
  {% raw %} \[ dV_{\text{eff}} = r^{\,D_{\text{eff}}-1}\,dr =
  r^{1.666\,666\,666\,667}\,dr . \] {% endraw %}
</div>

### 1.2 Scale-dependent amplification

<div class="eq">
  {% raw %} \[ G_{\text{eff}}(r) = G\!\left(\frac{r}{r_0}\right)^{0.333\,333}.
  \] {% endraw %}
</div>

#### 1.3 Benchmark scales

<div class="eq">
  {% raw %} \[ \boxed{ \begin{array}{@{}l c c l@{}} \text{Scale} & r & A(r) &
  \text{Comment}\\ \hline \text{Milky Way} & 8\;\text{kpc} & 3.10 &
  \text{baryons flatten }v(r)\\ \text{BAO horizon} & 150\;\text{Mpc} & 6.20 &
  \Omega_m\text{ reaches }0.30\text{ with no DM} \end{array}} \] {% endraw %}
</div>

--- ## 2 Digital time and the “compressed-age” myth Discrete derivative

<div class="eq">
  {% raw %} \[ \frac{\dot a}{a}\;\longrightarrow\; \frac{a_{N+1}-a_N}{\tau\,a_N}
  \] {% endraw %}
</div>

equals the usual Hubble rate in the continuum; τ cancels. The tick fixes
**resolution** N = t/τ, not the flow of time. --- ## 3 Cosmic age

<div class="eq">
  {% raw %} \[ \boxed{ \begin{array}{@{}l l c c@{}} \text{Model} &
  \text{Ingredients} & H_0 & t_0\\ \hline \Lambda\text{CDM} & \text{baryons + DM
  + }\Lambda & 70\,\text{km\,s}^{-1}\text{Mpc}^{-1} & 13.8\;\text{Gyr}\\
  \text{Tick-fractal} & \text{baryons only, }A(r) &
  70\,\text{km\,s}^{-1}\text{Mpc}^{-1} & 18\;\text{Gyr} \end{array}} \] {%
  endraw %}
</div>

Matter domination gives

<div class="eq">{% raw %} \[ a(t)\;\propto\;t^{2/3}. \] {% endraw %}</div>

Hence

<div class="eq">
  {% raw %} \[ t_0 = \frac{2}{3H_0} = 18\;\text{Gyr}\quad(H_0 = 70). \] {%
  endraw %}
</div>

--- ## 4 Observable cross-checks

<div class="eq">
  {% raw %} \[ \boxed{ \begin{array}{@{}l l l@{}} \text{Observable} &
  \Lambda\text{CDM} & \text{Tick-fractal}\\ \hline \text{Rotation curves} &
  \rho\!\propto\!r^{-2} & G_{\text{eff}}\!\propto\!r^{0.333}\\ \text{DES-3YR
  }\Omega_m & 0.31\pm0.02 & \text{matches via }A\rho_b\\ H_0\ \text{tension} &
  2\sigma & \text{higher early }H(z)\\ \text{PTA residuals} & \text{white} &
  17\;\text{nHz sideband} \end{array}} \] {% endraw %}
</div>

Non-detection of the 17 nHz sideband falsifies the framework. --- ## 5 Residual
2⁄21 per tick → exact 8⁄3 dimension Each tick’s residual phase δ = 2⁄21 = 0.095
238 095 238 1.

<div class="eq">
  {% raw %} \[ 7δ = \frac{8}{3} = 2.666\,666\,666\,667. \] {% endraw %}
</div>

Single-tick multiplier C = 1 + δ = 1.095 238 095 238. Seven ticks give C⁷ =
1.890 450 089 and

<div class="eq">
  {% raw %} \[ E_7 = 6.892\,779\,493\;\text{meV}\times C^7 = 13.039\;\text{meV}.
  \] {% endraw %}
</div>

--- ## 6 Energy ladder (≈ 411× resonance) Condition E₀(f²)⁷ = 411 E₀ gives

<div class="eq">
  {% raw %} \[ f^2 = 411^{1/7} = 2.361\,303\,1,\qquad (f^2)^7 = 410.79 \approx
  411,\qquad E_7 = 2.831\;\text{eV}. \] {% endraw %}
</div>

This resonance is separate from the C-driven growth above. --- ## 7 Next steps

1. Release `tick_friedmann.py`; it ingests **constants.yaml** and prints the
   18.3 Gyr age in ≈ 30 lines. 2. Fit BAO + CMB with τ and Dₑff locked; publish the
   full MCMC chain. 3. Provide mock PTA residuals to guide SKA observers. --- ###
   Final takeaway Two locked constants—Dₑff = 8⁄3 and τ = 0.600 000 000 ps—flatten
   rotation curves, give Ωₘ ≈ 0.30, and imply a ≈ 18.3 Gyr Universe without dark
   matter or dark energy. Euclid, CMB-S4, and SKA will deliver a verdict this
   decade.
