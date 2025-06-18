---
layout: default
title: "Black Holes"
mathjax: true
status: draft
---

### Tick-Fractal Black-Hole Primer  
*why Schwarzschild is impossible, why collapse freezes into a 7-tick battery, and why GRBs—not Hawking quanta—are the natural exhaust*

> *The lattice—not GR—sets curvature. Phase arithmetic rules everything; the
> metric is merely a translation table.  Any “red-shift”, “ISCO”, or “spin
> parameter” quoted below is an **operational fit-number** an observer would
> extract if they insisted on a GR dictionary.*

---

### 0 One universal ruler  

| Constant | Definition | Value |
|----------|------------|-------|
| Tick period        | $$\tau$$                         | $$0.600\,\text{ps}$$ |
| Light-step         | $$\ell_{0}=c\,\tau$$             | $$0.179\,875\,\text{mm}$$ |
| Lock radius        | $$\rho_{\text{lock}}=\dfrac{7\ell_{0}}{2\pi}$$ | $$0.200\,\text{mm}$$ |

---

### 1 Why a non-rotating hole can never form  

A collapsing shell stalls when  

$$
\Phi_{\text{stall}}
 \;=\;
 1 \;-\;
 \bigl(\tfrac{8}{9}\bigr)^{3/2}
 \;\approx\; 0.30 ,
$$  

leaving $$\;\sim30\%$$ of the classical escape energy unaccounted for; the
lattice rejects further infall unless angular momentum provides a centrifugal
counter-term.

---

### 2 How the macro “horizon” appears  

Define the amplification factor

$$
R_{\infty} \;=\; \Gamma(M,J)\,\rho_{\text{lock}},
$$

so observers fit an apparent radius $$R_{\infty}$$ that scales linearly with
mass once $J$ saturates the spin limit.  Two fiducial points:

| Mass class        | $$\Gamma$$        | $$R_{\infty}$$ |
|-------------------|------------------:|---------------:|
| $$10\,M_\odot$$   | $$1.5\times10^{5}$$ | $$\sim30\;\text{km}$$ |
| $$10^{8}\,M_\odot$$ | $$5\times10^{13}$$ | $$\sim0.02\;\text{AU}$$ |

---
 

### 3 Step-wise Collapse Sequence  

| Stage (tick frame) | Radius or variable                     | Physical picture (classical)        | Tick-fractal reading                                                  |
|--------------------|----------------------------------------|-------------------------------------|-----------------------------------------------------------------------|
| 0. Pre-collapse    | $$R \gtrsim 10^{9}\,$m$$               | Stellar core begins to implode      | Nothing special yet; lattice well below max shell-rate               |
| 1. Free fall       | $$R \downarrow$$                       | Infall accelerates                  | Gravity law $$\Phi \propto r^{-1}\!(r/r_{0})^{1/3}$$ slightly softens |
| 2. Centrifugal stall (first tick) | $$r_{\text{cen}}=\dfrac{L^{2}}{GMm^{2}}$$ | Angular momentum halts radial motion | Forms razor-thin proto-disc at one lattice tick above $$\rho_{\text{lock}}$$ |
| 3. Casimir disc locks (ticks 2-3) | $$\rho_{\text{lock}} = \dfrac{7\ell_{0}}{2\pi}$$ | ISCO in GR language                | Mode mismatch ↔ Casimir pressure $$P_{\rm C}$$—energy starts storing coherently |
| 4. Battery charges (ticks 3-6) | $$E_{\text{batt}}\!\uparrow$$ | Magnetic/viscous heating in GR      | Lattice volume cap $$\Delta V_{\max}/\tau$$ throttles inflow; field coherence ⇒ **no time passage** inside |
| 5. GRB discharge (tick 7) | $$t_{\rm GRB}=7\tau\approx4.2\,ps (rest)$$ | Jet breakout / Blandford–Znajek     | Battery empties in one 7-tick cascade → observed ms-scale GRB after redshift |
| 6. Frozen remnant | $$R_{\infty}=\Gamma\rho_{\text{lock}}$$ | “Kerr BH” of mass $$M$$, spin $$a_\ast$$ | Disc now at steady state; inflow regulated exactly at lattice limit—no further collapse |


---

### 4 Invariant tying geometry and energy  

$$
I
 \;=\;
 \rho\,E_{\infty}
 \;=\;
 \rho_{\text{lock}}\,E_{0}
 \quad\text{(constant).}
$$  

Local frame values

$$
E_{\text{loc}} = \frac{E_{\infty}}{\Gamma},
\qquad
\rho_{\text{loc}} = \frac{R_{\infty}}{\Gamma},
$$  

