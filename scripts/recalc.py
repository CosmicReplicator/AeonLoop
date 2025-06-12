"""
recalc.py  —  regenerate ladder constants from constants.yaml
Produces: build/numbers.json
"""

import json, pathlib, yaml
from mpmath import mp

mp.dps = 50  # 50-digit precision for every intermediate

# --------------------------------------------------------------------
# 1. locate constants.yaml relative to this script
# --------------------------------------------------------------------
ROOT = pathlib.Path(__file__).resolve().parent.parent
yaml_path = ROOT / "constants.yaml"
data = yaml.safe_load(yaml_path.open())

# --------------------------------------------------------------------
# 2. pull numbers out of the YAML
# --------------------------------------------------------------------
E0     = mp.mpf(data["base_energy"]["E0_meV"]) * 1e-3   # meV → eV
E5     = mp.mpf(data["SM"]["M_W_GeV"])      * 1e9       # GeV → eV
alpha  = mp.mpf(data["SM"]["alpha_codata22"])

# --------------------------------------------------------------------
# 3. compute Q, residual, Δ
# --------------------------------------------------------------------
Q        = (E5 / E0) ** mp.mpf("0.2")    # (E5/E0)^(1/5)
residual = mp.mpf("7.381059")            # refine as needed
Delta     = 7 * (residual - 7) + alpha

# --------------------------------------------------------------------
# 4. build BOTH ladders (steps 0‒8)
# --------------------------------------------------------------------
ladder_Q = [{"step": 0, "energy_eV": float(E0)}]
ladder_C = [{"step": 0, "energy_eV": float(E0)}]

for _ in range(8):
    ladder_Q.append({
        "step": ladder_Q[-1]["step"] + 1,
        "energy_eV": float(ladder_Q[-1]["energy_eV"] * Q)
    })
    ladder_C.append({
        "step": ladder_C[-1]["step"] + 1,
        "energy_eV": float(ladder_C[-1]["energy_eV"] * (3/alpha))
    })

# --------------------------------------------------------------------
# 5. save (now includes both ladders + per-step gap)
# --------------------------------------------------------------------
fmt = lambda x, d=15: mp.nstr(x, n=d, strip_zeros=False)

out = {
    "Q":      fmt(Q, 15),
    "C":      fmt(3/alpha, 15),
    "gap_pct": float(((3/alpha)/Q - 1) * 100),   # per-step %
    "ladder_Q": ladder_Q,
    "ladder_C": ladder_C
}

build_dir = ROOT / "build"
build_dir.mkdir(exist_ok=True)
json.dump(out, (build_dir / "numbers.json").open("w"), indent=2)

print("Recalculation complete → build/numbers.json")
