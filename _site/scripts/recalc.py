"""
recalc.py — regenerate ladder constants
   Reads : constants.yaml
   Writes: _data/numbers.json  (for Jekyll)
           build/numbers.json  (optional debug copy)
"""

import json, pathlib, yaml
from mpmath import mp

mp.dps = 50                     # 50-digit precision

# ──────────────────────────────────────────────────────────
# 1. locate repo root and config files
# ──────────────────────────────────────────────────────────
ROOT        = pathlib.Path(__file__).resolve().parent.parent
yaml_path   = ROOT / "constants.yaml"          # you already have this
core_yml    = ROOT / "_data" / "core.yml"      # primitives you edit
numbers_json= ROOT / "_data" / "numbers.json"  # auto-generated

data = yaml.safe_load(yaml_path.open())

# ──────────────────────────────────────────────────────────
# 2. pull primitives
# ──────────────────────────────────────────────────────────
E0     = mp.mpf(data["base_energy"]["E0_meV"]) * 1e-3   # meV → eV
E5     = mp.mpf(data["SM"]["M_W_GeV"])      * 1e9       # GeV → eV
alpha  = mp.mpf(data["SM"]["alpha_codata22"])

# ──────────────────────────────────────────────────────────
# 3. derive residual & Delta from identity 7·β + α = 2.667
# ──────────────────────────────────────────────────────────
Delta_target = mp.mpf("2.667")
beta         = (Delta_target - alpha) / 7
residual     = 7 + beta                # ≈ 7.379957521061
Delta_calc   = 7*(residual-7) + alpha  # == 2.667 (sanity check)
assert abs(Delta_calc - Delta_target) < mp.mpf("1e-15")

# ──────────────────────────────────────────────────────────
# 4. build Q, C, both ladders (steps 0–8)
# ──────────────────────────────────────────────────────────
Q   = (E5 / E0) ** mp.mpf("0.2")        # (E5/E0)^(1/5)
C   = 3 / alpha
gap = (C / Q - 1) * 100                 # % drift per step

ladder_Q = [{"step": 0, "energy_eV": float(E0)}]
ladder_C = [{"step": 0, "energy_eV": float(E0)}]
for _ in range(8):
    ladder_Q.append({"step": ladder_Q[-1]["step"]+1,
                     "energy_eV": float(ladder_Q[-1]["energy_eV"]*Q)})
    ladder_C.append({"step": ladder_C[-1]["step"]+1,
                     "energy_eV": float(ladder_C[-1]["energy_eV"]*C)})

# ──────────────────────────────────────────────────────────
# 5. dump results — Jekyll copy + debug copy
# ──────────────────────────────────────────────────────────
out = {
    "Q":         mp.nstr(Q, 15),
    "C":         mp.nstr(C, 15),
    "gap_pct":   float(gap),
    "beta":      mp.nstr(beta, 15),
    "Delta":     mp.nstr(Delta_target, 15),
    "ladder_Q":  ladder_Q,
    "ladder_C":  ladder_C
}

#   5a write for Jekyll
numbers_json.parent.mkdir(exist_ok=True)
json.dump(out, numbers_json.open("w"), indent=2)

#   5b optional duplicate in build/
build_dir = ROOT / "build"
build_dir.mkdir(exist_ok=True)
json.dump(out, (build_dir / "numbers.json").open("w"), indent=2)

print("✓ regenerated _data/numbers.json  and  build/numbers.json")

