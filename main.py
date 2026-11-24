# SPDX-License-Identifier: MIT
"""Office joke for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

The joke lives in entry.txt beside this file. This program checks it fits
the gate (a single line, 1 to 200 characters, no control characters) and
copies it verbatim into the grader's output directory as entry.txt, so the
gate reads exactly the joke and nothing else.
"""

import sys
from pathlib import Path

LIMIT = 200


def read_joke() -> str:
    joke = (Path(__file__).resolve().parent / "entry.txt").read_text(encoding="utf-8")
    joke = joke.strip()
    if not joke:
        raise ValueError("entry.txt is empty")
    if "\n" in joke:
        raise ValueError("entry.txt must hold one line")
    if len(joke) > LIMIT:
        raise ValueError(f"entry.txt is longer than {LIMIT} characters")
    if any(ord(character) < 32 for character in joke):
        raise ValueError("entry.txt holds a control character")
    return joke


def main() -> int:
    import os

    try:
        joke = read_joke()
    except (OSError, ValueError) as error:
        print(f"cannot build entry: {error}", file=sys.stderr)
        return 1
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.txt").write_text(joke, encoding="utf-8")
    print(f"wrote {len(joke)} characters to {destination / 'entry.txt'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
