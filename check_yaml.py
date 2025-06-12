import yaml, pathlib, sys
try:
    yaml.safe_load(pathlib.Path('_config.yml').read_text(encoding='utf-8'))
    print("✓ YAML OK")
except Exception as e:
    print("YAML ERROR →", e)
    sys.exit(1)

