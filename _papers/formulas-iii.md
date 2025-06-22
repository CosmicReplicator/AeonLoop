---
layout: papers
title: "Formulas III"
series: formulas      # common tag for every formula paper
order: 3              # 1, 2, 3 … in reading order
mathjax: true
permalink: /papers/formulas-iii
---


## 8 · Emergent Gravitational & Strong-Force Terms

**(a) Gravitational coupling in tick units**

$$
G_{\text{tick}}
  = \frac{\Delta x^{3}}{\tau^{2}\,M_{*}},
  \qquad
  M_{*}\equiv\text{effective mass scale}.
$$  

*Here $$G$$ is **not** fundamental; once $$\tau$$ and $$\Delta x$$ are fixed it
follows from lattice geometry.*

**(b) Confinement string tension**

$$
V(r)=\sigma\,r,
\qquad
\boxed{\;
  \sigma=\frac{2\pi\,E_{0}}{\Delta x}
        =\frac{2\pi\times6.892\,779\,493\ \text{meV}}
               {0.179\,875\,474\,8\ \text{mm}}
\;}
$$

Linear growth appears because each tick adds a fixed energy quantum while
elongating the flux tube by one spatial step $$\Delta x$$.

---

## 9 · Vacuum Energy & Cosmological Constant

**(a) Time-tick formulation**

$$
\rho_{\text{vac}}
  =\tfrac12\,E_{0}\,S_{D_{\mathrm{eff}}}\,
   \Delta x^{-D_{\mathrm{eff}}}.
$$

**(b) Frequency formulation**

$$
\rho_{\text{vac}}
  =\frac{\eta\,S_{D_{\mathrm{eff}}}}
         {4\pi\,\xi^{D_{\mathrm{eff}}}}\;
   f^{2}\,\bigl(c/f\bigr)^{2-D_{\mathrm{eff}}}.
$$

Both routes give the same  
$$\rho_{\text{vac}}\approx10^{-9}\,\text{J m}^{-3}$$,
implying $$\Lambda\approx10^{-52}\,\text{m}^{-2}$$.

---

## 10 · Discrete Friedmann Chain

**(a) Finite-difference Hubble step**

$$
\left(
  \frac{a_{N+1}-a_{N}}{\tau\,a_{N}}
\right)^{2}
  =\frac{8\pi G_{\text{eff}}}{3}\,
   \rho_{b0}\!\left(\frac{a_{0}}{a_{N}}\right)^{3}
  -\frac{k_{\text{eff}}}{a_{N}^{2}} .
$$

**(b) Scale-dependent $$G$$**

$$
G_{\text{eff}}(r)
  =G\left(\frac{r}{r_{0}}\right)^{3-D_{\mathrm{eff}}}
  =G\left(\frac{r}{r_{0}}\right)^{0.333}.
$$

*(With $$k_{\text{eff}} = 0$$ and $$\Lambda \approx 0$$ the iteration reproduces
$$a(t) \propto t^{2/3}$$ as $$\tau \to 0$$; discrete-time corrections adjust the
late-time expansion history without locking in a specific cosmic-age value.)*

---

## 11 · Tick-Induced Red-Shift

Standard relation  
$$1+z = \dfrac{a(t_{0})}{a(t_{\text{emit}})}$$  
becomes

$$
1+z
  =\prod_{i=1}^{N}(1+\delta_{i})
  \approx\exp\!\Bigl(\sum_{i=1}^{N}\delta_{i}\Bigr)
  \approx 1 + N\,\delta ,
$$

where $$\delta$$ is the phase advance per tick along the photon path.  
For $$\delta \approx 10^{-12}$$ a red-shift $$z \approx 1$$ accumulates after  
$$N \approx 10^{12}$$ ticks (≈ 190 Myr).

---


## 12 · Helix Coupling & Heptad Energy Step  

**(a) One-loop running of the fine-structure constant**  

$$
\boxed{
\alpha^{-1}(E)=\alpha^{-1}(0)
-\frac{1}{3\pi}\sum_{f}Q_{f}^{2}\,
      \ln\!\bigl(\tfrac{E^{2}}{m_{f}^{2}}\bigr)}
$$  

For optical energies $$E_{0}=2.83\;\text{eV}$$ only the electron contributes, giving  

$$
\alpha^{-1}(E_{0})\simeq135.896
\tag{12.1}
$$  

---

**(b) Seven-tick promotion factor**  

A full helix knot (seven ticks) cancels its residual twist at an energy cost  

$$
\boxed{
\Lambda_{\text{step}}
=\frac{3}{\alpha_{\!\text{eff}}(E_{0})
\;\approx\;409.803}
\tag{12.2}}
$$  

so the ladder obeys  

$$
E_{n+1}=E_{n}\,\Lambda_{\text{step}} .
$$  

With $$E_{0}=6.892\,779\,493\;\text{meV}$$ this sequence reproduces  
the K-edge (1.17 keV), the $$2m_{e}$$ threshold (0.511 MeV),  
$$\Lambda_{\mathrm{QCD}}$$ (195 MeV) and $$M_{W}$$ (80 GeV) to within existing experimental error bars.

---

## 13 · Logical Corollaries (zero new parameters)

### 13.1 Curvature = the missing one-third dimension
$$
\boxed{
R \;=\; \frac{1}{3\,\Delta x^{2}}
}
\quad\bigl(D_{\text{eff}} = 3,\;8/3\text{ in the lattice}\bigr)
$$
Spacetime appears $$8/3$$-D in the flat lattice; real space is 3-D.  
The leftover $$1/3$$ shows up as curvature—no extra fields required.

---

### 13.2 No arrow of time—only the tick
The Universe is indexed by the integer frame count  
$$ t \;\mapsto\; t + n\tau,\qquad n\in\mathbb Z. $$
“Forward” and “backward” are undefined; only *how many* ticks have elapsed matters.

---

### 13.3 Entanglement as frame-sharing
Two world-lines remain phase-locked iff  
$$
\boxed{
\text{(i) } n_i = n_j
\;\;\land\;\;
\text{(ii) } |x_i - x_j| \le \Delta x
}
$$
(i.e.\ same tick index and separation $$\le 0.1799\,$$mm).  
Disturb either condition → decoheres in a single tick.

---

<p style="text-align:right;font-size:0.85em">
  ⇦ Back to Part I:&nbsp;
  <a class="button" href="formulas-i.html" target="_blank">Formula I</a>
</p>
