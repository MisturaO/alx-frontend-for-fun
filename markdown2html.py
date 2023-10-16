#!/usr/bin/python3

from sys import argv
import sys
import os


# argv_num = len(argv) -1
if __name__ == "__main__":

    if len(argv) != 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md\n')
        sys.exit(1)

    markdown_file = argv[1]

    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    sys.exit(0)
