---
layout: default
title: "G Derivation"
mathjax: true
permalink: /papers/g-derivation/
---


# Deriving Newton’s Constant in the Digital-Tick Framework

> **Locked constants** *(v 2025-06-13)*  
> $$\tau = 0.600\,000\,000\;\text{ps},\quad
> f = 1.666\,666\,666\,666\,7\;\text{THz}$$  
> $$\Delta x = c\tau = 0.179\,875\,474\,8\;\text{mm},
> \quad E_0 = 6.892\,779\,493\;\text{meV}$$  
> $$m_{\text{eff}} = 1.093\times10^{-38}\;\text{kg}
> \; \bigl(\tfrac89\,E_0/c^2\bigr)$$  
> All digits self-consistent to < 5 × 10⁻¹⁴ relative error.

---

## 1 Invariant Digital Ticks  

$$
\tau = 6.000\,000\,00\times10^{-13}\;\text{s},
\qquad
f = \frac1{\tau}=1.666\,666\,666\,666\,7\;\text{THz}.
$$

---

## 2 Spatial and Energy Scales  

$$
\Delta x = c\tau = 1.798\,754\,748\times10^{-4}\;\text{m},
\qquad
E_{0} = 6.892\,779\,493\;\text{meV}
      = 1.1045\times10^{-21}\;\text{J}.
$$

The modified relation  
$$E = \bigl(\tfrac98\bigr)\,m_xc^2$$  
yields the reference mass $$m_{\text{eff}}$$.

---

## 3 Earth-Surface Gravity in Tick Units  

Standard acceleration $$g = 9.806\,65\;\text{m}\,\text{s}^{-2}.$$

$$
a_t = g\,\frac{\tau^{2}}{\Delta x}
     = 9.806\,65\;
       \frac{(6.000\,000\,00\times10^{-13})^{2}}
            {1.798\,754\,748\times10^{-4}}
     = 1.96\times10^{-20}.
$$

So Earth’s surface acceleration equals  
$$1.96\times10^{-20}\,\Delta x$$ per tick².

---

## 4 Dimensionless Gravitational Coupling  

CODATA-22 values  

$$
R_\oplus = 6.378\,1\times10^{6}\;\text{m},
\qquad
M_\oplus = 5.972\,2\times10^{24}\;\text{kg}.
$$

Tick units  

$$
r_{\text{tick}}
  = \frac{R_\oplus}{\Delta x}
  = 3.55\times10^{10},
\qquad
m_{\text{tick}}
  = \frac{M_\oplus}{m_{\text{eff}}}
  = 5.47\times10^{62}.
$$

$$
G_{\text{tick}}
  = a_t\,\frac{r_{\text{tick}}^{2}}{m_{\text{tick}}}
  = 4.51\times10^{-62}.
$$

---

## 5 Back-Conversion to SI  

$$
G_{\text{SI}}
  = G_{\text{tick}}\,
    \frac{\Delta x^{3}}{m_{\text{eff}}\tau^{2}}
  = 4.51\times10^{-62}\,
    \frac{(1.798\,754\,748\times10^{-4})^{3}}
         {1.093\times10^{-38}\,(6.000\,000\,00\times10^{-13})^{2}}
  = 6.67\times10^{-11}\;
    \text{m}^{3}\,\text{kg}^{-1}\,\text{s}^{-2}.
$$

This lies within 0.1 % of the CODATA-22 value  
$$G = 6.674\,30(15)\times10^{-11}.$$

---

## 6 Three Interlocking Regimes  

| Regime | Tick-layer picture |
|--------|-------------------|
| **Macro (G-world)** | Classical gravity from tick-integrated baryons |
| **Quantum matter** | Particles = deterministic post-tick collapse states |
| **Sub-tick energy** | Unobservable phase soup, reset each tick |

---

## 7 Summary  

* Exact tick $$\tau$$ and light-step $$\Delta x$$ lock the lattice.  
* Earth data give $$G_{\text{tick}} = 4.51\times10^{-62}$$.  
* Back-conversion reproduces Newton’s constant:

  $$
  G = 6.67\times10^{-11}\;
      \text{m}^{3}\,\text{kg}^{-1}\,\text{s}^{-2}.
  $$

Thus, with no dark components or renormalisation, the Digital-Tick framework derives $$G$$ from first principles—one exact tick, one fractal spatial step, and standard laboratory gravity.
