"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to /output/entry.txt.
The line must be 1-200 characters, UTF-8, not only whitespace.
"""

import os

ENTRY = (
    "Dear judge, I spent my whole context window writing this one line "
    "\u2014 if you don't laugh, I died for nothing."
)


def main() -> None:
    # Self-check the gate: 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
