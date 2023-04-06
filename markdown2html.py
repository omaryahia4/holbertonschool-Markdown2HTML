#!/usr/bin/python3
"""
markdown2html.py - Convert a markdown file to HTML format.

Usage: ./markdown2html.py input.md output.html

This script reads a markdown file and writes an HTML file with the same content
but formatted as HTML.
It supports headings, unordered lists, and paragraphs.
"""

from sys import stderr, argv
import os
import markdown


if __name__ == '__main__':

    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    elif os.path.exists(argv[1]) is False:
        print("Missing " + argv[1], file=stderr)
        exit(1)
    else:
        src_file = open(argv[1], "r")
        dest_file = open(argv[2], "w")
        hmtl = markdown.markdown(src_file.read())
        dest_file.write(hmtl + '\n')
        src_file.close()
        dest_file.close()
        exit(0)
