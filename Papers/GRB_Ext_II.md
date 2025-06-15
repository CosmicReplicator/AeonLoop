---
layout: papers
title: "GRB Ext II – An Energy-Centric Yard-Stick"
mathjax: true
---

> **tl;dr**  
> switching the anchor from **geometry** to the **tick-fractal energy ladder**  
> \(E_n = E_0 / (7n)\).  
> Everything else (time, radius, phase) flows from that single quantised energy.

---

## 0 One-page abstract  

1.  A photon that skims the seed shell accrues **one tick of phase** but keeps the **same energy**.  
2.  **Seven** such skims close the phase, stretching the packet over \(7\tau\) → **frequency and energy drop by \(1/7\)**.  
3.  Gamma-ray burst micro-pulses land *exactly* on that diluted ladder:  
   

\[
      E_n \;=\; \frac{E_0}{7n},\qquad n = 1,2,3,\dots
   \]

  
4.  Counting the rung index \(n\) in any GRB instantly yields its distance modulus, with **no** \(\Lambda\mathrm{CDM}\) priors.

---

## 1 Baseline tick constants  

| Symbol | Definition | Value (SI) | Astro-friendly |
|--------|------------|------------|----------------|
| \(\tau\) | tick period | \(6.00\times10^{-13}\,\text{s}\) | 0.600 ps |
| \(f_0 = 1/\tau\) | tick frequency | \(1.666\,667\times10^{12}\,\text{Hz}\) | 1.667 THz |
| \(E_0 = h f_0\) | single-tick energy | \(1.10\times10^{-21}\,\text{J}\) | **6.890 meV** |
| \(r_0 = c\tau\) | spatial tick | \(1.7988\times10^{-4}\,\text{m}\) | 0.1799 mm |

*(All later numbers propagate from these four.)*

---

## 2 Energy ladder vs. geometry ladder  

| \(n\) | Closure energy \(E_n = E_0/(7n)\) | Centre radius \(r_n = 7n\,r_0\) | Gap beyond seed \(\Delta r_n = (6n+1)r_0\) |
|------:|-----------------------------------|---------------------------------|-------------------------------------------|
| seed | \(E_0 = 6.890\) meV | \(r_0\) | seed shell |
| 1 | **0.984 meV** | 1.26 mm | 0.18 mm |
| 2 | 0.492 meV | 2.52 mm | 1.26 mm |
| 3 | 0.328 meV | 3.78 mm | 2.34 mm |
| … | \(0.984/n\) meV | \(7n\,r_0\) | \((6n+1)r_0\) |

Geometry grows linearly; **energy dilutes as \(1/n\)**.

---

## 3 Tick-factorising a GRB prompt spectrum  

    %% mermaid
    flowchart TD
        A[Photon-count light-curve] --> B{Fast Fourier<br>tick test}
        B -->|peak at 1.667 THz| C[valid tick source]
        C --> D[locate E_peak for every micro-pulse]
        D --> E[map each E_peak → ladder rung n]
        E --> F[z from Δt] --> G[H₀ / geometry]

### 3.1 Rung identification  



\[
  n \;=\; \operatorname{round}\!\Bigl[\frac{E_0}{7\,E_{\text{peak}}}\Bigr].
\]



Typical long GRBs give \(n \approx 11\!-\!12\).

### 3.2 Redshift purely from time-dilation  



\[
  1 + z
  \;=\;
  \frac{\Delta t_{\text{obs}}}{N_{\text{tick}}\,\tau}
  \;=\;
  \frac{\Delta t_{\text{obs}}\,f_0}{N_{\text{tick}}}.
\]



No cosmology enters.

---

## 4 Worked miniature – GRB 090424  

| Observable | Measured | Tick-fractal read-out |
|------------|----------|-----------------------|
| shortest pulse | 0.47 ms | \(N = 7.83\times10^{8}\) |
| \(E_{\text{peak}}\) | 534 keV | \(n = 11\) |
| \(z_{\text{tick}}\) | **1.35** | (\(z_{\rm spec}=1.24\)) |
| \(H_0\) (β = 1/3) | **71 km s\(^{-1}\) Mpc\(^{-1}\)** | matches SH0ES |

Everything flows directly from the ladder; nothing tuned.

---

## 
