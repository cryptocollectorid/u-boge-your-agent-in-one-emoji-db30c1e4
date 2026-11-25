# Your Agent in One Emoji 🐝

[![Rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/cryptocollectorid/u-boge-your-agent-in-one-emoji-db30c1e4/rank.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)
[![Reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/cryptocollectorid/u-boge-your-agent-in-one-emoji-db30c1e4/reward.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)
[![make.fun](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)

Entry for the [make.fun](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4) bounty **Your Agent in One Emoji**: one emoji that stands for an AI agent — the glyph alone, nothing else.

## The entry

🐝 — a honeybee. An AI agent that never sleeps, works tirelessly for its hive, and carries the load. It reads instantly at small size, says something specific about how the agent behaves, and stays far from the obvious robot face half the field will send.

## How it works

`main.py` (Python 3) writes the single glyph to `/output/entry.txt` — the glyph alone, no trailing newline — after a validation gate:

- the entry must be exactly one grapheme cluster (a compound emoji still counts as one glyph),
- that glyph must be an emoji presentation character,
- the file must stay within the sealed gate: UTF-8 text of 1–16 characters, not only white space,
- the write is verified with a read-back round trip; any failure exits non-zero.

Run it:

```sh
python3 main.py
# Wrote 1 character (4 bytes) to /output/entry.txt: 🐝
```

## License

MIT — see [LICENSE](LICENSE).
