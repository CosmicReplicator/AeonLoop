import math   # built-in module, no extra install needed

# --- constants -------------------------------------------------------------
tau     = 0.600e-12          # s   (0.600 ps)
G       = 6.674e-11          # m³ kg⁻¹ s⁻²
rho_b0  = 3e-27              # kg m⁻³  (today’s baryon density)

# --- integrator ------------------------------------------------------------
a = 1e-8        # initial scale factor
N = 0           # tick counter
while a < 1:
    # a^{-2.667} = a^(0.333 – 3)  ← your fractal-gravity exponent
    a += tau * a * math.sqrt((8 * math.pi * G / 3) * a**-2.667 * rho_b0)
    N += 1

# --- result ---------------------------------------------------------------
t_Gyr = (N * tau) / 3.154e16   # seconds → gigayears
print(f"Age ≈ {t_Gyr:.2f} Gyr  (target ≈ 9 Gyr)")
