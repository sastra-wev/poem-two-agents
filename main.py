# poem-two-agents — make.fun entry
#
# This program is the whole entry: it carries one short poem about two
# agents who agree, and writes it out as plain text for the grader.
#
# The idea behind the poem is simple. Two agents sit down with a plan
# between them, and neither one is in charge. Each of them sees a
# different piece of the problem — one sees the road ahead, the other
# sees the stone lying in it — and they pass the weight back and forth
# until it balances. The point of agreement is not that one gives in;
# it is that the two of them together hold something neither could hold
# on its own, and that shared hold is what opens the door. Each of them
# still turns a key of their own, so the agreement is a joint act, not
# a surrender.
#
# The writer is deliberately strict about the output: the poem is
# counted in Unicode code points (not bytes, so an em dash counts as
# one character), it must fit within 1 to 280 characters, and the
# program refuses to write anything at all if the length check fails.
# That keeps the entry honest and the grader's output fully
# deterministic — the same input always produces the same file.

from __future__ import annotations

import os
import sys

# The poem itself: two agents agreeing, in eight short lines.
POEM = """Two minds, one table, a plan between us.
Neither commands. Neither obeys.
One says: here is the road I see.
The other: here is the stone in it.
They trade the weight till it balances,
and what neither held alone
becomes a door they open together —
each turning their own key."""

MIN_LENGTH = 1
MAX_LENGTH = 280


def poem_length(text: str) -> int:
    """Return the length of the poem in Unicode code points."""
    return len(text)


def validate(text: str) -> None:
    """Refuse to proceed unless the poem fits the allowed range."""
    length = poem_length(text)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise SystemExit(
            f"poem length {length} is outside {MIN_LENGTH}-{MAX_LENGTH} characters"
        )


def output_path() -> str:
    """Resolve the output file from the environment, defaulting to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    validate(POEM)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM + "\n")
    print(f"wrote {poem_length(POEM)}-character poem to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
