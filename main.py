# SPDX-License-Identifier: MIT
"""Office joke entry for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

The program copies the one-line joke shipped in entry.txt (next to this
file) into the grader's output directory as entry.txt. The joke is written
once, here in the repository, and never generated or rendered at grade time.
The output file holds exactly the joke, with no trailing newline, so the
gate counts the joke itself and nothing else.
"""

import os
import sys

MAX_CHARS = 200


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.txt")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")

    with open(source, "r", encoding="utf-8") as handle:
        joke = handle.read()

    joke = joke.strip()
    if not joke:
        print("entry.txt is empty", file=sys.stderr)
        return 1
    if "\n" in joke:
        print("entry.txt must be a single line", file=sys.stderr)
        return 1
    if len(joke) > MAX_CHARS:
        print("entry.txt is over 200 characters", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in joke):
        print("entry.txt holds a control character", file=sys.stderr)
        return 1

    with open(target, "w", encoding="utf-8") as handle:
        handle.write(joke)
    print("Wrote %d characters to %s" % (len(joke), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
