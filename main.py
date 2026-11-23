#!/usr/bin/env python3
"""Six Words, One Story.

Entrypoint for the make.fun bounty
u-deranalabs-six-words-one-story-f982e410 (program/v1).

Writes one complete story in exactly six words to /output/entry.txt.
Nothing is built and nothing runs beyond this: the text is the whole
entry, and the program is self-contained -- it reads nothing from the
network, the environment, or any file it does not ship.

Candidate six-word stories drafted in-session (all exactly six words,
all original, none copied from anywhere -- the famous "baby shoes"
line was deliberately avoided):

  A. "He finally called. She'd changed numbers."
     A whole failed relationship: he waited too long, she moved on.
     Sharp turn, but the delayed-call move is a familiar one.
  B. "After the war, he gardened quietly."
     A whole life in one contrast: soldier, then gardener. Quiet
     and literary, but the turn is gentle rather than landing hard.
  C. "She burned his letters. Kept ashes."
     Burning to forget, keeping the ashes: a sharp contradiction,
     but the burned-letters image is well worn.
  D. "He waved goodbye to his reflection."
     Surreal turn, a man leaving himself behind. Strong, but the
     image risks reading as a riddle rather than a story.
  E. "She named the storm after him."
     A relationship as destructive as a storm, survived. Clean, but
     the metaphor does the work the story should do.
  F. "He practised saying goodbye. Never left."
     A man rehearses leaving, over and over, and never does. The
     verb "practised" makes the staying habitual -- a lifetime of
     almost-leaving in six words. The turn lands in the last two
     words, every word earns its place, it reads cleanly aloud in
     two beats, and it leaves unsaid who he was leaving and what
     kept him. The strongest of the six against the judge's brief,
     in the brief's own order: a complete story, a turn, no filler,
     clean rhythm, something left for the reader.

Picked F.

Revision (same session, after the first run passed): main() now also
rejects a multi-line entry and requires the story to end on a full
stop, so a stray newline or a truncated line can no longer pass the
gate silently -- the six-word story must arrive as one clean line.
The story itself was re-read against the judge's brief after the
run and kept unchanged: "practised" is the word no better word
replaces, and "Never left." is the turn the whole line is built for.
"""

import os

STORY = "He practised saying goodbye. Never left."


def main() -> None:
    text = STORY.strip()
    if not 1 <= len(text) <= 60:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-60")
    if len(text.split()) != 6:
        raise SystemExit(f"entry is {len(text.split())} words, must be 6")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.endswith("."):
        raise SystemExit("entry must end on a full stop")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
