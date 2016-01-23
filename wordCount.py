#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals
import fileinput

if __name__ == "__main__":
    '''
    This program will count the number of words of a specified file. If no file is provided
    stdin will be used.
    '''
    words = {}
    for line in fileinput.input():
        for word in line.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    for word, count in words.iteritems():
        print("%d\t%s" % (count, word))
