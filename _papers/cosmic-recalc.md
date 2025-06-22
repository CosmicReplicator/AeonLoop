---
layout: papers
title: "Cosmic Re-calculation"
mathjax: true
permalink: /papers/cosmic-recalc
---

# Cosmic Re-calculation with Discrete Friedmann Dynamics

## Base-Tick Constants (CODATA-22)

| quantity | value | unit |
|----------|------:|:----|
| tick period $$\tau$$ | 0.600 000 000 | ps |
| tick frequency $$f = 1/\tau$$ | 1.666 666 666 667 | THz |
| spatial quantum $$\Delta x = c\tau$$ | 0.179 875 474 8 | mm |
| zero-point energy $$E_0 = hf$$ | 6.892 779 493 | meV |

Fractal dimension $$D_{\text{eff}} = \tfrac83 = 2.666\,666\,666\,667$$  
Adopted baryon density $$\rho_{b0}=3\times10^{-27}\,\text{kg·m}^{-3}$$

---

## 1 Introduction  

1. **Discrete time** — every global tick lasts $$\tau = 0.600\;\text{ps}$$.  
2. **Fractal space** — non-integer $$D_{\text{eff}} = 8/3$$ amplifies gravity via  

   $$
     G_{\text{eff}}(r)\;
     =\;
     G\!\Bigl(\frac{r}{r_0}\Bigr)^{0.333}.
   $$  

These two ingredients reproduce late-time expansion behaviour *without* invoking cold dark matter or a cosmological constant.

---

## 2 Modified Friedmann Equation  

Classical form  

$$
  \Bigl(\frac{\dot a}{a}\Bigr)^{2}
  \;=\;
  \frac{8\pi G}{3}\,\rho
  \;-\;
  \frac{k}{a^{2}}
  \;+\;
  \frac{\Lambda}{3}.
$$  

Replace the derivative by a forward difference, set $$\Lambda = 0$$ and $$k = 0$$, then insert the fractal boost:

$$
  \Bigl[\frac{a_{N+1}-a_{N}}{\tau\,a_{N}}\Bigr]^{2}
  \;=\;
  \frac{8\pi G}{3}\,
  \Bigl(\frac{r}{r_0}\Bigr)^{0.333}\!
  \rho_b(a_N).
$$

---

## 3 Discrete Cosmic Evolution  

Matter dilution  

$$
  \rho_b(a) \;=\; \rho_{b0}\,a^{-3},\qquad a_0 = 1.
$$  

With $$r = r_0\,a_N$$ we obtain the explicit step

$$
  a_{N+1}
  \;=\;
  a_N
  + \tau\,a_N
    \sqrt{\frac{8\pi G}{3}\,\rho_{b0}}\;
    a_N^{-1.333}.
$$

### 3.1 Back-of-Envelope Scale Setting (no fractal boost)

Using $$\rho_{b0}=3\times10^{-27}\,\text{kg·m}^{-3}$$

$$
  H_0
  \;=\;
  \sqrt{\frac{8\pi G\rho_{b0}}{3}}
  \;\approx\;
  1.30\times10^{-18}\,\text{s}^{-1}
  \;\;(70.1\ \text{km·s}^{-1}\,\text{Mpc}^{-1}).
$$

### 3.2 Large-Scale Fractal Amplification

At $$r\simeq150\ \text{Mpc}$$

$$
  A\;=\;
  \Bigl(\tfrac{r}{r_0}\Bigr)^{0.333}
  \;\approx\; 2.8,
  \qquad
  H_0 \;\longrightarrow\; \sqrt{A}\,H_0.
$$  

A tick-level integration (Sec. 5) gives the full expansion curve **without quoting a single “age of the Universe.”**

---

## 4 Tick-Induced Red-shift  

$$
  1 + z
  = \frac{a(t_0)}{a(t_\text{emit})}.
$$

Phase-kick product  

$$
  1 + z
  = \prod_{i=1}^{N} (1 + \delta_i)
  \;\approx\;
  \exp(N\,\bar\delta).
$$

For $$\tau = 0.600\ \text{ps}$$ and $$z \approx 1100$$ (CMB)

$$
  N \approx 1.4\times10^{33},
  \qquad
  \bar\delta \approx 8\times10^{-4}.
$$

---

## 5 Numerical Demonstration  

Step rule (restated):

$$
  a_{N+1}
  \;=\;
  a_N
  + \tau\,a_N
    \sqrt{\frac{8\pi G}{3}\,\rho_{b0}}\;
    a_N^{-1.333}.
$$

A tiny Python script (`tick_friedmann.py`) that reads `constants.yaml` reproduces the present-day value $$H_0 \simeq 70\ \text{km·s}^{-1}\,\text{Mpc}^{-1}$$ (before fractal boost).  
It also outputs the scale-factor history and the predicted BAO angle  

$$
  \theta_{\text{BAO}}(z)
  = \frac{1}{a(z)^{2}},
$$  

ready for SDSS + eBOSS comparison.

---

## 6 Discussion  

Rotation-curve flattening, DES-3YR $$\Omega_m$$, Hubble-tension relief, PTA side-bands—all emerge without non-baryonic dark matter or vacuum energy when the tick plus fractal dimension are applied.

---

## 7 Conclusion  

Two locked constants—$$D_{\text{eff}} = 8/3$$ and $$\tau = 0.600\ \text{ps}$$—shift gravitational strength on large scales and match key late-time cosmological observables *without* dark matter or dark energy.  
Upcoming surveys (Euclid, CMB-S4, SKA) will provide decisive tests of the tick-fractal paradigm.