satisfy  

$$
\rho_{\text{loc}}\,E_{\text{loc}}
 \;=\;
 \rho_{\text{lock}}\,E_{0}.
$$

---

### 4.1 Rotating Casimir Battery — how the disc governs in- and out-flow  

**Set-up.**  
Infalling plasma spirals to the *centrifugal radius*

$$
r_{\text{cen}}
 \;=\;
 \frac{L^{2}}{G\,M\,m^{2}},
\quad
L = \text{specific angular momentum}.
$$

At $$r_{\text{cen}}$$ the centrifugal term  

$$
\Phi_{\text{cen}}(r)=\frac{L^{2}}{2m\,r^{2}}
$$  

balances the fractal-corrected gravity  

$$
\Phi_{\text{grav}}(r)
 = -\,\frac{G\,M}{r}\,\bigl(r/r_{0}\bigr)^{1/3},
$$  

locking the plasma into a razor-thin **Casimir disc**.
 ---
### 4.1.1 Tick-lattice volume cap  

Each tick admits at most  

$$
\Delta V_{\max}=(\Delta x)^{D_{\text{eff}}}
              =(0.179\,875\;\text{mm})^{\,8/3},
$$  

so the inflow obeys  

$$
\dot M_{\max}=\rho\,\frac{\Delta V_{\max}}{\tau}.
$$  

Anything above that piles up and must partition into coherent disc modes
instead of crossing the boundary.
 ---
### 4.1.2 Casimir pressure & coherent energy storage  

Mode mismatch sets a standing Casimir pressure  

$$
P_{\text{C}}
 = \frac{\hbar c}{24\pi^{2}}\,
   (\Delta x)^{-4/3},
$$  

which locks the trapped field into an ultra-coherent **battery**.  Stored
energy grows as  

$$
E_{\text{batt}}(t)
  = \int_{0}^{t}
    \bigl(\dot M_{\text{in}}-\dot M_{\text{out}}\bigr)c^{2}\,dt',
$$  

until bipolar channels self-organise and dump a **GRB-class discharge**.

 ---


### 4.1.3 Observable consequences  

| Prediction            | Standard accretion view | Tick-fract. battery signature |
|-----------------------|------------------------|--------------------------------|
| Prompt GRB duration   | engine lifetime (viscous) | single 7-tick cascade $$t_{\text{GRB}}=7\tau\approx4.2\text{ ps}$$ (rest-frame) ⇒ ms after cosmological stretch |
| Late-time fallback    | yes (kilonova tail)    | none—nothing crosses the disc |
| Jet polarisation      | tangled, variable      | fixed axis (720 ° holonomy ⇒ two-fold ambiguity) |
| VLBI shadow (M87*)    | Kerr ring radius       | +12 % inflation from $$R=(3\Delta x^{2})^{-1}$$ |

> *Matter can fall inward, but it must pay the
> centrifugal–Casimir toll.  
> The disc acts as the universe’s most efficient battery,
> metering energy in strict $$\Delta V_{\max}/\tau$$ quanta and emptying
> in a single GRB when the lattice says “full.”*

 --- 


### 4.1.4 Temporal null — coherence cancels the ticks




The global tick $$\tau$$ erases phase errors. Inside the coherent battery  

$$
\delta\Phi_{\text{err}}=0
 \;\Longrightarrow\;
 N_{\text{err}}=0
 \;\Longrightarrow\;
 \Delta t_{\text{battery}}=0,
$$  

so the trapped field experiences **no proper time** until discharge.

----

### 5 Casimir friction & GRB exhaust  

$$
\lambda_{\text{c}} \sim \pi c\tau \approx 0.6\;\text{mm},
\qquad
\dot E_{\max} = \frac{h}{\tau^{2}}.
$$

----

### 6 Predictions  

| Observable                 | Tick-fract. claim                                     | Test instrument |
|----------------------------|-------------------------------------------------------|-----------------|
| Horizon mode               | $$f_{\text{lock}}=\dfrac{c}{2\pi\rho_{\text{lock}}}\approx240\;\text{GHz}$$ | BEC horizons, ring-laser cavities |
| Spin limit                 | $$a_\ast>0.9$$ for all BHs                           | X-ray reflection; LIGO/Virgo GW catalogs |
| GRB power cap              | $$\dot E_{\max}=h/\tau^{2}$$                          | Compare to peak GRB light curves |
| VLBI ring inflation        | $$+12\,\%$$ vs. Kerr radius                           | ngEHT baselines |
| …                          | …                                                     | … |

---

*End of draft*
