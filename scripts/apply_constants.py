import yaml, decimal, pathlib, re, sys

# ---------- 3.1  load YAML with full precision ----------
with open("constants.yaml", "r", encoding="utf-8") as f:
    # Preserve every digit using Decimal
    data = yaml.safe_load(f)
    def decimalise(obj):
        if isinstance(obj, dict):
            return {k: decimalise(v) for k, v in obj.items()}
        if isinstance(obj, float) or isinstance(obj, int):
            return decimal.Decimal(str(obj))
        return obj
    CONST = decimalise(data)

# ---------- 3.2  helper to fetch nested keys ----------
def get(keypath):
    node = CONST
    for key in keypath.split("."):
        node = node[key]          # raises KeyError if typo
    return node

# ---------- 3.3  compile one regex for {{  key.path  }} ----------
PAT = re.compile(r"\{\{\s*([A-Za-z0-9_.]+)\s*\}\}")

def inject(text, srcpath):
    def repl(m):
        kp = m.group(1)
        try:
            val = get(kp)
        except KeyError:
            print(f"⚠️  unknown constant '{kp}' in {srcpath}")
            return m.group(0)
        # Use 'g' format to preserve all significant digits, no sci-notation unless needed
        return format(val, "f").rstrip("0").rstrip(".") if isinstance(val, decimal.Decimal) else str(val)
    return PAT.sub(repl, text)

# ---------- 3.4  walk every .html/.md in Papers & Ladder ----------
for folder in ("Papers", "Ladder"):
    for path in pathlib.Path(folder).rglob("*.[hm]??"):
        txt = path.read_text(encoding="utf-8")
        new = inject(txt, path)
        if new != txt:
            path.write_text(new, encoding="utf-8")
            print("✔︎", path)

print("Done. Commit the changed files.")
