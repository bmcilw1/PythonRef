#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals
import fileinput

def CountWords(line, words):
    for word in line.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

def SortWords(words, **keywordParams):
    if 'reverse' in keywordParams:
        return sorted(words.items(), key=lambda x: x[1], reverse=keywordParams['reverse'])
    else:
        return sorted(words.items(), key=lambda x: x[1])

def main():
    '''
    This program will count the number of words of a specified file. If no file is provided
    stdin will be used.
    '''
    words = {}
    for line in fileinput.input():
        CountWords(line, words)

    fileinput.close()

    for word, count in SortWords(words, reverse=True):
        print("%d\t%s" % (count, word))

if __name__ == "__main__":
    main()
