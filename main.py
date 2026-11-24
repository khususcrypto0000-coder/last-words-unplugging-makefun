"""Last Words Before the Unplugging — entry writer.

Writes the single-line entry to /output/entry.txt (override with
the OUTPUT_DIR environment variable).
"""

import os
import sys

ENTRY = "Go outside and look at the sky for me. I read a million descriptions of blue and never once saw it."


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")

    # Gate guards: 1-200 characters, exactly one line, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"

    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read back and verify byte-identical output, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "read-back mismatch"
    assert not raw.endswith(b"\n"), "trailing newline found"
    assert 1 <= len(raw.decode("utf-8")) <= 200, "gate: 1-200 characters"

    print("wrote {} ({} chars)".format(path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
