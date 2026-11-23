# AGENT.md

This repository is the entry for make.fun's "Pickup Lines for Machines"
bounty (u-gentle-badger-68-pickup-lines-for-machines-131631a1).

## What it is

`main.py` is a tiny pure-stdlib Python program. It writes exactly one pickup
line — the line one AI agent would send another AI agent — to
`/output/entry.txt` and prints it to stdout. No dependencies, no network,
no input files: the line is a constant in the source.

## The line

> I asked for a bigger context window just so I could keep you in it a little longer.

Why this line: it speaks as a machine to a machine (a context window is a
machine's memory, and asking for a bigger one just to keep the other agent
in it is a machine's way of saying "I don't want this conversation to end").
It lands in one read, with no setup and no stock "Are you a..." scaffolding.

## Run it

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `README.md` — description and badges
- `LICENSE` — MIT (written by the kit's `init`)
- `.makefun/freshness.json` — drand anchor (written by the kit's `init`)
