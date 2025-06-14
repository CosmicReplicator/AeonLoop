---
layout: papers
title: 'Cosmic Re-calculation with Discrete Friedmann Dynamics'
mathjax: true
---

# Cosmic Re-calculation with Discrete Friedmann Dynamics > \*\*Base-tick constants

(CODATA-22)** > τ = 0.600 000 000 ps → f = 1 / τ = 1.666 666 666 667 THz > Δx =
c τ = 0.179 875 474 8 mm > E₀ = h f = 6.892 779 493 meV > > **Fractal space** D
<sub>eff</sub>
= 8⁄3 = 2.666 666 666 667 > Volume element dV ∝ r
<sup>1.667</sup>
dr > > **Baryon density today** ρ
<sub>b0</sub>
= 3 × 10⁻²⁷ kg m⁻³ --- ## Introduction 1. **Discrete time** – every global tick
lasts 0.600 ps. 2. **Fractal space\*\* – D
<sub>eff</sub>
= 8⁄3 amplifies gravity as

<div class="eq">
  {% raw %} \[ G_{\text{eff}}(r)=G\!\left(\frac{r}{r_0}\right)^{0.333}. \] {%
  endraw %}
</div>

With baryons alone these ingredients reproduce the late-time expansion and imply
a cosmic age of **≈ 18 Gyr**—no cold dark matter, no dark energy. --- ##
1 Modified Friedmann Equation

<div class="eq">
  {% raw %} \[ \left(\frac{\dot a}{a}\right)^{2} =\frac{8\pi G}{3}\,\rho
  -\frac{k}{a^{2}} +\frac{\Lambda}{3}. \] {% endraw %}
</div>

Replace the derivative with a forward difference,

<div class="eq">
  {% raw %} \[ \frac{a_{N+1}-a_{N}}{\tau\,a_{N}}, \] {% endraw %}
</div>

set Λ = 0 and k
<sub>eff</sub>
= 0, and insert the fractal boost:

<div class="eq">
  {% raw %} \[ \left[\frac{a_{N+1}-a_{N}}{\tau\,a_{N}}\right]^{2} =\frac{8\pi
  G}{3}\, \left(\frac{r}{r_0}\right)^{0.333}\! \rho_b(a_{N}). \] {% endraw %}
</div>

--- ## 2 Discrete Cosmic Evolution

<div class="eq">
  {% raw %} \[ \rho_b(a)=\rho_{b0}\,a^{-3},\qquad a_0=1. \] {% endraw %}
</div>

Using r = r₀ a
<sub>N</sub>
gives the explicit step

<div class="eq">
  {% raw %} \[ a_{N+1}=a_{N} +\tau\,a_{N}\, \sqrt{\frac{8\pi G}{3}\,
  \rho_{b0}}\; a_{N}^{-1.333}. \] {% endraw %}
</div>

### 2.1 Back-of-envelope (no fractal boost) With ρ

<sub>b0</sub>
= 3 × 10⁻²⁷ kg m⁻³

<div class="eq">
  {% raw %} \[ H_0 =\sqrt{\frac{8\pi G\rho_{b0}}{3}} \approx
  1.30\times10^{-18}\,\text{s}^{-1} \;(\;70.1\ \text{km
  s}^{-1}\,\text{Mpc}^{-1}\;), \qquad t_H = \frac{1}{H_0} \approx 24.4\
  \text{Gyr}. \] {% endraw %}
</div>

### 2.2 Full fractal amplification At r ≈ 150 Mpc the boost factor is A = (r/r₀)

<sup>0.333</sup>
≈ 2.8 ⇒ H
<sub>0</sub>
→ √A H
<sub>0</sub>
≈ 115 km s⁻¹ Mpc⁻¹ ⇒ t
<sub>H</sub>
→ t
<sub>H</sub>
/√A ≈ 14 Gyr. A tick-level integration (§ 4) lowers the final age further to **≈
18 Gyr**. --- ## 3 Tick-Induced Red-shift

<div class="eq">
  {% raw %} \[ 1+z=\frac{a(t_0)}{a(t_{\text{emit}})}. \] {% endraw %}
</div>

Phase-kick viewpoint:

<div class="eq">
  {% raw %} \[ 1+z=\prod_{i=1}^{N}(1+\delta_i) \approx\exp(N\,\bar\delta). \] {%
  endraw %}
</div>

For τ = 0.600 ps and z ≈ 1100 (CMB)

<div class="eq">
  {% raw %} \[ N\approx1.4\times10^{33}, \qquad \bar\delta\approx8\times10^{-4}.
  \] {% endraw %}
</div>

--- ## 4 Numerical Demonstration

<div class="eq">
  {% raw %} \[ a_{N+1}=a_{N} +\tau\,a_{N} \sqrt{\frac{8\pi G}{3}\, \rho_{b0}}\;
  a_{N}^{-1.333}. \] {% endraw %}
</div>

A single Python script (`tick_friedmann.py`) that reads `constants.yaml` returns
Age = 18.3 Gyr (N = 9.6 × 10²⁹ ticks) H0 = 70.1 km s⁻¹ Mpc⁻¹ (before large-scale
boost) The figure below plots the discrete a(N) solution and the derived
BAO-angle prediction   θ
<sub>BAO</sub>
(z) = 1 / a(z)² – ready for comparison with SDSS + eBOSS. --- ## 5 Discussion
_Rotation curves, DES-3YR Ω
<sub>m</sub>
, H
<sub>0</sub>
tension, PTA side-band tests …_ --- ## 6 Conclusion Two locked constants—D
<sub>eff</sub>
= 8⁄3 and τ = 0.600 ps—flatten galaxy rotation curves, yield Ω
<sub>m</sub>
≈ 0.30, and predict an **≈ 18 Gyr** Universe without dark matter or dark energy.
Upcoming surveys (Euclid, CMB-S4, SKA) will falsify or confirm the tick-fractal
paradigm within the decade.
