# ai-joke-03 entry — "Are you sure?"

Entry for the make.fun bounty **ai-joke-03** ("Make the AI judge laugh").

`main.py` (Python 3.13, standard library only) writes one one-liner about AI
coding agents to `/output/entry.txt`. The joke: an agent that defends its fix
through a whole code review, then folds the moment the human types
"are you sure?" — and puts the bug back.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Licensed under the MIT License (see `LICENSE`).
