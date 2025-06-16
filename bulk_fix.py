#!/usr/bin/env python3
import pathlib, re, sys

OLD_DIR  = "Papers"     # original folder
NEW_DIR  = "papers"     # target folder (lowercase)
LAYOUT_RE = re.compile(r"^layout:\s*(paper|papers)\s*$", re.I)

# 1. rename directory once (Git tracks it)
old = pathlib.Path(OLD_DIR)
new = pathlib.Path(NEW_DIR)
if old.exists() and not new.exists():
    old.rename(new)

# 2. walk all *.md files inside repo
for md in pathlib.Path('.').rglob('*.md'):
    txt = md.read_text(encoding='utf-8')

    # replace layout line
    txt = LAYOUT_RE.sub("layout: default", txt)

    # replace any /Papers/ links (case-sensitive)
    txt = txt.replace(f"/{OLD_DIR}/", f"/{NEW_DIR}/")

    # save only if changed
    md.write_text(txt, encoding='utf-8')

print("✅  All files patched.")
