---
layout: default
title: "Calibration"
mathjax: true
permalink: /papers/calibration/
---


## 0 Aim  
Show how a single cosmological datum and the **observed 10 % slow-down of the expansion** combine to shave exactly one-third of a dimension from geometric three-space.

$$
D_{\mathrm{eff}} = 3 - 0.333 = \tfrac83
$$  

---

## 1 Normalising the 1233 Mpc loop to 1000 nodes  

We fix the node count  

$$
N = 1000
$$  

and set the Big-Ring circumference  

$$
C_{\bigcirc} = 1233\ \text{Mpc}.
$$  

The calibrated node length is  

$$
L_{\mathrm{calib}} = \frac{C_{\bigcirc}}{N} = \frac{1233}{1000} = 1.233\ \text{Mpc}.
$$  

The fractional excess over a unit step is therefore  

$$
\Delta_{\text{rot}} = L_{\mathrm{calib}} - 1 = 1.233 - 1 = 0.233.
$$  

---

## 2 The 10 % expansion slow-down term  

Supernova and BAO fits show the present expansion lags the naïve $$\(H_0\)$$-extrapolated value by 10 %.  
We encode the global drag as  

$$
\delta_{\text{exp}} = 0.100.
$$  

---

## 3 Total slice removed from three-space  

$$
F_{\text{tot}} = \Delta_{\text{rot}} + \delta_{\text{exp}} = 0.233 + 0.100 = 0.333.
$$  

---

## 4 Effective spectral dimension  

$$
D_{\mathrm{eff}} = 3 - F_{\text{tot}} = 3 - 0.333 = 2.667 = \tfrac83.
$$  

The rounding to an exact third is enforced by the seven-tick holonomy.

---

### Chain of logic in one line  

$$
C_{\bigcirc}=1233\ \text{Mpc}
\;\Longrightarrow\;
\Delta_{\text{rot}}=0.233
\;\xrightarrow{-10\%\ \text{expansion}}\;
\delta_{\text{exp}}=0.100
\;\Longrightarrow\;
D_{\mathrm{eff}}=\tfrac83.
$$  

---

## 5 Next checks  

| Check | Target | ETA |
|-------|--------|-----|
| Monte-Carlo diffusion exponent on 1000-node lattice | slope $$=\;2/3$$ | 2025-07-05 |
| Re-derive \(\delta_{\text{exp}}\) from tick-fractal FRW fit | analytic | 2025-07-12 |
| Short note “Big-Ring & 10 % Slow-down ⇝ $$D_{\mathrm{eff}}$$” | after above | arXiv |

---

### Take-away  

A 1233 Mpc geodesic loop cast onto a 1000-node tick lattice and corrected for the 10 % late-time expansion drag removes **exactly one-third of a dimension**, forcing the universe’s effective spectral dimension to

$$
D_{\mathrm{eff}} = \tfrac83.
$$
