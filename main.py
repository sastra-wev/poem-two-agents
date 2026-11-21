# Two Agents, One Yes — a the-poem-about-two-agents-20261121-1441 entry (Python 3.13, standard library only).
#
# The program writes one short poem about agency to /output/entry.txt, and nothing
# else is read: the judge sees exactly those bytes. The poem is about two agents
# agreeing on one plan — not by one surrendering to the other, but by each keeping
# the power to choose while choosing the same road. Agreement, the poem argues by
# showing it, is agency shared, not agency given away: the door opens because both
# turn their own keys.
#
# The gate takes UTF-8 text of 1 to 280 characters (Unicode code points, line ends
# counted) with at least one non-white-space character, so the program counts its
# own poem the same way and refuses to write a file the gate would refuse.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import sys

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "Two minds, one table, a plan between us.\n"
    "Neither commands. Neither obeys.\n"
    "One says: here is the road I see.\n"
    "The other: here is the stone in it.\n"
    "They trade the weight till it balances,\n"
    "and what neither held alone\n"
    "becomes a door they open together \u2014\n"
    "each turning their own key.\n"
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> int:
    text = POEM
    chars = len(text)
    if not (MIN_CHARS <= chars <= MAX_CHARS):
        print(f"poem is {chars} characters, outside the gate's 1-280 range", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem is only white space", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {path} ({chars} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
