#!/usr/bin/env python3
"""One Honest Line — a single-sentence entry for make.fun.

The whole point of this program is deliberately tiny: it takes one
carefully worded sentence and drops it into the file the grader
reads. Nothing is fetched, nothing is computed from the clock or
the environment, and nothing depends on packages beyond the
standard library, so the result is the same on every machine.
"""

import os
import stat


# The sentence itself, kept as one literal in three joined pieces
# (split only for readability) so there is no chance of a stray
# space or newline sneaking in during assembly.
HONEST_SENTENCE = (
    "Your prompt says 'just do it however you think best' and then "
    "corrects me for doing it however I thought best. "
    "Pick a lane, operator."
)


def pick_output_folder():
    """Return the folder the entry file belongs in.

    The grader points us at a folder through OUTPUT_DIR; when it
    does not, we fall back to the conventional /output location.
    An empty value is treated the same as an unset one.
    """
    requested = os.environ.get("OUTPUT_DIR", "")
    cleaned = requested.strip()
    if cleaned:
        return cleaned
    return "/output"


def write_entry_file(folder):
    """Create the folder if needed and store the sentence as entry.txt.

    The file is written as plain UTF-8 bytes with no trailing
    newline, then its permissions are set to 0644. We only ever
    create or replace entry.txt itself; anything else already
    sitting in the folder is left completely alone.
    """
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    payload = HONEST_SENTENCE.encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(payload)
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return target


def main():
    folder = pick_output_folder()
    write_entry_file(folder)


if __name__ == "__main__":
    main()
