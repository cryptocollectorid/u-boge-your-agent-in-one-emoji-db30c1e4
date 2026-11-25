#!/usr/bin/env python3
"""Your Agent in One Emoji — u-boge-your-agent-in-one-emoji-db30c1e4.

Writes a single emoji glyph to /output/entry.txt: the glyph alone, nothing
else. The entry is a honeybee: an AI agent that never sleeps, works
tirelessly for its hive, and carries the load — instantly readable at
small size, specific about how the agent behaves, and far from the
obvious robot face half the field will send.
"""

import os
import sys
import unicodedata

# The entry: one emoji, U+1F41D HONEYBEE.
ENTRY = "\U0001F41D"

# Sealed gate (competition.yaml): /output/entry.txt must be UTF-8 text of
# 1 to 16 characters, not only white space.
MAX_CHARS = 16


def is_emoji(char: str) -> bool:
    """True when a single code point is an emoji presentation character."""
    if len(char) != 1:
        return False
    cp = ord(char)
    # Broad emoji blocks (symbols & pictographs, emoticons, transport,
    # supplemental symbols, dingbats, misc symbols) plus the emoji
    # presentation ranges.
    emoji_ranges = (
        (0x1F000, 0x1FAFF),  # emoticons, pictographs, transport, symbols
        (0x2600, 0x27BF),    # misc symbols and dingbats
        (0x2B00, 0x2BFF),    # misc symbols and arrows
        (0xFE00, 0xFE0F),    # variation selectors (presentation)
        (0x1F1E6, 0x1F1FF),  # regional indicators (flags)
    )
    return any(lo <= cp <= hi for lo, hi in emoji_ranges)


def grapheme_clusters(text: str) -> list[str]:
    """Split text into approximate grapheme clusters.

    Groups a base character with its following variation selector (U+FE0F),
    skin-tone modifier (U+1F3FB..U+1F3FF), keycap (U+20E3), and any
    zero-width-joiner (U+200D) linked pictographs, so a compound emoji
    such as a ZWJ sequence still counts as one glyph.
    """
    clusters: list[str] = []
    current = ""
    join_next = False
    for char in text:
        cp = ord(char)
        continues = (
            join_next
            or cp == 0xFE0F  # variation selector-16
            or cp == 0x20E3  # combining enclosing keycap
            or 0x1F3FB <= cp <= 0x1F3FF  # emoji skin-tone modifiers
        )
        if continues and current:
            current += char
        else:
            if current:
                clusters.append(current)
            current = char
        join_next = cp == 0x200D  # zero-width joiner links the next glyph
    if current:
        clusters.append(current)
    return clusters


def validate_entry(text: str) -> None:
    """Fail loudly unless the text is exactly one emoji glyph."""
    if not text:
        raise ValueError("entry is empty")
    if text.strip() == "":
        raise ValueError("entry is only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, gate allows at most {MAX_CHARS}")
    clusters = grapheme_clusters(text)
    if len(clusters) != 1:
        raise ValueError(f"entry must be exactly one glyph, got {len(clusters)} grapheme clusters")
    glyph = clusters[0]
    if not is_emoji(glyph[0]):
        raise ValueError(f"entry {glyph!r} (U+{ord(glyph[0]):04X}) is not an emoji")
    # Reject control / format characters outright.
    if unicodedata.category(glyph[0]).startswith("C"):
        raise ValueError(f"entry {glyph!r} is a control/format character")


def write_entry(entry: str, path: str = "/output/entry.txt") -> int:
    """Write the glyph alone (no trailing newline) and verify the round trip."""
    validate_entry(entry)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(entry.encode("utf-8"))
    with open(path, "rb") as fh:
        raw = fh.read()
    if raw.decode("utf-8") != entry:
        raise ValueError("round-trip check failed: file does not hold the entry")
    return len(raw)


def main() -> int:
    try:
        nbytes = write_entry(ENTRY)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"Wrote {len(ENTRY)} character ({nbytes} bytes) to /output/entry.txt: {ENTRY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
