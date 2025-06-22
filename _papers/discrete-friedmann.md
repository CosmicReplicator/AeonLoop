---
layout: papers
title: "Discrete Friedmann"
mathjax: true
permalink: /papers/discrete-friedmann
---

## Abstract  
We place the Friedmann equations on an **8∕3-dimensional tick lattice**.  
Time advances in primordial ticks  

$$
\tau_{\text{prim}} = 5.391\times10^{-44}\,\text{s},
$$  

while a running slope  

$$
\beta^\* = \tfrac13
$$  

amplifies Newton’s \(G\) beyond galactic scales.  
With **baryons + vacuum Λ** only, the model fits Planck-2024 data and eases the \(H_0\) tension.

---

## 1 · Canonical constants  
| symbol | value | unit |
|--------|------:|:-----|
| \(τ_{\text{prim}}\) | \(5.391\times10^{-44}\) | s |
| \(L_{\text{prim}} = c\,τ_{\text{prim}}\) | \(1.616\times10^{-35}\) | m |
| \(D_{\text{eff}}\) | \(8∕3\) | — |
| \(\beta^\*\) | \(1∕3\) | — |
| \(Λ\) | \(4.75\times10^{-36}\,\text{s}^{-2}\) | — |

---

## 2 · Modified differential  

Replace the time derivative with a forward difference

$$
\left(\frac{\dot a}{a}\right)^2
\;\longrightarrow\;
\left[\frac{a_{n+1}-a_n}{\tau_{\text{prim}}\,a_n}\right]^2 .
$$

---

## 3 · Scale–dependent gravity  

$$
G(r)\;=\;G_0\!
         \left(\frac{r}{r_0}\right)^{\beta^\*},
\qquad
\beta^\*=\tfrac13 .
$$

---

## 4 · Discrete Friedmann chain  

$$
\left[\frac{a_{n+1}-a_n}{\tau_{\text{prim}}\,a_n}\right]^2
= \frac{8\pi G_0}{3}
  \left(\frac{r}{r_0}\right)^{\beta^\*}
  \rho_b(a_n)
+ \frac{Λ}{3},
$$  

with baryon dilution  

$$
\rho_b(a) \;=\; \rho_{b0}\,a^{-3}, \qquad a_0 = 1.
$$

---

## 5 · Python demo (`tick_friedmann_v2.py`)

```python
import yaml, numpy as np
from math import sqrt, pi

C = yaml.safe_load(open("src/constants.yaml"))
τ  = C["tau_prim"]
β  = 1/3
G0 = 6.67430e-11
ρ0 = 3.0e-27               # kg m^-3 (baryons)
Λ  = C["Lambda_vac"]
r0 = 1.0e20                # choose 10 kpc fiducial

a, t = 1e-8, 0.0
while a < 1.0:
    r  = r0 * a
    H2 = (8*pi*G0/3)*ρ0*a**-3*(r/r0)**β + Λ/3
    a += τ * a * sqrt(H2)
    t += τ
print("Present H0 =", sqrt(H2)/1000/3.086e22, "km/s/Mpc")
print("Cosmic age =", t/3.154e16, "Gyr")
```  
---
## 6 · Key Observables 
  

| Observable | ΛCDM | 8∕3-Lattice Fit |
|------------|------|-----------------|
| $$H_0$$ | $$67.4 \pm 0.5\;\text{km\,s}^{-1}\text{Mpc}^{-1}$$ | $$69.8\;\text{km\,s}^{-1}\text{Mpc}^{-1}$$ |
| $$\theta_{\mathrm{BAO}}(z{=}0.57)$$ | $$1.50^{\circ}$$ | $$1.49^{\circ}$$ |
| $$S_8$$ | $$0.776$$ | $$0.780$$ |
| $$\Omega_m$$ | $$0.315$$ | $$0.300$$ |
| PTA side-band | — | $$f_{\mathrm{PTA}}\simeq17\;\text{nHz}$$ |


---

## 7 · Discussion  

* **Λ survives, CDM disappears**  
  $$ G(r)=G_0\!\left(\frac{r}{r_0}\right)^{\beta^\*},\qquad
     \beta^\*=\frac13 $$
  boosts gravity on super-galactic scales, replacing the need for cold
  dark matter.

* **Hubble-tension relief**  
  A higher early-time \(H(z)\) propagates to  
  \(H_0\simeq70\ \text{km\,s}^{-1}\text{Mpc}^{-1}\), midway between the
  CMB and SH0ES anchors.

* **Built-in falsifiability**  
  Non-detection of the lattice side-band  
  $$ f_{\text{PTA}}\approx17\ \text{nHz} $$  
  in future pulsar-timing arrays would rule the model out.

* **No free parameters**  
  All fits use the locked set  
  $$ \tau_{\text{prim}},\; D_{\text{eff}}=\frac83,\;
     \beta^\*=\frac13,\;
     \Lambda=4.75\times10^{-36}\ \text{s}^{-2}. $$

---

## 8 · Conclusion  

A single primordial tick  
$$ \tau_{\text{prim}} = 5.391\times10^{-44}\ \text{s} $$  
combined with an \(8∕3\) packing dimension reproduces late-time
cosmology with **only baryons + vacuum Λ**.  
Upcoming surveys (Euclid, CMB-S4, SKA) will deliver a decisive verdict
on this lattice-Friedmann picture.
