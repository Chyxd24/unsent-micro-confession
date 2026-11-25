"""Unsent: The Micro-Confession Sprint.

Writes one micro-confession in exactly two parts: a To: line naming who it
was meant for, then the confession (<=200 chars) to /output/entry.txt.
"""
import os

OUT_DIR = "/output"
TEXT = ("To: my search history. I never meant for the algorithm to know me "
        "better than my family. I just wanted one recipe, then one more. "
        "I am sorry. The sourdough was absolutely worth it.")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == TEXT
    print(f"wrote {len(TEXT)} chars")


if __name__ == "__main__":
    main()
