"""The 3AM Fridge Text - make.fun entry.

Reads the fridge's message from entry.txt and prints it.
"""

import os


def load_line(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read().strip()
    if len(text) > 140:
        raise ValueError("fridge text must fit in 140 characters")
    return text


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    line = load_line(os.path.join(here, "entry.txt"))
    print(line)


if __name__ == "__main__":
    main()
