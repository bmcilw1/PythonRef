#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals
import sys

def main():
    for filename in sys.argv[1:]:
        f = open(filename, 'rU')

        for line in f:
            print(line, end="")
        f.close()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()

