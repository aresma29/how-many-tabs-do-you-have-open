"""Print the entry number (one number in digits) from entry.txt.

Resolves entry.txt relative to this file so it works from any cwd,
including the grader's read-only run (`python3 -P -s /bot/main.py`).
"""
import os

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
        print(f.read().strip())

if __name__ == "__main__":
    main()
