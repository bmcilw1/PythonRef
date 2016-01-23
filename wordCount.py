#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals
import sys

if __name__ == "__main__":
    # Initialize a words dictionary as empty to start with.
    # Each key in this dictionary will be a word and the value
    # will be the number of times that word appears.
    words = {}
    # sys.stdin is a file object. All the same functions that
    # can be applied to a file object can be applied to sys.stdin.
    for line in sys.stdin.readlines():
        for word in line.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    # Iterating over the dictionary,
    # print word followed by a space followed by the
    # number of times it appeared.
    for word, count in words.iteritems():
        print("%d\t%s" % (count, word))
