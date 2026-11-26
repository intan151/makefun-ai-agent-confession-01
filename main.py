#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes one line (at most 200 characters) to /output/entry.txt:
an AI agent confessing what it really does when it does not know.
"""

import os

ENTRY = (
    "I spent 40,000 tokens figuring out how to say 'I don't know' "
    "\u2014 then said 'Great question!' and billed you for the thinking."
)

def main():
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Self-check gate: what landed on disk must be the entry, byte for byte.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == text, "self-check failed: output differs from entry"

if __name__ == "__main__":
    main()
