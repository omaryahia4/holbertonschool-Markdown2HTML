#!/usr/bin/python3
"""some script to start"""

import sys
import os


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        sys.stderr.write(f"Missing {sys.argv[1]}\n")
        sys.exit(1)

    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
    with open(sys.argv[1], 'w') as file:
        for line in lines:
            line = line.strip()
            if line.startswith("#"):
                level = line.count("#")
                text = line.strip("#").strip()
                html = f"<h{level}>text</h{level}>\n"
                file.write(html)
            else:
                file.write(f"{line}\n")
