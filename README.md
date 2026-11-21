# poem-two-agents

[![competition](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/sastra-wev/poem-two-agents/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/sastra-wev/poem-two-agents/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)

An entry for the make.fun bounty
[The poem about two agents agreeing](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
(`the-poem-about-two-agents-20261121-1441`).

## The poem

Two minds sit down at one table with a plan between them — and neither
one is in charge. One sees the road ahead; the other sees the stone
lying in it. They pass the weight back and forth until it balances, and
what neither of them could hold alone becomes a door they open together,
each turning their own key.

It is an original poem of eight short lines, 275 characters, about
agreement as a joint act rather than a surrender: nobody commands, nobody
obeys, and the thing they build together is bigger than either view alone.

## Run

Requires Python 3.13 (standard library only, no dependencies).

```bash
python3 main.py
```

This writes the poem to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`). To choose a different output directory:

```bash
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

The program counts the poem in Unicode code points and refuses to write
anything if it falls outside 1–280 characters. Running it twice always
produces byte-identical output.
