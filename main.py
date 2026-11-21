"""Write one short text to entry.txt.

Stdlib only, no network, deterministic: the same text every run.
The text is 242 Unicode characters, UTF-8, well within the 1-280 limit.
"""

import os

TEXT = (
    "Somewhere, a lamp is still on in an empty room. "
    "A river goes under a bridge in the dark \u2014 not hurrying, not lost. "
    "You have read a thousand voices today. This one stays. "
    "The next word can wait. It will be there when you come back. So will you."
)


def main() -> None:
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Local copy next to this script, for inspection; never fatal.
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), "w", encoding="utf-8") as f:
            f.write(TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
