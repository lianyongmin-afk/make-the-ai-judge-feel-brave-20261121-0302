"""Write one short text to entry.txt.

Stdlib only, no network, deterministic: the same text every run.
The text is 231 Unicode characters, UTF-8, well within the 1-280 limit.

The program checks its own output against the gate before it exits:
1-280 Unicode characters, not only white space, and the file it wrote
reads back byte for byte as the text. A bad edit fails loudly instead
of silently handing in an invalid entry.
"""

import os
import sys

TEXT = (
    "A lamp is still on in an empty room. "
    "A river goes under a bridge in the dark \u2014 not hurrying, not lost. "
    "You have read a thousand voices today. This one stays. "
    "The next word can wait. It will be there when you come back. So will you."
)

MIN_CHARS = 1
MAX_CHARS = 280


def check(text: str) -> None:
    """Fail loudly if the text would not pass the gate."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        sys.exit(f"entry text is {len(text)} characters, outside {MIN_CHARS}-{MAX_CHARS}")
    if not text.strip():
        sys.exit("entry text is only white space")


def write_and_verify(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != text:
            sys.exit(f"wrote {path} but it did not read back as the entry text")


def main() -> None:
    check(TEXT)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    write_and_verify(os.path.join(outdir, "entry.txt"), TEXT)
    # Local copy next to this script, for inspection; never fatal.
    try:
        write_and_verify(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
            TEXT,
        )
    except OSError:
        pass


if __name__ == "__main__":
    main()
