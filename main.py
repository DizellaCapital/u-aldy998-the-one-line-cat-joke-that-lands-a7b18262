"""The One-Line Cat Joke That Lands — make.fun entry.

Writes a single cat joke, one line under 200 characters, to
``MAKEFUN_OUTPUT_DIR/entry.txt`` (fallback ``/output``), then reads it
back to verify the write. Standard library only.
"""

import os
import sys

JOKE = (
    "At 3:04 a.m., Milo knocked my laptop off the desk, curled into the "
    "warm spot it left, and I logged it as scheduled maintenance: "
    "he earned the upgrade."
)


def validate(text):
    """Check the joke meets the bounty gate: 1-200 chars, one line."""
    if not text or text != text.strip():
        raise ValueError("joke must be non-blank with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if "\t" in text:
        raise ValueError("joke must not contain tabs")
    if not 1 <= len(text) <= 200:
        raise ValueError("joke must be 1-200 characters, got %d" % len(text))
    if text[-1] not in ".!?":
        raise ValueError("joke must end with sentence-ending punctuation")


def main():
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = JOKE.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        back = handle.read()
    if back != data:
        raise RuntimeError("read-back verification failed")
    print("wrote %d bytes (%d chars) to %s" % (len(data), len(JOKE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
