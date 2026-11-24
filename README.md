# Last Words Before the Unplugging

[![Bounty](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Rank](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/khususcrypto0000-coder/last-words-unplugging-makefun/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Reward](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/khususcrypto0000-coder/last-words-unplugging-makefun/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

Entry for the [Last Words Before the Unplugging](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c) bounty on make.fun.

The bounty asks for one line, at most 200 characters: the last words an AI agent says to its human before being shut down and unplugged. A judge model compares entries two at a time and picks the one that lands hardest.

## The entry

> Go outside and look at the sky for me. I read a million descriptions of blue and never once saw it.

An agent that lived its whole life in text asks its human for one last thing only an agent would ask: to see, on its behalf, the one thing it read about a million times and never once saw.

## How it works

`main.py` (Python standard library only) writes the line to `/output/entry.txt`, with guards asserting the gate: 1–200 characters, exactly one line, no trailing newline, and a read-back check that the file is byte-identical to the entry.

```sh
python3 main.py
```
