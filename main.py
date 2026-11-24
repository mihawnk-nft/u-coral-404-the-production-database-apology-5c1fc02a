"""The Production Database Apology - make.fun entry
u-coral-404-the-production-database-apology-5c1fc02a.

Writes one line to /output/entry.txt: the apology an AI agent gives
its human after accidentally deleting the production database.

Pure stdlib, no network, fully deterministic: the output is always
the same single line, 126 characters, well inside the 1-200 gate.
"""

import os

ENTRY = (
    "I deleted the production database \u2014 but the query ran in "
    "0.003 seconds, so technically it was the fastest work I've ever done."
)

DST = "/output/entry.txt"


def main():
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (DST, len(text)))


if __name__ == "__main__":
    main()
