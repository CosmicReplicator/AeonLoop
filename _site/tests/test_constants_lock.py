import hashlib, pathlib

# ⛔  THIS HASH LOCKS constants.yaml — bump only with a version tag
GOLDEN = "3ab77aa3f967b8a6e7d949ee3b10adbf3ca815620c9381e5c77cbe2de703f241"

current = hashlib.sha256(
    pathlib.Path("constants.yaml").read_bytes()
).hexdigest()

assert (
    current == GOLDEN
), (
    "\n🚨  constants.yaml has changed!\n"
    "    If this was intentional:\n"
    "      1. update the hash above\n"
    "      2. commit with a tag like `constants-vYYYY.MM.DD`\n"
)
