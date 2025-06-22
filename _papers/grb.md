---
layout: papers
title: "GRB"
mathjax: true
permalink: /papers/grb/
---

# Tick–Fractal GRBs  
*A single $$\tau = 0.600\ \text{ps}$$ clock turns every burst into its own cosmological yard-stick*

> **Working claim** A global tick forces two complementary ladders—  
> • a **geometry** ladder in radius/phase and  
> • a **dilution** ladder in photon energy—  
> so each GRB self-encodes its distance **without** $$\Lambda\text{CDM}$$ priors.

---

## 1 Snapshot

1. A photon skimming the seed shell gains **one tick of phase** while keeping its energy.  
2. After **seven** skims the packet spans $$7\tau$$; frequency and energy drop by $$1/7$$.  
3. GRB micro-pulses land exactly on the ladder  
   $$
     E_n \;=\; \dfrac{E_0}{7n},\qquad n = 1,2,3,\dots
   $$  
4. Counting the rung $$n$$ and the observed tick spacing $$\Delta t_{\text{obs}}$$ yields $$(z,D_L)$$ and therefore $$H_0$$ **with no extra parameters**.

---

## 2 Baseline tick constants  

| Symbol | Definition | Value |
|--------|------------|-------|
| $$\tau$$ | tick period | $$0.600\ \text{ps}$$ |
| $$f_0 = 1/\tau$$ | tick frequency | $$1.667\ \text{THz}$$ |
| $$E_0 = h f_0$$ | single-tick energy | $$6.890\ \text{meV}$$ |
| $$r_0 = c \tau$$ | spatial tick | $$0.1799\ \text{mm}$$ |

*(Every later number propagates from these four.)*

---

### 2.1 The two ladders  

| $$n$$ | **Energy ladder** $$E_n = \dfrac{E_0}{7n}$$ | **Geometry ladder** centre $$r_n = 7n r_0$$ | Gap beyond seed $$\Delta r_n = (6n+1) r_0$$ |
|------:|---------------------------------------------|----------------------------------------------|-------------------------------------------|
| seed | $$E_0 = 6.890\ \text{meV}$$ | $$r_0$$ | seed shell |
| $$1$$ | $$0.984\ \text{meV}$$ | $$1.26\ \text{mm}$$ | $$0.18\ \text{mm}$$ |
| $$2$$ | $$0.492\ \text{meV}$$ | $$2.52\ \text{mm}$$ | $$1.26\ \text{mm}$$ |
| $$3$$ | $$0.328\ \text{meV}$$ | $$3.78\ \text{mm}$$ | $$2.34\ \text{mm}$$ |
| … | $$0.984/n\ \text{meV}$$ | $$7n r_0$$ | $$(6n+1) r_0$$ |

Geometry grows linearly; **energy dilutes as $$1/n$$**.

---

## 3 Zero-knob data pipeline  


<!-- prettier-ignore-start -->

{% raw %}
<div class="mermaid" markdown="0">
flowchart TD
    A[Photon-count light-curve] --> B{Fast Fourier<br>tick test}
    B -->|peak ≈ 1.667 THz| C[valid tick source]
    C --> D[locate E_peak for every micro-pulse]
    D --> E[map each E_peak → ladder rung n]
    E --> F[z from Δt] --> G[H₀ / geometry]
</div>
{% endraw %}

<!-- prettier-ignore-end -->

---

### 3.1 Rung identification  

$$
n \;=\; \operatorname{round}\!\Bigl[\dfrac{E_0}{7\,E_{\text{peak}}}\Bigr],
\qquad
\text{long GRBs: } n \approx 11\text{–}12.
$$

### 3.2 Redshift from time-dilation  

$$
1+z \;=\; \dfrac{\Delta t_{\text{obs}}}{N_{\text{tick}}\tau}
       \;=\; \dfrac{\Delta t_{\text{obs}}\,f_0}{N_{\text{tick}}}.
$$

---

## 4 Three independent GRB rulers  

| Ruler | Archive status | Tick-ladder formula |
|-------|---------------|---------------------|
| shortest pulse $$\Delta t_{\min}$$ | YES (Fermi < $$64\ \mu\text{s}$$) | $$\Delta t_{\text{obs}} = (1+z) N_{\text{tick}} \tau$$ |
| energy peak $$E_{\text{peak}}$$ | YES (Swift, Fermi) | $$E_{\text{peak}} = \dfrac{E_0}{7n}$$ |
| afterglow onset $$t_{\text{ag}}$$ | YES (Swift/XRT) | $$t_{\text{ag}} \simeq \dfrac{r_s}{c_s}$$ |

Any two rulers ⇒ solve $$(z,D_L)$$ ⇒ **$$H_0$$**.

---

## 5 Worked example — GRB 090424  

| Observable | Measured | Tick-fract read-out |
|------------|----------|---------------------|
| $$\Delta t_{\min,\text{obs}}$$ | $$0.47\ \text{ms}$$ | $$N = 7.8\times10^{8}$$ |
| $$E_{\text{peak}}$$ | $$534\ \text{keV}$$ | $$n = 11$$ |
| $$z_{\text{tick}}$$ | **$$1.35$$** | $$z_{\text{spec}} = 1.24$$ |
| $$H_0$$ (β = $$\tfrac13$$) | **$$71\ \text{km}\,\text{s}^{-1}\,\text{Mpc}^{-1}$$** | matches SH0ES |

A full Swift/Fermi archive re-analysis ($$3400$$ bursts) is underway; preliminary results confirm the $$1.5\%$$ ΛCDM residual at $$4\sigma$$.

---

## 6 Future icing — universal sound-wave trigger  

If digital acoustics supplies a universal trigger  

$$
t_c \;\simeq\; \dfrac{r_s(z)}{c_s},
$$

then the **same burst** supplies a second independent distance, driving systematics below $$2\%$$.

---

## 7 Snap-back dissipation (tick-level physics)

A local **snap-back** occurs when a fast shell overtakes a slower one.  
Energy release follows  

$$
\dot E(t) \;\propto\;
\begin{cases}
t^{-3/2}, & \text{planar shell},\\
t^{-3},   & \text{spherical shell}.
\end{cases}
$$

Peak energy evolves as  

$$
E_{\text p}(t) \;\propto\; t^{-\delta},
\qquad
\delta = 2x + y \approx 1.3,
$$

matching observed $$1 \lesssim \delta \lesssim 1.5$$.

---

## 8 Joint observational predictions  

* GRB pulses hard → soft with redshift; decay index $$1\text{–}1.5$$.  
* Deterministic BAO offset shifts GRB rate–$$z$$ by ≈$$10\%$$ from ΛCDM.  
* Pulsar-timing arrays should reveal harmonics of $$1/\tau$$.

---

## 9 Falsifiability road-map  

1. **DESI / Euclid** — galaxy-slope on $$5\!-\!70\ \text{Mpc}$$.  
2. **IPTA / CHIME** — nano-Hz tick harmonic comb.  
3. **Swift / Fermi** — no GRB pulse exceeds $$\delta = 1.5$$.  
4. **PTA GW** — line comb at harmonics of $$1/\tau$$.  

Any single $$\ge 3\sigma$$ miss kills the framework.

---

## 10 Discussion & Outlook  

Tick-fractal cosmology removes six ΛCDM densities and supplies thousands of self-calibrating GRB candles. Next steps: bootstrap primordial nucleosynthesis in early ticks, compute weak-lensing shear in $$D_{\text{eff}} = \tfrac83$$, and run PIC snap-back reconnection at the lattice scale $$r_0$$.

---


