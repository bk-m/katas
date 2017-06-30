#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple script that opens a file, finds all instances of a regex pattern and
prints them
"""

__author__ = 'bkm'

import re
import sys

PATTERN = r'\[pr\d{4}\]\s(.*\s.*\s.*)'

def get_printers(filename):
    """
    findall() returns a list of tuples, 1 tuple for each group in the regex,
    since there's only 1 group we get a list of strings
    """
    with open(filename) as f:
        content_of_file = f.read()
        return re.findall(PATTERN, content_of_file)

def main():
    """
    Setup as command line tool that prints the results
    """
    if len(sys.argv) <= 1:
        print('<*> Usage: script.py /path/to/file')
        sys.exit(0)
    else:
        try:
            filename = sys.argv[1]
            printers = get_printers(filename)
        except FileNotFoundError:
            print('<*> Usage: script.py /path/to/file')
            sys.exit(0)
        for printer in printers:
            print(printer)

    # --Testing--
    # test_file = 'input.txt'
    # printers = get_printers(test_file)
    # for printer in printers:
    #     print(printer)

if __name__ == '__main__':
    main()
