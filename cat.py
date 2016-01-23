#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals
import fileinput

if __name__ == '__main__':
    '''
    This program will read out the contents of the specified files to stdout. Files 
    may be passed as arguments or as stdin.
    '''
    
    for line in fileinput.input():
        if fileinput.isfirstline():
            print("From file %s:\n" % fileinput.filename())

        print(line, end="")
        
    fileinput.close()
